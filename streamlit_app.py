import shutil
import streamlit as st
from Func_Streamlit import *

# streamlit run streamlit_app.py


COR_MENU = ''
COR_MIDIA = '#00FFFF'
COR_IA = '#FFDEAD'
COR_TEX = '#FF00FF'
COR_EDIC = '#FF8C00'
COR_ENV = '#00FF00'

def main():
    Titulo_Programa('.   POSTS AUTOMATICO GRUPOS     .','Alguns Códigos','HELISI-1984')


    from Pagina_Postar_Grupos import Grupos

    Grupos()
    linha('blue', 3)

    Rodape()


if __name__ == '__main__':

    st.set_page_config(layout="wide")
    main()
