import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# =====================================================
# LOAD FILES
# =====================================================

tfidf = pickle.load(open("tfidf.pkl", "rb"))
tfidf_matrix = pickle.load(open("matrix.pkl", "rb"))
df = pickle.load(open("jobs.pkl", "rb"))

# =====================================================
# COURSE MAPPING
# =====================================================

course_map = {
    "python": "Python for Everybody",
    "sql": "SQL for Data Science",
    "pandas": "Data Analysis with Pandas",
    "numpy": "NumPy Fundamentals",
    "statistics": "Statistics for Data Science",
    "machine learning": "Machine Learning Specialization",
    "deep learning": "Deep Learning Specialization",
    "tensorflow": "TensorFlow Developer Certificate",
    "pytorch": "PyTorch for Deep Learning",
    "nlp": "Natural Language Processing Specialization",
    "scikit learn": "Scikit-Learn for Machine Learning",
    "django": "Django for Beginners",
    "flask": "Flask Web Development",
    "react": "React Complete Guide",
    "flutter": "Flutter & Dart Complete Course",
    "aws": "AWS Cloud Practitioner",
    "docker": "Docker for Developers",
    "kubernetes": "Kubernetes Fundamentals",
    "git": "Git & GitHub Bootcamp"
}

# =====================================================
# JOB RECOMMENDATION
# =====================================================

def recommend_jobs(user_input, top_n=3):

    user_vector = tfidf.transform([user_input.lower()])

    similarities = cosine_similarity(
        user_vector,
        tfidf_matrix
    ).flatten()

    df_temp = df.copy()

    df_temp["score"] = similarities

    df_temp = df_temp.sort_values(
        by="score",
        ascending=False
    )

    df_temp = df_temp.drop_duplicates(
        subset="Job Title"
    )

    return df_temp[
        ["Job Title", "skills", "score"]
    ].head(top_n)

# =====================================================
# SKILL GAP
# =====================================================

def find_skill_gap(user_skills, required_skills):

    user_skills = {
        skill.strip().lower()
        for skill in user_skills
    }

    required_skills = {
        skill.strip().lower()
        for skill in required_skills
    }

    missing = list(required_skills - user_skills)

    return sorted(missing)

# =====================================================
# ROADMAP GENERATOR
# =====================================================

def generate_roadmap(missing_skills):

    beginner_skills = [
        "python",
        "sql",
        "statistics",
        "pandas",
        "numpy",
        "excel",
        "git"
    ]

    intermediate_skills = [
        "scikit learn",
        "machine learning",
        "django",
        "flask",
        "react",
        "angular",
        "nodejs",
        "flutter",
        "android",
        "ios",
        "firebase",
        "mongodb",
        "mysql",
        "postgresql"
    ]

    advanced_skills = [
        "deep learning",
        "tensorflow",
        "pytorch",
        "nlp",
        "aws",
        "azure",
        "docker",
        "kubernetes",
        "spark",
        "hadoop",
        "microservices"
    ]

    roadmap = {
        "Beginner": {
            "duration": "1-2 Months",
            "skills": []
        },
        "Intermediate": {
            "duration": "2-4 Months",
            "skills": []
        },
        "Advanced": {
            "duration": "4-6 Months",
            "skills": []
        }
    }

    for skill in missing_skills:

        if skill in beginner_skills:

            roadmap["Beginner"]["skills"].append(skill)

        elif skill in intermediate_skills:

            roadmap["Intermediate"]["skills"].append(skill)

        elif skill in advanced_skills:

            roadmap["Advanced"]["skills"].append(skill)

        else:

            roadmap["Intermediate"]["skills"].append(skill)

    return roadmap

# =====================================================
# COURSE RECOMMENDER
# =====================================================

def recommend_courses(missing_skills):

    recommendations = {}

    for skill in missing_skills:

        if skill in course_map:

            recommendations[skill] = course_map[skill]

    return recommendations

