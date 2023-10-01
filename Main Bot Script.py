from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.locateOnScreen('topright.png', region=(1500,350,100,100), grayscale=True, confidence=0.7) != None:
        click(1545,398)
        time.sleep(2)

    if pyautogui.locateOnScreen('tstart.png', region=(1020, 1020, 125, 50), grayscale=True, confidence=0.7) is not None:
        click(1078, 1048)
        time.sleep(5)

    # Initialize a timer for pixel checking
    pixel_check_start_time = time.time()

    # Loop for up to 60 seconds for pixel checking
    while time.time() - pixel_check_start_time < 60:
        if pyautogui.pixel(850, 595)[2] == 7:#1
            click(850, 595)

        if pyautogui.pixel(944, 570)[2] == 7:
            click(944, 570)

        if pyautogui.pixel(1036, 601)[2] == 7:
            click(1036, 601)

        if pyautogui.pixel(1129, 590)[2] == 7:
            click(1129, 590)

        if pyautogui.pixel(1224, 589)[2] == 7:#5
            click(1224, 589)

        if pyautogui.pixel(849, 745)[2] == 7:
            click(849, 745)

        if pyautogui.pixel(944, 725)[2] == 7:
            click(944, 725)

        if pyautogui.pixel(1036, 739)[2] == 7:
            click(1036, 739)

        if pyautogui.pixel(1129, 745)[2] == 7:
            click(1129, 745)

        if pyautogui.pixel(1224, 731)[2] == 7:#10
            click(1224, 731)

        if pyautogui.pixel(849, 905)[2] == 7:
            click(849, 905)

        if pyautogui.pixel(943, 877)[2] == 7:
            click(943, 877)
            
        if pyautogui.pixel(1036, 894)[2] == 7:
            click(1036, 894)

        if pyautogui.pixel(1130, 902)[2] == 7:
            click(1130, 902)

        if pyautogui.pixel(1224, 878)[2] == 7:#15
            click(1224, 878)

        
    if pyautogui.locateOnScreen('end.png', region=(750,1025,95,95), grayscale=True, confidence=0.7) != None:
        click(798,1055)
        time.sleep(310)











        




  
