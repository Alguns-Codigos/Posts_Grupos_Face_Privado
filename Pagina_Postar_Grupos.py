from WebScraping.Cadastro_Grupo import *
from  Func_Streamlit import *
from Banco_Dados_Campanha import *
import streamlit as st
from time import sleep

COR_MENU = ''
COR_MIDIA = '#00FFFF'
COR_IA = '#FFDEAD'
COR_TEX = '#FF00FF'
COR_EDIC = '#FF8C00'
COR_ENV = '#00FF00'

def Grupos():

    t1, t2 = st.columns([5, 2])
    LOGUIN = t1.text_input('usúario:'.title(),'pontooxigenado@gmail.com')
    SENHA = t2.text_input('senha:'.title(),'@Henriq150784IsaAna')

    ARQUIV = st.text_input('LOCAL PASTA:'.title(), r'G:\Top das Ofertas Online\Arquivos_Midias\2023-07-30 -- Celular Smartphone Note10+ 128GB\Video_Normal.mp4')

    #  =========================================================================== ESCOLHA DO PRODUTO
    t1, t2 = st.columns([5, 2])
    base = '''🛍️ Ofertas Irresistíveis: 
    💰 Preços mais baratos  que na 'Shopee'! 🔥
    🕵️‍♂️Pode Comparar, 🔗links nos posts .\nhttps://bit.ly/topdasofertasonline'''
    TEXTO = t1.text_area('DESCRIÇÃO:'.title(),base, height=300)

    t2.text('Midia')
    #t2.video(ARQUIV)

    t0,t1, t2 = st.columns([0.6,0.3,2])
    t0.text('De quantos em quanto Minutos ->')

    MIM = t1.number_input('',value=1, step=1,label_visibility="collapsed")
    if t2.button('INICIAR CAMPANHA'):
        linha('orange', 3)

        if  LOGUIN != '' and SENHA != '' and TEXTO != '' and ARQUIV != '':
            if ler_SE_USUARIO(LOGUIN) == True:
                esc_USUARIO(LOGUIN ,SENHA ,0)
            else:
                ATUAL_USUARIO(LOGUIN, 'SENHA', SENHA)

            from selenium import webdriver
            from selenium.webdriver.common.by import By
            L = 5
            N = 3
            R = 2

            driver = webdriver.Edge()
            driver.delete_all_cookies()
            driver.set_window_size(1200, 700)
            driver.set_window_position(350, 0)
            driver.get(f"https://www.facebook.com/")
            sleep(R)
            Email = driver.find_element(By.XPATH, '//*[@id="email"]')
            sleep(R)

            Email.send_keys(LOGUIN)
            Usuario = driver.find_element(By.XPATH, '//*[@id="pass"]')
            sleep(N)
            Usuario.send_keys(SENHA)
            sleep(N)
            Usuario.submit()
            sleep(N)
            Cadastro_Grupos(driver,int(MIM), LOGUIN,TEXTO, str(ARQUIV))

