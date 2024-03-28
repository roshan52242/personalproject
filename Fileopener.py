import pyautogui

def openfile(name):
    pyautogui.press('win')
    pyautogui.typewrite(name)
    pyautogui.press("ENTER")