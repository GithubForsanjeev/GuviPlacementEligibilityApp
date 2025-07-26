import streamlit as st
import sqlite3
import pandas as pd

# Database connection
def fetch_data(query, params=None):
    conn = sqlite3.connect(r"C:\Users\Sanjeev\Documents\Guvi\GuviPlacementEligibilityApp\student_data.db")
    if params:
        df = pd.read_sql_query(query, conn, params=params)
    else:
        df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Streamlit config
st.set_page_config(page_title="Placement Eligibility App", layout="wide")

# Sidebar Navigation
st.sidebar.title("Home Page")
page = st.sidebar.radio("Navigaton:", ["Eligibility Criteria", "Insights"])

# -------------------------------- Eligibility Criteria --------------------------------
if page == "Eligibility Criteria":
    st.title(" Placement Eligibility Check")
    st.subheader("Filter Students Based on Eligibility Criteria")

    # filters
    placement_status = st.selectbox("Placement Status", ["All", "Ready", "Not Ready"])
    problems_solved = st.slider("Total Problems Solved", 25, 10, 60)
    communication_score = st.slider("Communication Score", 50, 100, 75)
    mock_interview_score = st.slider("Mock Interview Score", 40, 100, 60)
    internships_completed = st.slider("Internship Completed",1 , 3, 1)
    # SQL Query with dynamic filters
    query = """
    SELECT s.student_id, s.name, s.course_batch, s.city, p.problems_solved,
           ss.communication, pl.placement_status, pl.mock_interview_score, pl.internships_completed
    FROM Student_Table s
    JOIN programming_table p ON s.student_id = p.student_id
    JOIN softskills_table ss ON s.student_id = ss.student_id
    JOIN placements_table pl ON s.student_id = pl.student_id
    WHERE p.problems_solved >= ?
      AND ss.communication >= ?
    """
    params = [problems_solved, communication_score]

    if placement_status != "All":
        query += " AND pl.placement_status = ?"
        params.append(placement_status)

    df = fetch_data(query, params=params)

    st.write("### Eligible Students")
    st.write(f"Filter condition: Problems Solved ≥ {problems_solved}, Communication Score ≥ {communication_score}, Placement Status = {placement_status}")
    st.dataframe(df)

# -------------------------------- Analytical Insights --------------------------------
elif page == "Insights":
    st.title("Performance & Placement Insights")

    queries = {
    "1. Students with High Problem Solving Skills (>100 problems solved)": """
        SELECT s.student_id, s.name, s.course_batch, p.problems_solved
        FROM Student_Table s
        JOIN programming_table p ON s.student_id = p.student_id
        WHERE p.problems_solved > 100
        ORDER BY p.problems_solved DESC
    """,
    
    "2. Top 10 Students by Placement Package": """
        SELECT s.student_id, s.name, s.course_batch, pl.placement_package
        FROM Student_Table s
        JOIN placements_table pl ON s.student_id = pl.student_id
        WHERE pl.placement_status = 'Ready'
        ORDER BY pl.placement_package DESC
        LIMIT 10
    """,

    "3. Average Soft Skill Score by Batch": """
        SELECT s.course_batch,
               AVG(ss.communication + ss.teamwork + ss.presentation + ss.leadership + ss.critical_thinking + ss.interpersonal_skills) AS avg_soft_skills
        FROM Student_Table s
        JOIN softskills_table ss ON s.student_id = ss.student_id
        GROUP BY s.course_batch
    """,

    "4. Students Without Any Certifications": """
        SELECT s.student_id, s.name, s.course_batch
        FROM Student_Table s
        LEFT JOIN programming_table p ON s.student_id = p.student_id
        WHERE p.certifications_earned = 0 OR p.certifications_earned IS NULL
    """,

    "5. Count of Students per Programming Language": """
        SELECT p.language, COUNT(*) AS student_count
        FROM programming_table p
        WHERE p.language IS NOT NULL
        GROUP BY p.language
        ORDER BY student_count DESC
    """,

    "6. Students with Strong Presentation Skills (>80)": """
        SELECT s.student_id, s.name, s.course_batch, ss.presentation
        FROM Student_Table s
        JOIN softskills_table ss ON s.student_id = ss.student_id
        WHERE ss.presentation > 80
        ORDER BY ss.presentation DESC
    """,

    "7. Internship to Placement Conversion Ratio": """
        SELECT COUNT(DISTINCT CASE WHEN pl.internships_completed > 0 THEN s.student_id END) AS with_internships,
               COUNT(DISTINCT CASE WHEN pl.placement_status = 'Ready' THEN s.student_id END) AS placed_students,
               ROUND(
                   100.0 * COUNT(DISTINCT CASE WHEN pl.internships_completed > 0 AND pl.placement_status = 'Ready' THEN s.student_id END)
                   / NULLIF(COUNT(DISTINCT CASE WHEN pl.internships_completed > 0 THEN s.student_id END), 0),
                   2
               ) AS conversion_rate_percentage
        FROM Student_Table s
        JOIN placements_table pl ON s.student_id = pl.student_id
    """,

    "8. Students with All-Rounder Skills (High in Programming, Soft Skills, and Mock Interview)": """
        SELECT s.student_id, s.name, s.course_batch, 
               p.problems_solved, ss.communication, ss.leadership, pl.mock_interview_score
        FROM Student_Table s
        JOIN programming_table p ON s.student_id = p.student_id
        JOIN softskills_table ss ON s.student_id = ss.student_id
        JOIN placements_table pl ON s.student_id = pl.student_id
        WHERE p.problems_solved > 80 
          AND (ss.communication + ss.leadership) / 2 > 75
          AND pl.mock_interview_score > 75
    """,

    "9. Students Without Placement Offers": """
        SELECT s.student_id, s.name, s.course_batch
        FROM Student_Table s
        LEFT JOIN placements_table pl ON s.student_id = pl.student_id
        WHERE pl.placement_status IS NULL OR pl.placement_status != 'Ready'
    """,

    "10. Top 5 Batches by Average Mock Interview Score": """
        SELECT s.course_batch, AVG(pl.mock_interview_score) AS avg_mock_score
        FROM Student_Table s
        JOIN placements_table pl ON s.student_id = pl.student_id
        GROUP BY s.course_batch
        ORDER BY avg_mock_score DESC
        LIMIT 5
    """,
}

    selected_query = st.selectbox("Select an Insight", list(queries.keys()))
    result_df = fetch_data(queries[selected_query])

    st.write("### Result:")
    st.dataframe(result_df)
