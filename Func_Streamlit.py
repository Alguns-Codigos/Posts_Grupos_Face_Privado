import streamlit.components.v1 as components


def HtmL(ht,tam):
    return components.html(ht,height=tam) # scrolling=True


def Titulo_Programa(texto, text2, text3):
    HtmL(f'''
          <head>
          <link href='https://fonts.googleapis.com/css?family=VT323' rel='stylesheet'>
          </head>
            <font color="white">            
            <div style="border: 3px dashed orange; font-family: 'VT323', monospace; box-shadow:  0 0 0.1em orange;  height: auto; font-weight: bold;  font-size: 50px; width: auto; background-color: #2e2e2e; text-align: center;">
            <span style="font-family: arial; font-size: 10px; font-weight: lighter; width: 100px; color: orange; text-align: left;">{text2}</span>
                <strong> {texto}</strong>
            <span style="color: orange;   font-family: arial; font-weight: lighter; font-size: 10px; width: 100px;  text-align: right;">{text3}</span>
            </div>

            </font>''', 90)  # Altura

def Caixa_Decora_Simples_centro(texto1, COR,Cor2= 'black'):

    div = f'''
    <style>  
        @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    </style>  
    '''
    return HtmL(f'''   
                {div} 
                <div style="font-family: 'Press Start 2P', monospace;color: {Cor2}; border: 2px dashed black; text-align: center; 
                font-size: 13px; background-color: {COR}; height: 13px; padding-top: 5px; border-radius: 5px; ">
                {str(texto1)}</div>  

''', 36)  # Altura

def linha(Cor,Larg):
    HtmL(f'<span style="display: block; background-color: {Cor}; width: 100%; height: {Larg}px; border-bottom: 2px solid black;"></span>'
                    ,14)


def Rodape():
    estilo ="""
   <style>
   .footer {
       display: flex;
       align-items: center;
       justify-content: space-between;
       padding: 20px;
       background-color: #f8f8f8;
       font-size: 14px;
       color: #555555;
       font-family: 'Courier New', monospace;
   }
   .footer .text {
       flex: 1;
       text-align: center;
   }
   .footer .text p {
       margin: 0;
   }
   .footer .text a {
       color: #555555;
       text-decoration: none;
   }
   .footer img {
       width: 80px;
       height: 60px;
       object-fit: cover;
       border-radius: 50%;
   }
   </style>
   """
    # Defina o conteúdo do rodapé
    rodape_html = f"""
    {estilo}
            <div class="footer">
                <div class="text">
                    <p>Site: <a href="algunscodigos.com">algunscodigos.com</a></p>
                    <p>Contato: algunscodigos@gmail.com</p>
                </div>
                <div class="text">
                    <p>Facebook: <a href="https://www.facebook.com/people/Alguns-C%C3%B3digos/100094731667949/">@Alguns-Códigos</a></p>
                    <p>Instagram: <a href="https://www.instagram.com/alguns_codigos.com">@alguns_codigos</a></p>
                </div> 
                <div class="text">
                    <p>Desenvolvido por HELISI-1984:</p>
                    <p>Henrique Liandro Da Silva</p>                
                </div> 
                <div class="text">
                    <img src="https://i.postimg.cc/9FW3JmWK/AMIMA-GIF1.gif" alt="Imagem do Rodapé">
                </div> 
            </div>
        """

    # Exiba o rodapé
    HtmL(rodape_html,100)