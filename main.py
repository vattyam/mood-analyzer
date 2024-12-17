import streamlit as st
import nltk
import glob
from pathlib import Path
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px
import matplotlib

filepaths = sorted(glob.glob("diary/*.txt"))
analyzer = SentimentIntensityAnalyzer()

positive_scores = []
negative_scores = []
dates = []
for filepath in filepaths:
    dates.append(Path(filepath).stem)
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positive_scores.append(scores["pos"])
    negative_scores.append(scores["neg"])

print(dates)
print(positive_scores)
print(negative_scores)

st.title("Diary Tone")
st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positive_scores,
                     labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)
st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negative_scores,
                     labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_figure)

