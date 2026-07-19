from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    Text,
)
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


# ==========================
# User
# ==========================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    xp = Column(Integer, default=0)
    hearts = Column(Integer, default=5)
    streak = Column(Integer, default=0)
    gems = Column(Integer, default=100)

    daily_goal = Column(Integer, default=50)
    last_active = Column(DateTime, default=datetime.utcnow)

    progress = relationship("Progress", back_populates="user")


# ==========================
# Unit
# ==========================
class Unit(Base):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    unit_order = Column(Integer)

    skills = relationship("Skill", back_populates="unit")


# ==========================
# Skill
# ==========================
class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)

    unit_id = Column(Integer, ForeignKey("units.id"))

    title = Column(String)
    skill_order = Column(Integer)

    unit = relationship("Unit", back_populates="skills")
    lessons = relationship("Lesson", back_populates="skill")


# ==========================
# Lesson
# ==========================
class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)

    skill_id = Column(Integer, ForeignKey("skills.id"))

    title = Column(String)

    xp_reward = Column(Integer, default=20)

    skill = relationship("Skill", back_populates="lessons")
    exercises = relationship("Exercise", back_populates="lesson")
    progress = relationship("Progress", back_populates="lesson")


# ==========================
# Exercise
# ==========================
class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)

    lesson_id = Column(Integer, ForeignKey("lessons.id"))

    exercise_type = Column(String)

    question = Column(Text)

    options = Column(Text)

    correct_answer = Column(Text)

    hint = Column(Text)

    lesson = relationship("Lesson", back_populates="exercises")


# ==========================
# Progress
# ==========================
class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    lesson_id = Column(Integer, ForeignKey("lessons.id"))

    completed = Column(Boolean, default=False)

    score = Column(Integer, default=0)

    completed_at = Column(DateTime)

    user = relationship("User", back_populates="progress")
    lesson = relationship("Lesson", back_populates="progress")