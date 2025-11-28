🚀 AI Resume Analyzer
A Complete End-to-End AI Project built using React, Tailwind CSS, Flask & NLP
📌 Overview

The AI Resume Analyzer is a smart web application that analyzes resumes (PDF/DOCX) and provides:

Skill extraction

Resume score

Suggestions to improve

AI-powered insights

This project is built using Modern Frontend + Python Backend + NLP.

🎯 Why I Built This Project

I built this project to learn and implement:

✔ Real-world Full-Stack Development

✔ React + Tailwind for professional UI

✔ Flask + NLP for backend analysis

✔ Resume Parsing (PDF + DOCX)

✔ End-to-End API integration

✔ Skill extraction logic

✔ Animated UI using Framer Motion

This project helped me understand how real ATS (Applicant Tracking Systems) work.

✨ Key Features
🧠 AI-Powered Resume Insights

Extracts text from uploaded PDF/DOCX

Identifies technical skills

Calculates resume strength score

Gives suggestions to improve your resume

🎨 Beautiful Modern UI

Tailwind CSS

Custom gradients

Glassmorphism

Animated buttons

Framer Motion transitions

Mobile responsive design

🔥 Custom "Choose File" Button

No default ugly browser styles

Clean & modern UI

Shows selected filename

⚙️ Fully Functional Backend

Python Flask API

PDF parsing using pdfplumber

DOCX parsing using python-docx

Clean file handling

CORS enabled for frontend access

🏗 Tech Stack
Frontend

React + Vite

Tailwind CSS

Framer Motion

Custom CSS animations

Backend

Python

Flask

pdfplumber

python-docx

NLP logic

📂 Project Structure
ai-resume-analyzer/
│
├── frontend/        # React + Tailwind UI
│   ├── src/
│   ├── index.css
│   ├── App.jsx
│   ├── vite.config.js
│
├── backend/         # Flask API
│   ├── app.py
│   ├── requirements.txt
│   ├── uploads/
│
└── README.md

🚀 How to Run the Project
▶️ 1. Run Backend

Open terminal:

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py


Backend runs at:

http://127.0.0.1:5000

▶️ 2. Run Frontend
cd frontend
npm install
npm run dev


Frontend runs at:

http://localhost:5173

🧠 How the AI Analysis Works
✔ 1. Extract text

PDF → pdfplumber

DOCX → python-docx

✔ 2. Convert to lowercase text
✔ 3. Match against a pre-defined skill list
✔ 4. Count matched skills → calculate score
✔ 5. Provide improvement suggestions
📈 Future Improvements

I plan to add:

🔥 JD vs Resume Match

🤖 GPT-based Smart Suggestions

📊 Skill Graphs

🎯 ATS Score

📝 Downloadable Report

❤️ Author

Karibugatha Yaswanth
Passionate AI/ML Developer | Full-Stack Learner

🎉 DONE!
