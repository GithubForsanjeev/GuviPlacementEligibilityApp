
# 📊 Placement Eligibility Streamlit Application

## 🎯 Project Overview

This project is a data-driven **Streamlit web application** designed to evaluate students' placement eligibility based on customizable criteria. It integrates synthetic student performance data and displays insights through interactive dashboards, enabling real-time decision-making for EdTech placement teams.

---

## 🧠 Skills You Will Gain

- ✅ Building data applications using **Streamlit**
- ✅ Generating synthetic datasets using **Faker**
- ✅ Implementing **Object-Oriented Programming (OOP)** in Python
- ✅ Writing optimized **SQL queries** for analytics
- ✅ Interacting with **relational databases** (SQLite/MySQL)
- ✅ Developing **interactive dashboards** for business insights

---

## 🌐 Domain

**Ed Tech**

---

## 🧩 Problem Statement

Design and implement a Streamlit application where users can input **eligibility criteria** for placements (e.g., minimum problem-solving scores or soft skills scores). Based on these inputs, the app filters and displays the eligible students from a dataset stored in a relational database.

---

## 💼 Business Use Cases

- 🎓 **Placement Management**: Shortlist students dynamically using filters.
- 📈 **Student Performance Tracking**: Assess placement readiness using skill metrics.
- 📊 **Interactive Analytics**: Deliver actionable insights to placement teams via visual dashboards.

---

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **Backend**: Python (OOP principles)
- **Database**: SQLite / MySQL
- **Libraries**: Faker, Pandas, SQLAlchemy, Streamlit
- **Other Tools**: Git, VSCode, Jupyter

---

## 🚀 Approach

### Step 1: Dataset Creation
Generate four interlinked tables using **Faker**:
1. **Students Table**: Name, age, gender, city, contact, enrollment and graduation year.
2. **Programming Table**: Language, problems solved, assessments, mini projects, certifications, project scores.
3. **Soft Skills Table**: Scores for communication, teamwork, presentation, leadership, etc.
4. **Placements Table**: Placement status, internship count, interview rounds, company, package, date.

### Step 2: Data Storage
- Store the data in **SQLite** or **MySQL**.
- Use **Python classes** for database operations and relationships.

### Step 3: Streamlit Application
- Accept dynamic input criteria from users (e.g., `problems_solved > 50`, `communication > 75`)
- Show a filtered list of **eligible students**.
- Add download option for filtered results.

### Step 4: SQL Queries & Insights
Write and display **10 insightful queries**, such as:
- Average programming performance by batch
- Top 5 placement-ready students
- Soft skills score distribution
- Certification vs mock interview correlation

---

## 📄 Database Schema

### Students Table
| Column             | Type         | Description                          |
|--------------------|--------------|--------------------------------------|
| student_id         | Primary Key  | Unique ID for each student           |
| name               | String       | Full name                            |
| age                | Integer      | Student age                          |
| gender             | String       | Male / Female / Other                |
| email              | String       | Email address                        |
| phone              | String       | Phone number                         |
| enrollment_year    | Integer      | Year of enrollment                   |
| course_batch       | String       | Batch name                           |
| city               | String       | Residence city                       |
| graduation_year    | Integer      | Graduation year                      |

### Programming Table
| Column               | Description                                 |
|----------------------|---------------------------------------------|
| programming_id       | Primary Key                                 |
| student_id           | Foreign Key to `Students.student_id`        |
| language             | Python, SQL, etc.                            |
| problems_solved      | Total problems solved                        |
| assessments_completed| Number of assessments                       |
| mini_projects        | Number of projects                          |
| certifications_earned| Number of certifications                    |
| latest_project_score | Latest project score                        |

### Soft Skills Table
| Column             | Description                                   |
|--------------------|-----------------------------------------------|
| soft_skill_id      | Primary Key                                   |
| student_id         | Foreign Key to `Students.student_id`          |
| communication      | Out of 100                                    |
| teamwork           | Out of 100                                    |
| presentation       | Out of 100                                    |
| leadership         | Out of 100                                    |
| critical_thinking  | Out of 100                                    |
| interpersonal_skills | Out of 100                                  |

### Placements Table
| Column                 | Description                                |
|------------------------|--------------------------------------------|
| placement_id           | Primary Key                                |
| student_id             | Foreign Key to `Students.student_id`       |
| mock_interview_score   | Score out of 100                            |
| internships_completed  | Count of internships                       |
| placement_status       | Ready / Not Ready / Placed                 |
| company_name           | Name of company (if placed)                |
| placement_package      | Offered package                            |
| interview_rounds_cleared| Rounds cleared                            |
| placement_date         | Date of offer                              |

---

## 📊 Sample SQL Insights

```sql
-- 1. Top 5 Students Ready for Placement
SELECT s.name, pl.mock_interview_score
FROM Students s
JOIN Placements pl ON s.student_id = pl.student_id
WHERE pl.placement_status = 'Ready'
ORDER BY pl.mock_interview_score DESC
LIMIT 5;
```

(Include 10 such queries in a separate SQL file.)

---

## ✅ Project Results

- ✅ Fully functional Streamlit app to filter eligible students.
- ✅ Realistic dataset with OOP-based backend.
- ✅ 10 meaningful SQL insights.
- ✅ Clean modular code and UI with real-time interactivity.

---

## 🧪 Evaluation Metrics

| Metric          | Description                                            |
|-----------------|--------------------------------------------------------|
| ✅ Functionality | Application filters and displays eligible students    |
| ✅ SQL Queries   | Insightful and performant                             |
| ✅ OOP Design    | Proper use of Python classes and modularity           |
| ✅ UI/UX         | Intuitive and interactive frontend with Streamlit     |
| ✅ Documentation | Clear and comprehensive README & code comments        |

---

## 📌 Best Practices Followed

- ✅ PEP8 Python coding standards
- ✅ Environment variables for DB credentials
- ✅ Modular class-based code
- ✅ Git-based version control

---

## 🏷️ Tags

`Streamlit` `Python` `Faker` `SQLite` `SQL` `OOP` `Data Science` `Dashboard Development` `EdTech`

---

## 👨‍💻 Author(s)

**Sanjeev Kumar**  
[GitHub Profile](https://github.com/GithubForsanjeev)  

---

## 📌 Future Enhancements

- Integrate resume parsing for auto student profiling.
- Deploy on cloud (Streamlit Sharing / Heroku).
