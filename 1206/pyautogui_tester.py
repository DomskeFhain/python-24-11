import pyautogui
import time

# x = -510 y = 1000
# x - 1300 y 420
# strg + tab 650 655
time.sleep(2)
pyautogui.moveTo(-500, 1000, 0.1,pyautogui.easeInQuad)
pyautogui.dragTo(-1300,420, button="left")
pyautogui.hotkey("command", "c")
pyautogui.keyDown("command")
pyautogui.press("tab")
pyautogui.keyUp("command")
pyautogui.moveTo(-650, 655,0.1, pyautogui.easeInQuad)
pyautogui.click()
pyautogui.hotkey("command", "v")

