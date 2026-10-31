import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Breast Cancer EDA Dashboard",
    page_icon="🎗️",
    layout="wide"
)
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #C2185B;
}
}
h1, h2, h3 {
    color: black !important;
}
}
[data-testid="stMetric"] {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #D1E7D5;
}
</style>
""", unsafe_allow_html=True)
st.title("🎗️ Breast Cancer Data Analysis")
st.write("Exploratory Data Analysis Dashboard")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("Breast_Cancer.csv")

df = load_data()
st.sidebar.header("Dashboard Filters")

selected_status = st.sidebar.multiselect(
    "Select Patient Status",
    options=df["Status"].unique(),
    default=df["Status"].unique()
)

filtered_df = df[df["Status"].isin(selected_status)]
selected_age = st.sidebar.slider(
    "Select Age Range",
    min_value=int(df["Age"].min()),
    max_value=int(df["Age"].max()),
    value=(int(df["Age"].min()), int(df["Age"].max()))
)

filtered_df = filtered_df[
    (filtered_df["Age"] >= selected_age[0]) &
    (filtered_df["Age"] <= selected_age[1])
]
df = filtered_df
selected_tumor = st.sidebar.slider(
    "Select Tumor Size",
    min_value=int(df["Tumor Size"].min()),
    max_value=int(df["Tumor Size"].max()),
    value=(int(df["Tumor Size"].min()), int(df["Tumor Size"].max()))
)

filtered_df = filtered_df[
    (filtered_df["Tumor Size"] >= selected_tumor[0]) &
    (filtered_df["Tumor Size"] <= selected_tumor[1])
]
selected_race = st.sidebar.multiselect(
    "Select Patient Race",
    options=df["Race"].unique(),
    default=df["Race"].unique()
)

filtered_df = filtered_df[
    filtered_df["Race"].isin(selected_race)
]
selected_marital = st.sidebar.multiselect(
    "Select Marital Status",
    options=df["Marital Status"].unique(),
    default=df["Marital Status"].unique()
)

filtered_df = filtered_df[
    filtered_df["Marital Status"].isin(selected_marital)
]
df = filtered_df
st.sidebar.metric("Filtered Patients", len(df))
if st.sidebar.button("Reset Filters"):
    st.session_state.clear()
    st.rerun()
st.success("Dataset loaded successfully!")

st.write("### Dataset Preview")
st.dataframe(df.head())

st.write("### Dataset Information")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", df.shape[0])
col2.metric("Total Columns", df.shape[1])
col3.metric("Missing Values", int(df.isnull().sum().sum()))

st.write("### Dataset Statistics")
st.write("### Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Average Age", round(df["Age"].mean(), 1))
col2.metric("Average Tumor Size", round(df["Tumor Size"].mean(), 1))
col3.metric("Average Survival Months", round(df["Survival Months"].mean(), 1))
st.dataframe(df.describe())

st.write("### Survival Status Distribution")
st.write("### Age Distribution")
st.write("### Tumor Size Distribution")
st.write("### Survival Months Distribution")

fig = px.histogram(
    df,
    x="Survival Months",
    nbins=20,
    title="Distribution of Survival Months"
)
st.write("### Patients by Race")

fig = px.histogram(
    df,
    x="Race",
    color="Race",
    title="Number of Patients by Race"
)
# Marital Status Distribution

st.write("### Patients by Marital Status")

fig = px.histogram(
    df,
    x="Marital Status",
    color="Marital Status",
    title="Patients by Marital Status"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="marital_status_chart"
)
st.plotly_chart(fig, use_container_width=True)
st.plotly_chart(fig, use_container_width=True, key="race_chart")
# Tumor Stage Distribution

st.write("### Patients by Tumor Stage")
# 6th Stage Distribution

st.write("### Patients by 6th Stage")

fig = px.histogram(
    df,
    x="6th Stage",
    color="6th Stage",
    title="Distribution of Patients by 6th Stage"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="sixth_stage_chart"
)
# Correlation Heatmap

st.write("### Correlation Heatmap")

numeric_df = df.select_dtypes(include="number")

fig = px.imshow(
    numeric_df.corr(),
    text_auto=True,
    aspect="auto",
    title="Correlation Between Numerical Features",
    color_continuous_scale="RdYlGn"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="correlation_heatmap"
)
# Estrogen Status Distribution

st.write("### Estrogen Status Distribution")

fig = px.histogram(
    df,
    x="Estrogen Status",
    color="Estrogen Status",
    title="Patients by Estrogen Status"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="estrogen_status_chart"
)
# Progesterone Status Distribution

st.write("### Progesterone Status Distribution")

fig = px.histogram(
    df,
    x="Progesterone Status",
    color="Progesterone Status",
    title="Patients by Progesterone Status"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="progesterone_status_chart"
)
# Grade Distribution

st.write("### Patients by Grade")

fig = px.histogram(
    df,
    x="Grade",
    color="Grade",
    title="Distribution of Patients by Grade"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="grade_distribution_chart"
)
# A Stage Distribution

st.write("### Patients by A Stage")

fig = px.histogram(
    df,
    x="A Stage",
    color="A Stage",
    title="Distribution of Patients by A Stage"
)
# Differentiate Distribution

st.write("### Patient Differentiation")

fig = px.histogram(
    df,
    x="differentiate",
    color="differentiate",
    title="Distribution of Patients by Differentiation"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="differentiate_chart"
)
# Regional Nodes Analysis

st.write("### Regional Nodes Analysis")

fig = px.scatter(
    df,
    x="Regional Node Examined",
    y="Reginol Node Positive",
    color="Status",
    title="Regional Nodes Examined vs Positive"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="regional_nodes_chart"
)
st.plotly_chart(
    fig,
    use_container_width=True,
    key="a_stage_chart"
)
fig = px.histogram(
    df,
    x="T Stage ",
    color="T Stage ",
    title="Distribution of Tumor Stages"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="tumor_stage_chart"
)
fig = px.histogram(
    df,
    x="Tumor Size",
    nbins=20,
    title="Distribution of Tumor Sizes"
)

st.plotly_chart(fig, use_container_width=True)
st.plotly_chart(fig, use_container_width=True, key="patients_by_race")
fig = px.histogram(
    df,
    x="Age",
    nbins=20,
    title="Distribution of Patients by Age"
)

st.plotly_chart(fig, use_container_width=True)

fig = px.pie(
    df,
    names="Status",
    title="Alive vs Dead"
)

st.plotly_chart(fig, use_container_width=True)
st.write("## Key Insights")

alive = (df["Status"] == "Alive").sum()
dead = (df["Status"] == "Dead").sum()
total = len(df)

col1, col2, col3 = st.columns(3)

col1.metric("🟢 Alive Patients", alive, f"{alive/total*100:.1f}%")
col2.metric("🔴 Dead Patients", dead, f"{dead/total*100:.1f}%")
col3.metric("👥 Total Patients", total)
st.write("### Survival Rate by Tumor Stage")

survival_by_stage = df.groupby("6th Stage")["Status"].apply(
    lambda x: (x == "Alive").mean() * 100
).reset_index()

survival_by_stage.columns = ["Tumor Stage", "Survival Rate (%)"]

fig = px.bar(
    survival_by_stage,
    x="Tumor Stage",
    y="Survival Rate (%)",
    color="Survival Rate (%)",
    title="Patient Survival Rate Across Tumor Stages",
    text_auto=".1f"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="survival_by_stage_chart"
)
st.write("### 2. Average Survival by Age Group")

df["Age Group"] = pd.cut(
    df["Age"],
    bins=[0, 40, 50, 60, 70, 100],
    labels=["Below 40", "40–50", "50–60", "60–70", "Above 70"]
)

age_survival = df.groupby("Age Group", observed=True)["Survival Months"].mean().reset_index()

fig = px.bar(
    age_survival,
    x="Age Group",
    y="Survival Months",
    color="Survival Months",
    title="Average Survival Months by Age Group",
    text_auto=".1f"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="age_group_survival"
)
st.write("## Project Conclusion")

st.markdown("""
This project explores breast cancer patient data using Python.
Different charts and visualizations help us understand patient
demographics, tumor characteristics, and survival patterns.

The dashboard makes the dataset easier to explore and understand.
""")
st.write("## Download Dataset")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Breast Cancer Dataset",
    data=csv,
    file_name="Breast_Cancer.csv",
    mime="text/csv"
)
st.markdown("---")
st.markdown(
    "<center>Breast Cancer Data Analysis Dashboard | Created with Python & Streamlit</center>",
    unsafe_allow_html=True
)