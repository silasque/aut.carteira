import pyautogui
import time

# Abrir CMD

pyautogui.hotkey("win", "r") #Abrir o executar
time.sleep(1)
pyautogui.write("cmd")
pyautogui.press("enter")
time.sleep(1)

# Comandos locais CMD
pyautogui.write("ssh bree@172.30.1.38")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("mnb789MNB789")
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("cd docker-django/")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("make up docker-compose up -d")
pyautogui.press("enter")
time.sleep(5)
pyautogui.write("cd ..")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("cd superset/")
pyautogui.press("enter")
pyautogui.sleep(1)
pyautogui.write("docker-compose -f docker-compose-non-dev.yml up")
pyautogui.press("enter")
pyautogui.sleep(10)
pyautogui.hotkey("alt", "f4")

