import streamlit as st
import pandas as pd
import glob

files = glob.glob("data/attendance_day*.xlsx")
df_list = [pd.read_excel(f) for f in files]
attendance = pd.concat(df_list, ignore_index=True)

students = pd.read_csv("data/students.csv")

df = attendance.merge(students, on="Student_ID")

df["Present"] = df["Status"].apply(lambda x: 1 if x=="Present" else 0)

st.title("Attendance Analytics Dashboard")

st.metric("Total Students", df["Student_ID"].nunique())
st.metric("Average Attendance (%)", round(df["Present"].mean()*100,2))

attendance_rate = df.groupby("Student_ID")["Present"].mean()*100
low_attendance = attendance_rate[attendance_rate < 75]

st.subheader("Low Attendance Students")
st.write(low_attendance)

dept_attendance = df.groupby("Department")["Present"].mean()*100
st.bar_chart(dept_attendance)

daily_attendance = df.groupby("Date")["Present"].mean()*100
st.line_chart(daily_attendance)