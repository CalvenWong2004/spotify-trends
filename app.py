import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_icon="spotify.jpg", page_title="Spotify Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned-blue.csv")

df = load_data()

st.title("Spotify Analysis")
st.markdown("This is a mini project that shows the Spotify stream trends of my own playlist - blue")\

st.sidebar.header("Select your music")

selected_cat = st.sidebar.multiselect(
    "Select your desired genres:",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

filter_df = df[df["Category"].isin(selected_cat)]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distributions of Genres")
    cat_counts = filter_df['Category'].value_counts().reset_index()
    cat_counts.columns = ["Category", "Counts"]

    fig_bar = px.bar(cat_counts, x="Category", y="Counts", color= "Category")
    st.plotly_chart(fig_bar, width="stretch")

with col2:
    st.subheader("Danceability vs Energy")
    fig_scat = px.scatter(
        filter_df,
        x="Danceability",
        y="Energy",
        color="Category",
        hover_data = ["Track Name", "Artist Name(s)"]
    )
    st.plotly_chart(fig_scat, use_container_width=True)

st.subheader("Raw Data Exploratory")
st.dataframe(filter_df[["Track Name", "Artist Name(s)", "Category", "Popularity"]])