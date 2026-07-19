This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```
# 🦉 Duolingo Clone

A simplified Duolingo-inspired language learning platform built using FastAPI and Next.js.

---

## Features

- Home Dashboard
- Interactive Lessons
- Multiple Choice Questions
- Fill in the Blank Questions
- XP Reward System
- Hearts
- Streak Counter
- Profile Page
- Leaderboard
- Responsive UI

---

## Tech Stack

### Frontend

- Next.js 16
- TypeScript
- Tailwind CSS
- Axios

### Backend

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

---

## Project Structure

```
DuolingoClone/

│
├── backend/
│   ├── app/
│   ├── database.db
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## Backend Setup

```bash
cd backend

python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
uvicorn app.main:app --reload
```

Backend runs on

```
http://localhost:8000
```

---

## Frontend Setup

```bash
cd frontend
```

Install packages

```bash
npm install
```

Run

```bash
npm run dev
```

Frontend runs on

```
http://localhost:3000
```

---

## API Endpoints

### Home

```
GET /home
```

### Lesson

```
GET /lessons/{id}
```

### Submit Lesson

```
POST /lessons/submit
```

### Profile

```
GET /profile
```

### Leaderboard

```
GET /leaderboard
```

---

## Screens

- Home
- Lesson
- Profile
- Leaderboard

---

## Future Improvements

- Authentication
- Real Progress Tracking
- Daily Challenges
- Sound Effects
- Achievements
- Multiple Languages
- Dark Mode

---

## Author

Aakriti Shakya
Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
