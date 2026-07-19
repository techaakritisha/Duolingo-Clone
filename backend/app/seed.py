import json

from app.database import SessionLocal
from app.models import User, Unit, Skill, Lesson, Exercise


def add_lesson(db, skill, title, xp, exercises):
    lesson = Lesson(
        skill_id=skill.id,
        title=title,
        xp_reward=xp,
    )
    db.add(lesson)
    db.commit()

    for ex in exercises:
        db.add(
            Exercise(
                lesson_id=lesson.id,
                exercise_type=ex["type"],
                question=ex["question"],
                options=json.dumps(ex.get("options", [])),
                correct_answer=ex["answer"],
                hint=ex["hint"],
            )
        )

    db.commit()


def seed_database():
    db = SessionLocal()

    if db.query(User).first():
        db.close()
        return

    db.add(
        User(
            name="Demo User",
            xp=0,
            hearts=5,
            streak=1,
            gems=100,
            daily_goal=50,
        )
    )
    db.commit()

    units = [
    (
        "Unit 1: Basics",
        [
            (
                "Greetings",
                [
                    {
                        "title": "Hello & Welcome",
                        "xp": 20,
                        "exercises": [
                            {
                                "type": "MCQ",
                                "question": "What is 'Hello' in Spanish?",
                                "options": ["Hola", "Gracias", "Adiós", "Por favor"],
                                "answer": "Hola",
                                "hint": "A common greeting."
                            },
                            {
                                "type": "TYPE",
                                "question": "Type the English word for 'Hola'",
                                "answer": "Hello",
                                "hint": "The most common greeting."
                            },
                            {
                                "type": "MCQ",
                                "question": "Which means 'Goodbye'?",
                                "options": ["Gracias", "Hola", "Adiós", "Sí"],
                                "answer": "Adiós",
                                "hint": "Used when leaving."
                            },
                            {
                                "type": "TYPE",
                                "question": "Type the Spanish word for 'Please'",
                                "answer": "Por favor",
                                "hint": "Used to be polite."
                            },
                            {
                                "type": "MCQ",
                                "question": "How do you say 'Thank you'?",
                                "options": ["Gracias", "Hola", "Buenos días", "Perdón"],
                                "answer": "Gracias",
                                "hint": "You say this after receiving help."
                            },
                        ],
                    },
                    {
                        "title": "Introducing Yourself",
                        "xp": 20,
                        "exercises": [
                            {
                                "type": "MCQ",
                                "question": "What does 'Me llamo' mean?",
                                "options": [
                                    "My name is",
                                    "Good morning",
                                    "Thank you",
                                    "Goodbye",
                                ],
                                "answer": "My name is",
                                "hint": "Used while introducing yourself."
                            },
                            {
                                "type": "TYPE",
                                "question": "Type the Spanish word for 'Name'",
                                "answer": "Nombre",
                                "hint": "Starts with N."
                            },
                            {
                                "type": "MCQ",
                                "question": "How do you say 'Nice to meet you'?",
                                "options": [
                                    "Mucho gusto",
                                    "Buenos días",
                                    "Hasta luego",
                                    "Perdón",
                                ],
                                "answer": "Mucho gusto",
                                "hint": "A polite introduction phrase."
                            },
                            {
                                "type": "TYPE",
                                "question": "Type the Spanish word for 'I am'",
                                "answer": "Yo soy",
                                "hint": "Starts with Yo."
                            },
                            {
                                "type": "MCQ",
                                "question": "What does '¿Cómo estás?' mean?",
                                "options": [
                                    "How are you?",
                                    "Where are you?",
                                    "Who are you?",
                                    "Good night",
                                ],
                                "answer": "How are you?",
                                "hint": "A common greeting question."
                            },
                        ],
                    },
                    {
                        "title": "Common Expressions",
                        "xp": 20,
                        "exercises": [
                            {
                                "type": "MCQ",
                                "question": "What is 'Good Morning' in Spanish?",
                                "options": [
                                    "Buenos días",
                                    "Buenas noches",
                                    "Buenas tardes",
                                    "Hola",
                                ],
                                "answer": "Buenos días",
                                "hint": "Used before noon."
                            },
                            {
                                "type": "TYPE",
                                "question": "Type the Spanish word for 'Sorry'",
                                "answer": "Lo siento",
                                "hint": "Used to apologize."
                            },
                            {
                                "type": "MCQ",
                                "question": "How do you say 'See you later'?",
                                "options": [
                                    "Hasta luego",
                                    "Gracias",
                                    "Hola",
                                    "Sí",
                                ],
                                "answer": "Hasta luego",
                                "hint": "Used while leaving."
                            },
                            {
                                "type": "TYPE",
                                "question": "Type the Spanish word for 'Excuse me'",
                                "answer": "Perdón",
                                "hint": "Starts with P."
                            },
                            {
                                "type": "MCQ",
                                "question": "What is 'Good Night' in Spanish?",
                                "options": [
                                    "Buenas noches",
                                    "Buenos días",
                                    "Hola",
                                    "Adiós",
                                ],
                                "answer": "Buenas noches",
                                "hint": "Used before sleeping."
                            },
                        ],
                    },
                ],
            ),
        ],
    ),
]

    lesson_order = 1

    for unit_order, (unit_name, skills) in enumerate(units, start=1):

        unit = Unit(
            title=unit_name,
            unit_order=unit_order,
        )

        db.add(unit)
        db.commit()

        for skill_order, (skill_name, lessons) in enumerate(skills, start=1):

            skill = Skill(
                unit_id=unit.id,
                title=skill_name,
                skill_order=skill_order,
            )

            db.add(skill)
            db.commit()

            for lesson in lessons:

                exercises = [
                    {
                        "type": "MCQ",
                        "question": f"What is the correct translation in {lesson}?",
                        "options": [
                            "Option A",
                            "Option B",
                            "Option C",
                            "Option D",
                        ],
                        "answer": "Option A",
                        "hint": "Choose the first option.",
                    },
                    {
                        "type": "TYPE",
                        "question": f"Type the correct word for {lesson_name}",
                        "answer": "Answer",
                        "hint": "Starts with A.",
                    },
                    {
                        "type": "MCQ",
                        "question": f"Select the correct sentence for {lesson_name}",
                        "options": [
                            "Sentence 1",
                            "Sentence 2",
                            "Sentence 3",
                            "Sentence 4",
                        ],
                        "answer": "Sentence 2",
                        "hint": "Think carefully.",
                    },
                    {
                        "type": "TYPE",
                        "question": f"Complete the phrase in {lesson_name}",
                        "answer": "Correct",
                        "hint": "Simple word.",
                    },
                    {
                        "type": "MCQ",
                        "question": f"Final question of {lesson_name}",
                        "options": [
                            "Choice 1",
                            "Choice 2",
                            "Choice 3",
                            "Choice 4",
                        ],
                        "answer": "Choice 3",
                        "hint": "Read all options.",
                    },
                ]

                add_lesson(
                    db,
                    skill,
                    lesson["title"],
                    lesson["xp"],
                    lesson["exercises"],
                )
                lesson_order += 1

    db.close()


if __name__ == "__main__":
    seed_database()