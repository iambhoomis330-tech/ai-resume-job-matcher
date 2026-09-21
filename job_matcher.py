from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_text_similarity(resume_text, job_description):
    """Calculate text similarity using TF-IDF."""

    if not resume_text.strip() or not job_description.strip():
        return 0.0

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return round(similarity * 100, 2)


def calculate_skill_match(resume_skills, job_skills):
    """Calculate percentage of required job skills found in resume."""

    if not job_skills:
        return 0.0

    resume_set = {
        skill.lower()
        for skill in resume_skills
    }

    matching_skills = [
        skill
        for skill in job_skills
        if skill.lower() in resume_set
    ]

    score = (
        len(matching_skills) /
        len(job_skills)
    ) * 100

    return round(score, 2)


def calculate_match_score(
    resume_text,
    job_description,
    resume_skills=None,
    job_skills=None
):
    """Calculate combined resume-job match score."""

    text_score = calculate_text_similarity(
        resume_text,
        job_description
    )

    if resume_skills is not None and job_skills is not None:
        skill_score = calculate_skill_match(
            resume_skills,
            job_skills
        )
    else:
        skill_score = 0.0

    final_score = (
        text_score * 0.40
        + skill_score * 0.60
    )

    return round(final_score, 2)


def get_match_level(score):
    """Convert score into a readable category."""

    if score >= 80:
        return "Excellent Match"
    elif score >= 65:
        return "Strong Match"
    elif score >= 50:
        return "Moderate Match"
    elif score >= 35:
        return "Weak Match"
    else:
        return "Low Match"