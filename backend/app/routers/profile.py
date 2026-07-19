from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


@router.get("/")
def get_profile(db: Session = Depends(get_db)):
    user = db.query(User).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user.id,
        "name": user.name,
        "xp": user.xp,
        "hearts": user.hearts,
        "streak": user.streak,
        "gems": user.gems,
        "daily_goal": user.daily_goal,
    }