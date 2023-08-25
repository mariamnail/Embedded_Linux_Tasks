import pyautogui,time
 
pyautogui.hotkey('win')
time.sleep(1)
pyautogui.typewrite('code')
pyautogui.press('enter')
time.sleep(5)

def install_ex(ex_name):
    pyautogui.hotkey('ctrl', 'shift', 'x')
    time.sleep(2)
    pyautogui.typewrite(ex_name)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(10)
 
install_ex('clangd')
install_ex('c++ testmate')
install_ex('c++ helper')
install_ex('cmake')
install_ex('cmake tools')    
