import pyperclip
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, InvalidArgumentException
from selenium.webdriver.common.by import By
from  Banco_Dados_Campanha  import ATUAL_USUARIO
from time import sleep
import pyautogui
from datetime import datetime
import random
# velocidade
D = 10
L = 5
N = 3
R = 2

def entrada(driver):
    try:
        resp = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]')
        driver.execute_script("arguments[0].click();", resp)
        return True
    except NoSuchElementException:...

    try:
        resp = driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[2]')
        driver.execute_script("arguments[0].click();", resp)
        return True
    except NoSuchElementException:...
    try:
        resp = driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div')
        driver.execute_script("arguments[0].click();", resp)
        return True
    except NoSuchElementException:...
    try:
        resp = driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[2]')
        driver.execute_script("arguments[0].click();", resp)
        return True
    except NoSuchElementException:...
    try:
        resp = driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[2]')
        driver.execute_script("arguments[0].click();", resp)
        return True
    except NoSuchElementException:...
    try:
        resp = driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[2]')
        driver.execute_script("arguments[0].click();", resp)
        return True
    except NoSuchElementException:...
    try:
        resp = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[2]')
        driver.execute_script("arguments[0].click();", resp)
        return True
    except NoSuchElementException:...

    try:
        resp = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[3]')
        driver.execute_script("arguments[0].click();", resp)
        return True
    except NoSuchElementException:...
    try:
        resp = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[2]')
        driver.execute_script("arguments[0].click();", resp)
        return True
    except NoSuchElementException:...
    try:
        resp = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div')
        driver.execute_script("arguments[0].click();", resp)
        return True
    except NoSuchElementException:...
    try:
        resp = driver.find_element(By.XPATH,
                                   '')
        driver.execute_script("arguments[0].click();", resp)
        return True
    except NoSuchElementException:...

Horas_in = [str(datetime.now())[10:19]]
print('print das start horas', Horas_in)

LISTA = ['PRODUTO', 'TEXTO', 'ARQUIVO', 'NOME_PAGINA', 'LINK_PAGINA']

def Post_Montado_Produto(driver,MIM,TEXTO,ARQUIVO):
    import streamlit as st
    try:
        #st.write( PRODUTO, TEXTO, ARQUIVO, NOME_PAGINA, LINK_PAGINA)

        # Carrega a nova aba
        elemento_aleatorio = random.choice(LISTA)  # Pega um elemento aleatório da lista

        print()
        driver.get(f"{elemento_aleatorio}")
        sleep(N)
        pyautogui.press('space')
        sleep(N)

        # =============================================================_ P O S T A N D O  _=====================================
        try:
            try:#/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div
                if entrada(driver) == True:
                    st.markdown('''-----''')
                    st.write(F'POSTANDO EM : {elemento_aleatorio}')
                    sleep(N)
                    try:
                        Escreve = driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div')

                        pyperclip.copy(TEXTO)
                        sleep(1)
                        pyautogui.hotkey('ctrl', 'v')
                        sleep(R)
                        st.write('Digitou Texto')
                        sleep(R)
                        pyautogui.press('tab')
                        sleep(R)
                        pyautogui.press('tab')
                        sleep(R)
                        pyautogui.press('space')
                        sleep(R)

                        pyperclip.copy(ARQUIVO)
                        pyautogui.hotkey('ctrl', 'v')
                        sleep(R)

                        pyautogui.press('enter')
                        sleep(D)

                        Escreve.submit()
                        st.write(f'Enviou ARQUIVO, Escperar {MIM} Min.')
                        sleep(D)


                        my_bar = st.progress(0)
                        for percent_complete in range(MIM*60):
                            sleep(1)
                            my_bar.progress((percent_complete + 1) / MIM*60)

                    except NoSuchElementException:...

            except StaleElementReferenceException:...

        except NoSuchElementException as e:
            st.write(e)
    except InvalidArgumentException:...


def Cadastro_Grupos(driver,MIM, LOGUIN,TEXTO, ARQUIVO):
    # ========================================================= LIBERAR TODOS GRUPOS========== ===================================

    # Carrega a nova aba
    driver.get(f"https://www.facebook.com/groups/feed/")
    sleep(L)
    pyautogui.press('enter')
    for i in range(1, 20):
        pyautogui.press('tab')

    for i in range(1, 300):
        pyautogui.press('down')

    CONTADOR = 5
    while True:

        try:

            import streamlit as st
            tabela_toda = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div')

            html2 = tabela_toda.get_attribute('outerHTML')
            soup2 = BeautifulSoup(html2, 'html.parser')
            #print(soup2.prettify())


            tag = soup2.find_all('a',
                                 class_='x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1lliihq',
                                 href=True)
            cont = []
            for p,ID in enumerate(tag):
                sleep(.05)

                if 'https://' in str(ID.get('href')):
                    TITULO = str(str(ID.get_text())).split('Última atividade')[0]

                    LISTA.append(str(ID.get('href'))+'buy_sell_discussion')
                    st.write(f'{p} - ',TITULO,ID.get('href'))
                    cont.append(p+1)
            try:
                ATUAL_USUARIO(LOGUIN, 'GRUPOS', cont[-1])
            except IndexError:...
            Post_Montado_Produto(driver,MIM,TEXTO,ARQUIVO )


        except NoSuchElementException as e:
            st.write(e)

        CONTADOR += 1
