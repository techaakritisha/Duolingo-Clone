from pydantic import BaseModel
from typing import List


# ---------- HOME ----------

class LessonSummary(BaseModel):
    id: int
    title: str
    xp_reward: int
    completed: bool

    class Config:
        from_attributes = True


class SkillResponse(BaseModel):
    id: int
    title: str
    lessons: List[LessonSummary]


class UnitResponse(BaseModel):
    id: int
    title: str
    skills: List[SkillResponse]


class UserResponse(BaseModel):
    id: int
    name: str
    xp: int
    hearts: int
    streak: int
    gems: int
    daily_goal: int


class HomeResponse(BaseModel):
    user: UserResponse
    units: List[UnitResponse]


# ---------- LESSON ----------

class ExerciseResponse(BaseModel):
    id: int
    exercise_type: str
    question: str
    options: List[str]
    correct_answer: str
    hint: str

    class Config:
        from_attributes = True


class LessonResponse(BaseModel):
    id: int
    title: str
    xp_reward: int
    exercises: List[ExerciseResponse]

    class Config:
        from_attributes = True


class LessonSubmission(BaseModel):
    lesson_id: int


# ---------- PROFILE ----------

class ProfileResponse(BaseModel):
    id: int
    name: str
    xp: int
    hearts: int
    streak: int
    gems: int
    daily_goal: int


# ---------- LEADERBOARD ----------

class LeaderboardUser(BaseModel):
    id: int
    name: str
    xp: int