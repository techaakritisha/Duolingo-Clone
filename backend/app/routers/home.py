from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User, Unit, Skill, Lesson

router = APIRouter(
    prefix="/home",
    tags=["Home"]
)


@router.get("/")
def get_home(db: Session = Depends(get_db)):

    user = db.query(User).first()

    units = db.query(Unit).all()

    response = []

    for unit in units:

        skills_data = []

        skills = (
            db.query(Skill)
            .filter(Skill.unit_id == unit.id)
            .all()
        )

        for skill in skills:

            lessons = (
                db.query(Lesson)
                .filter(Lesson.skill_id == skill.id)
                .all()
            )

            skills_data.append({
                "id": skill.id,
                "title": skill.title,
                "lessons": [
                        {
                            "id": lesson.id,
                            "title": lesson.title,
                            "xp_reward": lesson.xp_reward,
                    }
                    for lesson in lessons
                ]
            })

        response.append({
            "id": unit.id,
            "title": unit.title,
            "skills": skills_data,
        })

    return {
        "user": {
            "id": user.id,
            "name": user.name,
            "xp": user.xp,
            "hearts": user.hearts,
            "streak": user.streak,
            "gems": user.gems,
            "daily_goal": user.daily_goal,
        },
        "units": response,
    }