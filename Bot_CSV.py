
import pyautogui # ferramenta de automaçao
import pyperclip #permite copiar e colar
import time # envolve tempo, tempo de espera, etc
'''


'''
# baixar a base de dados do sistema

# 1° abrir o navegador (usando teclado)
pyautogui.PAUSE = 1
pyautogui.press('winleft') # aperta a bandeira do windows
pyautogui.write('chrome')#escreve crome
pyautogui.press('enter')
pyautogui.alert("Vai começar, Aperte OK e nao mexa em nada.")
pyautogui.hotkey('ctrl','t') # abre nova aba  ATTALHO
link = 'https://drive.google.com/file/d/1HmQlk7CElqbSdzc6I6tboVyi78JTMoqf/view?usp=sharing'

# 2° Copiar o link do google drive # abrir o drive
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(10)

# 3° Baixar o arquivo do drive
# pegar posição do botao 'download'
pyautogui.click(1223,127, clicks=1) #dowloado
time.sleep(10)
pyautogui.click(1355,8) # fechar navegador
pyautogui.alert("Ok - processo finalizado...")
# print(pyautogui.position()) #pegar posicao do botao dowload

# importando os dados agora, dados em excel


import pandas as pd

# Ler o arquivo xls
df = pd.read_excel(r'C:\Users\usuario\Pictures\Videos Gislene\Saved Pictures\imagens\Downloads\Vendas - Dez.xlsx') #r especifica para o python
display(df) # printa a planilha mais correto 

# calcular o faturamento das vendas
faturamento = df['Valor Final'].sum()

#Somar quantidade vendida 
qtd_prod = df['Quantidade'].sum()

print(f'O faturamento da empresa foi {faturamento}')
print(f'Quantidade vendida foi de {qtd_prod}')


# Enviar o faturamento para o email do patrão 
# 1° abrir o gmail
pyautogui.PAUSE = 1
pyautogui.press('winleft') # aperta a bandeira do windows
pyautogui.write('chrome')#escreve crome
pyautogui.press('enter')
#pyautogui.alert("Vai começar, Aperte OK e nao mexa em nada.")
pyautogui.hotkey('ctrl','t') # abre nova aba  ATTALHO
link = 'https:gmail.com'
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(4)
#print(pyautogui.position()) #pegar posicao do botao dowload x=98, y=205
time.sleep(4)
pyautogui.click(98,205, clicks=1) #Abrir caixa de mensagem

#email a do chefe 
time.sleep(3)
email = 'gustavoguape182@gmail.com'
pyperclip.copy(email)
pyautogui.hotkey('ctrl','v')
time.sleep(3)


#clica assunto
pyautogui.click(910,349, clicks=1) #Clicar no Asssunto
time.sleep(3)
assunto ='Faturamento do dia anterior...'
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl','v')
time.sleep(2)

#converte de int para string e colar msg
fat = str(faturamento)
qtd = str(qtd_prod)
time.sleep(1)
pyautogui.click(852,421, clicks=1) #Clicar no Asssunto
time.sleep(1)
msg1= 'Bom dia \n O faturamento do dia anterior foi de: '
msg2 = '\n \n A quantidade vendidade foi de: '
pyperclip.copy(msg1)
pyautogui.hotkey('ctrl','v')
time.sleep(1)
pyperclip.copy(fat)
pyautogui.hotkey('ctrl','v')
time.sleep(1)
pyperclip.copy(msg2)
pyautogui.hotkey('ctrl','v')
time.sleep(1)
pyperclip.copy(qtd)
pyautogui.hotkey('ctrl','v')
time.sleep(1)
pyautogui.hotkey('ctrl','enter')
time.sleep(1)



pyautogui.alert("E-mail enviado... ") 






