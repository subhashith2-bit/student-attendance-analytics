# student-attendance-analytics
An interactive attendance analytics dashboard that processes multi-source Excel data to generate insights on student performance, attendance trends, and low attendance detection using Python, Pandas, and Streamlit.
#  Attendance Analytics Dashboard

##  Project Overview

This project is an **Attendance Analytics System** that processes student attendance data from multiple Excel files and generates meaningful insights using data analysis and visualization.

It provides an interactive **Streamlit dashboard** to monitor attendance trends, identify low-performing students, and analyze performance across departments, subjects, and time.


##  Features

*  Multi-file data processing (Excel files)
*  Student attendance percentage calculation
*  Low attendance detection (<75%)
*  Department-wise analysis
*  College-wise analysis
*  Subject-wise insights
*  Attendance trend visualization
*  Student search functionality
*  Interactive dashboard using Streamlit


##  Tech Stack

* **Python**
* **Pandas** (Data Processing)
* **Matplotlib** (Visualization)
* **Streamlit** (Dashboard)
* **OpenPyXL** (Excel Handling)


##  Project Structure

attendance_project/
├── data/
   ├── students.csv
   ├── attendance_day1.xlsx
   ├── attendance_day2.xlsx
   ├── attendance_day3.xlsx
   ├── attendance_day4.xlsx
├── notebook/
   └── analysis.ipynb
├── app.py
└── README.md


# Installation & Setup

1. Clone the repository:

```
git clone https://github.com/your-username/attendance-analytics-dashboard.git
cd attendance-analytics-dashboard
```

2. Install dependencies:

pip install pandas matplotlib streamlit openpyxl

3. Run the dashboard:

python -m streamlit run app.py

---

## Sample Insights

* Identify students with attendance below 75%
* Compare attendance across departments
* Detect subjects with low participation
* Analyze attendance trends over time

---

##  Dashboard Preview

*(Add your dashboard screenshot here)*

---

##  Future Improvements

*  Attendance prediction using Machine Learning
*  Student clustering (regular vs irregular)
*  Automated alert system
*  Deploy dashboard online

---

# Use Cases

* Universities & Colleges
* Coaching Institutes
* EdTech Platforms
* Corporate Training Programs
