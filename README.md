# 🎯 Personalized Career Roadmap Agent

An AI-powered NLP-based career guidance system that recommends suitable career paths, identifies skill gaps, generates personalized learning roadmaps, and suggests courses to help users achieve their target careers.

---

## 📌 Project Overview

Choosing the right career path can be challenging for students and job seekers. Many individuals struggle to understand:

- Which career role best matches their skills and interests.
- What skills are required for a desired career.
- Which skills they are currently missing.
- How to systematically learn those missing skills.

This project addresses these challenges by leveraging Natural Language Processing (NLP) and Machine Learning techniques to analyze job descriptions and provide personalized career recommendations.

---

## 🚀 Features

### ✅ Career Recommendation

Recommends the most suitable career paths based on user skills and interests.

### ✅ Top 3 Career Suggestions

Displays the top matching career roles along with match percentages.

### ✅ Skill Gap Analysis

Compares user skills against job requirements and identifies missing skills.

### ✅ Personalized Learning Roadmap

Generates a structured roadmap categorized into:

- Beginner
- Intermediate
- Advanced

with estimated learning durations.

### ✅ Course Recommendations

Suggests relevant learning resources and courses for missing skills.

### ✅ Interactive Dashboard

Built using Streamlit for a simple and user-friendly experience.

---

## 🏗️ System Architecture

```text
User Skills & Interests
            │
            ▼
     NLP Preprocessing
            │
            ▼
      TF-IDF Vectorization
            │
            ▼
      Cosine Similarity
            │
            ▼
   Career Recommendation
            │
            ▼
     Skill Gap Analysis
            │
            ▼
  Learning Roadmap Generator
            │
            ▼
   Course Recommendation Engine
            │
            ▼
      Streamlit Dashboard
```

---

## 📊 Dataset

### Source

Kaggle Dataset:

**Jobs and Job Descriptions Dataset**

Contains:

- Job Titles
- Job Descriptions

Dataset Size:

- 2,277 job postings

---

## 🧠 NLP Pipeline

### 1. Text Cleaning

Performed:

- Lowercasing
- Removal of special characters
- Removal of punctuation
- Removal of extra spaces

### 2. Text Preprocessing

Performed:

- Tokenization
- Stopword Removal
- Lemmatization

### 3. Skill Extraction

Skills are extracted using a predefined skill dictionary containing:

- Programming Languages
- Databases
- Cloud Technologies
- Data Science Skills
- Web Development Skills
- Mobile Development Skills

---

## 🔍 Recommendation Engine

### TF-IDF Vectorization

Job descriptions are converted into numerical vectors using:

```python
TfidfVectorizer
```

### Cosine Similarity

User input is transformed into a vector and compared against all job vectors.

Similarity Score:

```text
Higher Score = Better Career Match
```

---

## 📈 Skill Gap Analysis

The system compares:

```text
Required Skills
            -
User Skills
```

to identify missing competencies.

Example:

```text
Required Skills:
Python
Machine Learning
TensorFlow

User Skills:
Python

Missing Skills:
Machine Learning
TensorFlow
```

---

## 🗺️ Roadmap Generation

Missing skills are organized into learning phases.

### Beginner (1–2 Months)

Examples:

- SQL
- Pandas
- NumPy
- Statistics

### Intermediate (2–4 Months)

Examples:

- Machine Learning
- Scikit-Learn
- Django
- React

### Advanced (4–6 Months)

Examples:

- Deep Learning
- TensorFlow
- PyTorch
- NLP
- AWS

---

## 🎓 Course Recommendation System

Each missing skill is mapped to a recommended learning resource.

Example:

```text
Machine Learning
→ Machine Learning Specialization

TensorFlow
→ TensorFlow Developer Certificate

NLP
→ Natural Language Processing Specialization
```

---

## 🛠️ Technologies Used

### Programming Language

- Python

### NLP

- NLTK

### Machine Learning

- Scikit-Learn

### Data Manipulation

- Pandas
- NumPy

### Visualization / Interface

- Streamlit

### Model Serialization

- Pickle

---

## 📂 Project Structure

```text
career_roadmap_agent/
│
├── app.py
├── jobs.pkl
├── tfidf.pkl
├── matrix.pkl
│
├── notebooks/
│   ├── main.ipynb
│   └── career_agent.ipynb
│
├── requirements.txt
├── README.md
│
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/career-roadmap-agent.git
```

### Move Into Project Folder

```bash
cd career-roadmap-agent
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 💡 Example Usage

### User Input

```text
Skills/Interests:
python sql machine learning pandas

Current Skills:
python, sql
```

### Output

```text
Recommended Career:
Machine Learning Engineer

Match Percentage:
78%

Missing Skills:
Machine Learning
Scikit Learn
TensorFlow
Deep Learning
PyTorch
NLP

Learning Roadmap:
Beginner → Intermediate → Advanced

Recommended Courses:
Machine Learning Specialization
TensorFlow Developer Certificate
PyTorch for Deep Learning
```

---

## 🎯 Learning Outcomes

This project demonstrates:

- Natural Language Processing
- Text Vectorization
- TF-IDF
- Cosine Similarity
- Recommendation Systems
- Skill Gap Analysis
- Career Guidance Systems
- Streamlit Application Development

---

## 🔮 Future Enhancements

### Resume Upload

Allow users to upload resumes in PDF format and automatically extract skills.

### AI-Powered Career Guidance

Integrate Large Language Models (LLMs) to provide personalized career advice.

### Real-Time Job Market Analysis

Fetch live job data from job portals and analyze current market trends.

### Course APIs

Integrate Coursera, Udemy, and LinkedIn Learning APIs for dynamic course recommendations.

### Advanced Skill Extraction

Replace dictionary-based extraction with:

- Named Entity Recognition (NER)
- Sentence Transformers
- Embedding-Based Matching

