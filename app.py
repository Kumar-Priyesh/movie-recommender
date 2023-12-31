import streamlit as st
import pickle
import requests


movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movie_list = movies['title'].values
st.title("Movie Recommendation System")

selected_movie = st.selectbox('Choose your movie', index=None,options=movie_list, placeholder="Choose an option", disabled=False, label_visibility="visible")

def recommended(movie):
    recommended_movie=[]
    movie_index = []
    index = movies[movies['title']==movie].index[0]
    movie = sorted(list(enumerate(similarity[index])), key= lambda x:x[1], reverse =True)[1:6]
    for i in movie:
        recommended_movie.append(movies.iloc[i[0]].title)
        movie_index.append(movies.iloc[i[0]].movie_id)
    return recommended_movie,movie_index

def fetch_posterPath(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5f4a6bef49cc03f3c78b567862af6bd0'.format(movie_id))
    data= response.json()['poster_path']
    return "https://image.tmdb.org/t/p/w500/"+data


def main():
    if st.button('Recommend'):
        if not selected_movie:
            st.warning("Please select an option.")
        else:
            recommended_movie, movie_index = recommended(selected_movie)
            movie_poster = []

            try:
                for i in range(0, 5):
                    movie_poster.append(fetch_posterPath(movie_index[i]))
            except:
                pass

            st.header(":green[Recommended Movies]",divider='rainbow')
            col = st.columns(5)
            for i in range(0, 5):
                    if (len(movie_poster)==5):
                        with col[i]:
                            st.markdown(recommended_movie[i])
                            st.image(movie_poster[i])
                    else:

                        st.subheader(recommended_movie[i])


if __name__ == "__main__":
    main()
