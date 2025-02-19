import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

#Função executar
def exec_automacao():
    try:
        # Abrir CMD
        pyautogui.hotkey("win", "r") #Abrir o executar
        time.sleep(1)
        pyautogui.write("cmd")
        pyautogui.press("enter")
        time.sleep(1)

        # Conectar usuário e senha ssh
        pyautogui.write("ssh bree@172.30.1.38")
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.write("mnb789MNB789")
        pyautogui.press("enter")
        time.sleep(3)

        #Conectando ao Docker
        pyautogui.write("cd docker-django/")
        pyautogui.press("enter")
        time.sleep(1)

        #Startando Container
        pyautogui.write("make up docker-compose up -d")
        pyautogui.press("enter")
        time.sleep(4)

        #Retornando diretório
        pyautogui.write("cd ..")
        pyautogui.press("enter")
        time.sleep(2)

        #Conectando ao Superset
        pyautogui.write("cd superset/")
        pyautogui.press("enter")
        pyautogui.sleep(1)

        #Startando Docker
        pyautogui.write("docker-compose -f docker-compose-non-dev.yml up")
        pyautogui.press("enter")
        pyautogui.sleep(6)

        #Close CMD
        pyautogui.hotkey("alt", "f4")

        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", "Automação concluída com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro", f"Falha na automação: {str(e)}")

#Função Sair do Programa

def sair():
    janela.destroy() #Fechar interface


#Criando Janela

janela = tk.Tk("Automação Carteira")
janela.title("Automação Carteira")
janela.geometry("400x200")

#Criando botão para Startar Script

botao = tk.Button(janela, text="Iniciar", command=exec_automacao, height=2, width=20)
botao_sair = tk.Button(janela, text="Sair", command=sair, height=2, width=20)
botao.pack(pady=20)
botao_sair.pack(pady=10)

#Executando a interface Gráfica
janela.mainloop()
