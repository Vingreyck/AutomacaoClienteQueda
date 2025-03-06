import pyautogui as bot
import numpy as np
import cv2
import pytesseract
import pyperclip

bot.sleep (5)

bot.PAUSE = 0.8

# Configuração dos limites de cor verde (ajuste se necessário)
lower_green = np.array([50, 100, 100])  # Limite inferior (HSV)
upper_green = np.array([70, 255, 255])  # Limite superior (HSV)

def procurar_boneco_verde():
    # Captura a tela
    screenshot = bot.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Converte a imagem para HSV
    hsv_image = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)

    # Cria a máscara para o verde
    mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # Encontra os contornos
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    bonecos = []
    for contour in contours:
        if cv2.contourArea(contour) > 100:  # Filtra áreas muito pequenas
            x, y, w, h = cv2.boundingRect(contour)
            bonecos.append((x, y, w, h))
    return bonecos

def verificar_nome_proximo(x, y, w, h, nome_copiado):
    # Configurar o caminho do Tesseract manualmente
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # Captura a área ao redor do boneco
    screenshot = bot.screenshot(region=(x, y, w, h + 50))  # Inclui área abaixo
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Realiza OCR para extrair o texto
    texto_extraido = pytesseract.image_to_string(screenshot, lang='eng')

    # Verifica se o nome copiado está no texto extraído
    return nome_copiado.strip().lower() in texto_extraido.strip().lower()

