import pickle
import streamlit as st
import requests





def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances=similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
   
    for i in movie_list:
      
        recommended_movie_names.append(movies.iloc[i[0]].title)
        
    return recommended_movie_names
     

st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names=recommend(selected_movie)
    for i in recommended_movie_names:
        st.write(i)

   
  

