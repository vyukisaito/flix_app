import requests
import streamlit as st
from login.service import logout


class GenreRepository:

    def __init__(self):
        self.__base_url = 'https://yuks.pythonanywhere.com/api/v1/'
        self.__genres_url = f'{self.__base_url}genres/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_genres(self):
        response = requests.get(
            self.__genres_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:  # caso a sessão do token expirou
            logout()  # vamos criar um sistema de logout
            return None
        raise Exception(f'Erro ao obter dadso da API. Status code: {response.status_code}')

    def create_genre(self, genre):  # o genre vai ser do service
        response = requests.post(
            self.__genres_url,
            headers=self.__headers,
            data=genre
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dadso da API. Status code: {response.status_code}')
