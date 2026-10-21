# Student Attendance Analytics

An attendance analytics project built using Python and Pandas to analyze student attendance data from multiple Excel files.

The project calculates attendance percentages, identifies students with low attendance, and provides insights by department, college, subject, and date.

## Project Overview

This project was built to practice a complete data analysis workflow:

- Loading data from multiple Excel files
- Cleaning and combining datasets
- Calculating attendance percentages
- Identifying students with attendance below 75%
- Analyzing attendance across departments and subjects
- Creating visualizations
- Building an interactive dashboard using Streamlit

## Key Analysis

The project focuses on questions such as:

- Which students have attendance below 75%?
- Which departments have the highest and lowest attendance?
- Which subjects have lower attendance?
- How does attendance change over time?
- How many students fall below the required attendance level?

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- Streamlit
- OpenPyXL
- Excel

## Project Structure

```text
student-attendance-analytics/
│
├── data/
│   ├── students.csv
│   ├── attendance_day1.xlsx
│   ├── attendance_day2.xlsx
│   ├── attendance_day3.xlsx
│   └── attendance_day4.xlsx
│
├── notebook/
│   └── analysis.ipynb
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
Dashboard
The project includes an interactive Streamlit dashboard for exploring attendance data.
Dashboard Features
- Attendance percentage overview
- Low attendance student detection
- Department-wise analysis
- College-wise analysis
- Subject-wise analysis
- Attendance trends
- Student search
How to Run
1. Clone the repository
git clone https://github.com/subhashith2-bit/student-attendance-analytics.git
cd student-attendance-analytics

2. Install the required libraries
pip install -r requirements.txt

3. Run the Streamlit dashboard
python -m streamlit run app.py

Sample Insights
The analysis can be used to identify:
- Students below the 75% attendance threshold
- Departments with attendance differences
- Subjects with lower participation
- Attendance patterns over multiple days
Future Improvements
- Add attendance prediction using machine learning
- Add automated alerts for low attendance
- Improve dashboard visualizations
- Deploy the dashboard online
Author
Subhashith N
