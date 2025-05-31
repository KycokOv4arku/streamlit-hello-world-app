import pandas as pd
import streamlit as st

# hrs per day data points. For now adding them manually.
study = {
    "Jan'24": 51 / 30,
    "Feb'24": 43 / 29,
    "Mar'24": 21 / 31,
    "Apr'24": 24 / 30,
    "May'24": 16 / 31,
    "Jun'24": 55 / 30,
    "Jul'24": 72 / 31,
    "Aug'24": 87 / 31,
    "Sep'24": 75 / 30,
    "Oct'24": 118 / 31,
    "Nov'24": 117 / 30,
    "Dec'24": 38 / 31,
    "Jan'25": 11.5 / 31,
    "Feb'25": 53 / 28,
    "Mar'25": 78.5 / 31,
    "Apr'25": 79 / 30,
    "May'25": 63.5 / 31,
}
# convert into DF and change to index to datetime
df = pd.DataFrame({"month": list(study.keys()), "avg_hours": list(study.values())})
df["avg_hours"] = df.avg_hours.round(1)  # round to 2 decimal places
df["date"] = pd.to_datetime(df["month"], format="%b'%y")  # e.g. “Jan'24” → 2024-01-01

df.set_index("date", inplace=True)
print(df)
st.title("🎓Average hours of study per day")
st.line_chart(df["avg_hours"])
