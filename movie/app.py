import streamlit as st
from movie_agent import agent

st.set_page_config(page_title=" Movie Recommender", layout="wide")

st.title(" Movie Recommender Buddy")
st.write("Ask me for movies by mood, genre, or vibe!")

query = st.text_input(" What kind of movie are you in the mood for?")

if st.button("Recommend"):
    if query:
        response = agent.run(query)
        st.write("###  Recommendations")
        st.write(response)
    else:
        st.warning("Please enter a query first!")
