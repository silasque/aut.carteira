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
        time.sleep(5)

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
        pyautogui.sleep(10)

        #Close CMD
        pyautogui.hotkey("alt", "f4")

        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", "Automação concluída com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro", f"Falha na automação: {str(e)}")

#Criando Janela

janela = tk.Tk()
janela.title("Automação Carteira")
janela.geometry("200x100")

#Criando botão para Startar Script

botao = tk.Button(janela, text="Start", command=exec_automacao, height=2, width=20)
botao.pack(pady=40)

#Executando a interface Gráfica
janela.mainloop()
