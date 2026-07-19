from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json

from app.database import get_db
from app.models import Lesson, Exercise

from app.models import User, Progress
from app.schemas import LessonSubmission

router = APIRouter(
    prefix="/lessons",
    tags=["Lessons"]
)


@router.get("/{lesson_id}")
def get_lesson(lesson_id: int, db: Session = Depends(get_db)):

    lesson = db.query(Lesson).filter(
        Lesson.id == lesson_id
    ).first()

    if not lesson:
        raise HTTPException(
            status_code=404,
            detail="Lesson not found"
        )

    exercises = db.query(Exercise).filter(
        Exercise.lesson_id == lesson_id
    ).all()

    return {
        "id": lesson.id,
        "title": lesson.title,
        "xp_reward": lesson.xp_reward,
        "exercises": [
            {
                "id": exercise.id,
                "exercise_type": exercise.exercise_type,
                "question": exercise.question,
                "options": json.loads(exercise.options) if exercise.options else [],
                "correct_answer": exercise.correct_answer,
                "hint": exercise.hint,
            }
            for exercise in exercises
        ]
    }

@router.post("/submit")
def submit_lesson(
    submission: LessonSubmission,
    db: Session = Depends(get_db),
):

    user = db.query(User).first()

    lesson = (
        db.query(Lesson)
        .filter(Lesson.id == submission.lesson_id)
        .first()
    )

    if not lesson:
        raise HTTPException(
            status_code=404,
            detail="Lesson not found"
        )

    exercises = (
        db.query(Exercise)
        .filter(Exercise.lesson_id == submission.lesson_id)
        .all()
    )

    correct = 0
    wrong = 0

    for exercise, answer in zip(exercises, submission.answers):

        if answer.strip().lower() == exercise.correct_answer.strip().lower():
            correct += 1
        else:
            wrong += 1

    # Award XP
    user.xp += lesson.xp_reward

    # Lose hearts
    user.hearts = max(0, user.hearts - wrong)

    progress = Progress(
        user_id=user.id,
        lesson_id=lesson.id,
        completed=True,
        score=correct,
    )

    db.add(progress)
    db.commit()

    return {
        "correct": correct,
        "wrong": wrong,
        "xp": user.xp,
        "hearts": user.hearts,
        "lesson_completed": True,
    }    