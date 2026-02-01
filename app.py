import streamlit as st
import  pickle
import pandas as pd


movies_list=pickle.load(open("movies.pkl","rb"))
                             
similarity=pickle.load(open("similarity.pkl", "rb"))

def recommend(movie):
    movie_index = list(movies_list).index(movie)
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movie = []
    for i in movie_list:
        recommended_movie.append(movies_list[i[0]])

    return recommended_movie




movies_list=movies_list['title'].values

st.set_page_config(page_title="My First App", layout="centered")

st.title("Movie Recommender 👋")
selected_movie_name = st.selectbox(
    '**Search your favourite**',
    (movies_list)
)

if st.button('Recommend'):
    recommendation=recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)
    