# =====================================================
# COMPLETE PIPELINE
# =====================================================

def career_roadmap(user_input, user_skills):

    recommendations = recommend_jobs(
        user_input,
        top_n=3
    )

    if recommendations.empty:
        return None

    best_job = recommendations.iloc[0]

    job_title = best_job["Job Title"]

    required_skills = best_job["skills"]

    match_score = round(
        best_job["score"] * 100,
        2
    )

    missing_skills = find_skill_gap(
        user_skills,
        required_skills
    )

    roadmap = generate_roadmap(
        missing_skills
    )

    courses = recommend_courses(
        missing_skills
    )

    return {
        "recommended_job": job_title,
        "match_score": match_score,
        "required_skills": required_skills,
        "missing_skills": missing_skills,
        "roadmap": roadmap,
        "recommended_courses": courses,
        "top_recommendations": recommendations
    }

# =====================================================
# STREAMLIT UI
# =====================================================

st.set_page_config(
    page_title="Personalized Career Roadmap Agent",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Personalized Career Roadmap Agent")

st.write(
    """
    Get personalized career recommendations,
    identify skill gaps,
    generate a learning roadmap,
    and discover relevant courses.
    """
)

user_input = st.text_area(
    "Enter your skills/interests",
    placeholder="python sql machine learning pandas"
)

user_skills = st.text_input(
    "Enter your current skills (comma separated)",
    placeholder="python, sql"
)

if st.button("Generate Career Roadmap"):

    if not user_input.strip():

        st.warning(
            "Please enter your skills/interests."
        )

        st.stop()

    if not user_skills.strip():

        st.warning(
            "Please enter your current skills."
        )

        st.stop()

    user_skills_list = [
        skill.strip().lower()
        for skill in user_skills.split(",")
    ]

    result = career_roadmap(
        user_input,
        user_skills_list
    )

    if result is None:

        st.error(
            "Unable to generate recommendations."
        )

        st.stop()

    # =====================================
    # METRICS
    # =====================================

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Recommended Career",
            result["recommended_job"]
        )

    with col2:
        st.metric(
            "Match Percentage",
            f"{result['match_score']}%"
        )

    st.divider()

    # =====================================
    # TOP 3 RECOMMENDATIONS
    # =====================================

    st.subheader(
        "🏆 Top 3 Career Recommendations"
    )

    for idx, row in enumerate(
        result["top_recommendations"].itertuples(),
        start=1
    ):

        st.write(
            f"{idx}. {row[1]} "
            f"({round(row.score * 100,2)}%)"
        )

    st.divider()

    # =====================================
    # REQUIRED VS MISSING SKILLS
    # =====================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Required Skills")

        for skill in result["required_skills"]:

            st.markdown(
                f"- {skill}"
            )

    with col2:

        st.subheader("❌ Missing Skills")

        for skill in result["missing_skills"]:

            st.markdown(
                f"- {skill}"
            )

    st.divider()

    # =====================================
    # ROADMAP
    # =====================================

    st.subheader(
        "🗺️ Personalized Learning Roadmap"
    )

    roadmap = result["roadmap"]

    for phase, details in roadmap.items():

        if details["skills"]:

            st.markdown(
                f"### {phase} ({details['duration']})"
            )

            for skill in details["skills"]:

                st.markdown(
                    f"✅ {skill}"
                )

    st.divider()

    # =====================================
    # COURSES
    # =====================================

    st.subheader(
        "🎓 Recommended Courses"
    )

    if result["recommended_courses"]:

        for skill, course in result[
            "recommended_courses"
        ].items():

            st.markdown(
                f"🎓 **{skill}** → {course}"
            )

    else:

        st.info(
            "No course recommendations available."
        )

st.divider()

st.caption(
    "Built using NLP, TF-IDF, Cosine Similarity, Skill Gap Analysis, and Streamlit."
)