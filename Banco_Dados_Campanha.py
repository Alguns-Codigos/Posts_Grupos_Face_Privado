import sqlite3
import datetime

data_atual = datetime.date.today()
data_formatada = data_atual.strftime("%d/%m/%Y")

dbase = sqlite3.connect('Dados_Campanha.db',check_same_thread=False)
c = dbase.cursor()


# --------_  USUARIO
dbase.execute('''CREATE TABLE IF NOT EXISTS USUARIO( 
                DATA TEXT NOT NULL,
                LOGUIN TEXT NOT NULL,
                SENHA TEXT NOT NULL,
                GRUPOS INTEGER NOT NULL             
)''')


# =======================================_ USUARIO
def esc_USUARIO(LOGUIN ,SENHA ,GRUPOS):
    DATA = data_formatada
    c.execute('''INSERT INTO USUARIO (DATA ,LOGUIN ,SENHA ,GRUPOS)
                VALUES (?,?,?,?)''',
              (DATA ,LOGUIN ,SENHA ,GRUPOS))
    dbase.commit()

def ler_SE_USUARIO(LOGUIN):
    c.execute("SELECT * FROM USUARIO WHERE LOGUIN = ? ", (LOGUIN,))
    result = c.fetchall()
    if result == []:
        return True
    else:
        return False

def ler_USUARIO(ID=''):
    if ID !='':
        c.execute("SELECT * FROM USUARIO WHERE ID = ?", (ID,))
        result = c.fetchall()
        return result
    else:
        c.execute("SELECT * FROM USUARIO")
        result = c.fetchall()
        return result

def ler_USUARIO_NOME(NOME):
    if NOME !='':
        c.execute("SELECT * FROM USUARIO WHERE NOME = ?", (NOME,))
        result = c.fetchall()
        return result

def ATUAL_USUARIO(LOGUIN,COLUNA,TEXTO):
    query = f'''
    UPDATE USUARIO
    SET {COLUNA} = ?
    WHERE LOGUIN = ?
    '''
    c.execute(query, (TEXTO,LOGUIN))
    dbase.commit()



