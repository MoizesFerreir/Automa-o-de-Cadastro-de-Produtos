import pyautogui
from time import sleep

pyautogui.click(678,386,duration=2)
pyautogui.write('Moizes')

pyautogui.click(681,407,duration=2)
pyautogui.write('123456')

pyautogui.click(584,441,duration=2)

with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        pyautogui.click(420,371,duration=1)
        pyautogui.write(produto)

        pyautogui.click(420,394,duration=1)
        pyautogui.write(quantidade)
        pyautogui.click(425,426,duration=1)
        pyautogui.write(preco)

        pyautogui.click(326,581,duration=1)
        sleep(1)