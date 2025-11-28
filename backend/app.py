import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import pdfplumber
import docx
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Allowed extensions
ALLOWED = {"pdf", "doc", "docx"}

# Skills to detect
CORE_SKILLS = [
    "python", "java", "javascript", "react", "node", "flask", "django",
    "sql", "mysql", "mongodb", "aws", "docker", "machine learning",
    "deep learning", "nlp", "html", "css", "pytorch", "tensorflow"
]


def extract_pdf(path):
    """Extract text from PDF using pdfplumber"""
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
    return text


def extract_docx(path):
    """Extract text from DOCX using python-docx"""
    doc = docx.Document(path)
    return "\n".join([p.text for p in doc.paragraphs])


def analyze_text(text):
    """Simple rule-based resume analysis"""
    lower = text.lower()
    skills_found = [skill for skill in CORE_SKILLS if skill in lower]

    score = int((len(skills_found) / len(CORE_SKILLS)) * 100)

    suggestions = []

    if "project" not in lower:
        suggestions.append("Add your project details with technologies used.")

    if "experience" not in lower:
        suggestions.append("Mention your work experience clearly.")

    if score < 40:
        suggestions.append("Include more technical skills relevant to your field.")

    return skills_found, score, suggestions


@app.route("/analyze", methods=["POST"])
def analyze():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filename = secure_filename(file.filename)

    if filename == "":
        return jsonify({"error": "Empty filename"}), 400

    ext = filename.rsplit(".", 1)[-1].lower()
    if ext not in ALLOWED:
        return jsonify({"error": "Only PDF, DOC, DOCX allowed"}), 400

    path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(path)

    # Extract text
    try:
        if ext == "pdf":
            text = extract_pdf(path)
        else:
            text = extract_docx(path)
    except Exception as e:
        return jsonify({"error": "Failed to extract text", "detail": str(e)}), 500

    # Analyze
    skills, score, suggestions = analyze_text(text)

    return jsonify({
        "filename": filename,
        "skills": skills,
        "score": score,
        "suggestions": suggestions,
        "snippet": text[:200]
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
