import pandas as pd
import re


def load_skills():
    """Load skills from the skills database."""
    return pd.read_csv("data/skills.csv")


def extract_skills(text):
    """Extract known skills from resume or job description text."""

    skills_df = load_skills()

    text_lower = text.lower()
    found_skills = []

    for skill in skills_df["skill"]:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return sorted(set(found_skills))


def get_skill_categories(skills):
    """Return categories for detected skills."""

    skills_df = load_skills()

    matched = skills_df[
        skills_df["skill"].isin(skills)
    ]

    return matched[["skill", "category"]]

if __name__ == "__main__":
    sample_text = """
    I am a Data Science student with experience in Python,
    Pandas, NumPy, SQL, Machine Learning, Scikit-learn,
    Power BI and GitHub.
    """

    skills = extract_skills(sample_text)

    print("Detected Skills:")
    print(skills)

    print("\nSkill Categories:")
    print(get_skill_categories(skills))