# Loop principal
repeticoes = 1
for _ in range(repeticoes):
    bot.click(x=248, y=564, clicks=3)# 1
    bot.hotkey('ctrl', 'c')  # Copia o nome
    bot.hotkey('alt', 'tab')
    bot.hotkey('ctrl', 'v')
    bot.press('tab')
    bot.hotkey('alt', 'tab')
    bot.click(x=169, y=26)#IXC
    bot.click(x=1025, y=156)#barra de pesquisa
    bot.hotkey('ctrl', 'v')
    bot.sleep(2)
    nome_copiado = pyperclip.paste()  # Obtém o nome copiado
    bonecos = procurar_boneco_verde()
    for x, y, w, h in bonecos:
        if verificar_nome_proximo(x, y, w, h, nome_copiado):
            # Se o nome corresponde, clica no boneco
            bot.click(x + w // 2, y + h // 2)
            print("DASLKDJALSDJNLAWJNDKANHICKXBZJKINSKDNFBIWEDKASMLKCMLSMLFEIONLJSNLCMLCSIBNEKFJNCLXKJDNVKNSLEFKNIJNCLXKMLKDNVLIXNFEKLJS")
            break
        
    
    bot.sleep (2)
    bot.click(x=301, y=228)#editar
    bot.sleep (2)
    bot.click(x=301, y=228)#editar
    bot.click(x=453, y=264)#contato
    bot.click(x=707, y=453, clicks=3)#telefone
    bot.hotkey('ctrl', 'c')
    bot.hotkey('alt', 'tab')
    bot.hotkey('ctrl', 'v')
    bot.press('enter')
    bot.hotkey('alt', 'tab')
    bot.click(x=1887, y=177)#fechar
    bot.click(x=16, y=19)#grafico/site


    bot.click(x=297, y=615, clicks=3)#2
    bot.hotkey('ctrl', 'c')  # Copia o nome
    bot.hotkey('alt', 'tab')
    bot.hotkey('ctrl', 'v')
    bot.press('tab')
    bot.hotkey('alt', 'tab')
    bot.click(x=169, y=26)#IXC
    bot.click(x=1025, y=156)#barra de pesquisa
    bot.hotkey('ctrl', 'v')
    bot.sleep(2)
    nome_copiado = pyperclip.paste()  # Obtém o nome copiado
    bonecos = procurar_boneco_verde()
    for x, y, w, h in bonecos:
        if verificar_nome_proximo(x, y, w, h, nome_copiado):
            # Se o nome corresponde, clica no boneco
            bot.click(x + w // 2, y + h // 2)
            break
    
    bot.sleep (2)
    bot.click(x=301, y=228)#editar
    bot.sleep (2)
    bot.click(x=301, y=228)#editar
    bot.click(x=453, y=264)#contato
    bot.click(x=707, y=453, clicks=3)#telefone
    bot.hotkey('ctrl', 'c')
    bot.hotkey('alt', 'tab')
    bot.hotkey('ctrl', 'v')
    bot.press('enter')
    bot.hotkey('alt', 'tab')
    bot.click(x=1887, y=177)#fechar
    bot.click(x=16, y=19)#grafico/site

    bot.click(x=271, y=651, clicks=3)#3
    bot.hotkey('ctrl', 'c')  # Copia o nome
    bot.hotkey('alt', 'tab')
    bot.hotkey('ctrl', 'v')
    bot.press('tab')
    bot.hotkey('alt', 'tab')
    bot.click(x=169, y=26)#IXC
    bot.click(x=1025, y=156)#barra de pesquisa
    bot.hotkey('ctrl', 'v')
    bot.sleep(2)
    nome_copiado = pyperclip.paste()  # Obtém o nome copiado
    bonecos = procurar_boneco_verde()
    for x, y, w, h in bonecos:
        if verificar_nome_proximo(x, y, w, h, nome_copiado):
            # Se o nome corresponde, clica no boneco
            bot.click(x + w // 2, y + h // 2)
            break
    
    bot.sleep (2)
    bot.click(x=301, y=228)#editar
    bot.sleep (2)
    bot.click(x=301, y=228)#editar
    bot.click(x=453, y=264)#contato
    bot.click(x=707, y=453, clicks=3)#telefone
    bot.hotkey('ctrl', 'c')
    bot.hotkey('alt', 'tab')
    bot.hotkey('ctrl', 'v')
    bot.press('enter')
    bot.hotkey('alt', 'tab')
    bot.click(x=1887, y=177)#fechar
    bot.click(x=16, y=19)#grafico/site


    bot.click(x=299, y=703, clicks=3)#4
    bot.hotkey('ctrl', 'c')  # Copia o nome
    bot.hotkey('alt', 'tab')
    bot.hotkey('ctrl', 'v')
    bot.press('tab')
    bot.hotkey('alt', 'tab')
    bot.click(x=169, y=26)#IXC
    bot.click(x=1025, y=156)#barra de pesquisa
    bot.hotkey('ctrl', 'v')
    bot.sleep(2)
    nome_copiado = pyperclip.paste()  # Obtém o nome copiado
    bonecos = procurar_boneco_verde()
    for x, y, w, h in bonecos:
        if verificar_nome_proximo(x, y, w, h, nome_copiado):
            # Se o nome corresponde, clica no boneco
            bot.click(x + w // 2, y + h // 2)
            break
    
    bot.sleep (2)
    bot.click(x=301, y=228)#editar
    bot.sleep (2)
    bot.click(x=301, y=228)#editar
    bot.click(x=453, y=264)#contato
    bot.click(x=707, y=453, clicks=3)#telefone
    bot.hotkey('ctrl', 'c')
    bot.hotkey('alt', 'tab')
    bot.hotkey('ctrl', 'v')
    bot.press('enter')
    bot.hotkey('alt', 'tab')
    bot.click(x=1887, y=177)#fechar
    bot.click(x=16, y=19)#grafico/site


    bot.click(x=279, y=753, clicks=3)#5
    bot.hotkey('ctrl', 'c')  # Copia o nome
    bot.hotkey('alt', 'tab')
    bot.hotkey('ctrl', 'v')
    bot.press('tab')
    bot.hotkey('alt', 'tab')
    bot.click(x=169, y=26)#IXC
    bot.click(x=1025, y=156)#barra de pesquisa
    bot.hotkey('ctrl', 'v')
    bot.sleep(2)
    nome_copiado = pyperclip.paste()  # Obtém o nome copiado
    bonecos = procurar_boneco_verde()
    for x, y, w, h in bonecos:
        if verificar_nome_proximo(x, y, w, h, nome_copiado):
            # Se o nome corresponde, clica no boneco
            bot.click(x + w // 2, y + h // 2)
            break
    
    bot.sleep (2)
    bot.click(x=301, y=228)#editar
    bot.sleep (2)
    bot.click(x=301, y=228)#editar
    bot.click(x=453, y=264)#contato
    bot.click(x=707, y=453, clicks=3)#telefone
    bot.hotkey('ctrl', 'c')
    bot.hotkey('alt', 'tab')
    bot.hotkey('ctrl', 'v')
    bot.press('enter')
    bot.hotkey('alt', 'tab')
    bot.click(x=1887, y=177)#fechar
    bot.click(x=16, y=19)#grafico/site
'''
    bot.click(x=216, y=796, clicks=3)#6
    bot.hotkey('ctrl', 'c')  # Copia o nome
    bot.hotkey('alt', 'tab')
    bot.hotkey('ctrl', 'v')
    bot.press('tab')
    bot.hotkey('alt', 'tab')
    bot.click(x=169, y=26)#IXC
    bot.click(x=1025, y=156)#barra de pesquisa
    bot.hotkey('ctrl', 'v')
    bot.sleep(2)
    nome_copiado = pyperclip.paste()  # Obtém o nome copiado
    bonecos = procurar_boneco_verde()
    for x, y, w, h in bonecos:
        if verificar_nome_proximo(x, y, w, h, nome_copiado):
            # Se o nome corresponde, clica no boneco
            bot.click(x + w // 2, y + h // 2)
            break
    
    bot.sleep (2)
    bot.click(x=301, y=228)#editar
    bot.sleep (2)
    bot.click(x=301, y=228)#editar
    bot.click(x=453, y=264)#contato
    bot.click(x=707, y=453, clicks=3)#telefone
    bot.hotkey('ctrl', 'c')
    bot.hotkey('alt', 'tab')
    bot.hotkey('ctrl', 'v')
    bot.press('enter')
    bot.hotkey('alt', 'tab')
    bot.click(x=1887, y=177)#fechar
    bot.click(x=16, y=19)#grafico/site


    bot.click(x=240, y=841, clicks=3)#7
    bot.hotkey('ctrl', 'c')  # Copia o nome
    bot.hotkey('alt', 'tab')
    bot.hotkey('ctrl', 'v')
    bot.press('tab')
    bot.hotkey('alt', 'tab')
    bot.click(x=169, y=26)#IXC
    bot.click(x=1025, y=156)#barra de pesquisa
    bot.hotkey('ctrl', 'v')
    bot.sleep(2)
    nome_copiado = pyperclip.paste()  # Obtém o nome copiado
    bonecos = procurar_boneco_verde()
    for x, y, w, h in bonecos:
        if verificar_nome_proximo(x, y, w, h, nome_copiado):
            # Se o nome corresponde, clica no boneco
            bot.click(x + w // 2, y + h // 2)
            break
    
    bot.sleep (2)
    bot.click(x=301, y=228)#editar
    bot.sleep (2)
    bot.click(x=301, y=228)#editar
    bot.click(x=453, y=264)#contato
    bot.click(x=707, y=453, clicks=3)#telefone
    bot.hotkey('ctrl', 'c')
    bot.hotkey('alt', 'tab')
    bot.hotkey('ctrl', 'v')
    bot.press('enter')
    bot.hotkey('alt', 'tab')
    bot.click(x=1887, y=177)#fechar
    bot.click(x=16, y=19)#grafico/site


    bot.click(x=191, y=888, clicks=3)#8
    bot.hotkey('ctrl', 'c')  # Copia o nome
    bot.hotkey('alt', 'tab')
    bot.hotkey('ctrl', 'v')
    bot.press('tab')
    bot.hotkey('alt', 'tab')
    bot.click(x=169, y=26)#IXC
    bot.click(x=1025, y=156)#barra de pesquisa
    bot.hotkey('ctrl', 'v')
    bot.sleep(2)
    nome_copiado = pyperclip.paste()  # Obtém o nome copiado
    bonecos = procurar_boneco_verde()
    for x, y, w, h in bonecos:
        if verificar_nome_proximo(x, y, w, h, nome_copiado):
            # Se o nome corresponde, clica no boneco
            bot.click(x + w // 2, y + h // 2)
            break
    
    bot.sleep (2)
    bot.click(x=301, y=228)#editar
    bot.sleep (2)
    bot.click(x=301, y=228)#editar
    bot.click(x=453, y=264)#contato
    bot.click(x=707, y=453, clicks=3)#telefone
    bot.hotkey('ctrl', 'c')
    bot.hotkey('alt', 'tab')
    bot.hotkey('ctrl', 'v')
    bot.press('enter')
    bot.hotkey('alt', 'tab')
    bot.click(x=1887, y=177)#fechar
    bot.click(x=16, y=19)#grafico/site
    bot.click(x=987, y=996)#seta pular
'''
#bot.click(x=169, y=26)#IXC
#bot.click(x=1025, y=156)#barra de pesquisa
#bot.click(x=301, y=230)#editar
#bot.click(x=453, y=264)#contato
#bot.click(x=707, y=453)#telefone
#ot.click(x=1887, y=177)#fechar
#bot.click(x=16, y=19)#grafico/site
#bot.click(x=987, y=996)#seta pular
