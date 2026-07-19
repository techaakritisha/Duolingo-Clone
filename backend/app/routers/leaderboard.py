from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User

router = APIRouter(
    prefix="/leaderboard",
    tags=["Leaderboard"]
)


@router.get("/")
def get_leaderboard(db: Session = Depends(get_db)):

    users = (
        db.query(User)
        .order_by(User.xp.desc())
        .all()
    )

    leaderboard = []

    for rank, user in enumerate(users, start=1):
        leaderboard.append({
            "rank": rank,
            "name": user.name,
            "xp": user.xp,
            "streak": user.streak,
        })

    return leaderboard