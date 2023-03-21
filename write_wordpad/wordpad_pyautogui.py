import os
import pyautogui as pe
import time
import subprocess

def open_app(path):
    os.startfile(path)

def wait(seconds):
    time.sleep(seconds)

def find_pointer_position():
    return pe.position()

def write(text):
    pe.typewrite(text, .1)

def move_and_click(x, y, timeout):
    pe.moveTo(x, y, timeout)
    pe.click(x, y)

def key_press(key):
    pe.press(key)

def hotkey_press(cond, key):
    pe.hotkey(cond, key)

def click_by_image(img):
    pe.click(pe.locateCenterOnScreen(img))

def usign_wordpad():
    path = 'C:/Program Files/Windows NT/Accessories/WordPad.exe'
    open_app(path)
    wait(1)
    move_and_click(167, 200, 1)
    wait(.5)
    write("This is an ")
    hotkey_press('ctrl', 'I')
    write("automated test ")
    move_and_click(210, 200, 1)
    write("with python!")
    hotkey_press('ctrl', 'B')
    key_press('enter')
    wait(.5)
    write('And this is some ')
    hotkey_press('ctrl', 'U')
    write('regular')
    hotkey_press('ctrl', 'U')
    write(' text.')

def using_calc():
    path = 'C:/Windows/System32/calc.exe'
    open_app(path)
    wait(1)

usign_wordpad()

# os.startfile('C:/Program Files/Windows NT/Accessories/WordPad.exe')
# time.sleep(1)
# print(pe.position())
# pe.moveTo(167,146,2)
# pe.click(167,146)
# time.sleep(.5)
# pe.typewrite("This is an automated test", .1)




# os.startfile('C:/Program Files/Windows NT/Accessories/WordPad.exe'),time.sleep(1),pe.moveTo(268,70,1),pe.click(268,70),time.sleep(0.1),pe.typewrite('24'),time.sleep(1),pe.press('enter'),pe.hotkey('ctrl','B'),pe.typewrite('Hi!!',0.1),time.sleep(2),pe.typewrite('  I am an AutoBot programmed by Adams Tech Guide :)',0.1),time.sleep(1),pe.press('enter'),time.sleep(0.1),pe.typewrite('My task is to help you make a bootable USB Flashdrive for Windows OS.',0.1),time.sleep(1),pe.press('enter'),pe.typewrite('So, Sit back relax and let me do the needful for you.',0.1),time.sleep(1),pe.press('enter'),pe.typewrite('INITIALIZING in 5 seconds',0.1),pe.press('enter'),pe.typewrite,pe.typewrite('.....',1),time.sleep(0.1),pe.hotkey('alt','f4'),pe.press('tab'),time.sleep(0.1),pe.press('enter'),time.sleep(3)

# os.startfile('C:/Users/Adams Tech Guide/Desktop/WiNToBootic.exe')

# time.sleep(1),pe.hotkey('alt','tab'),time.sleep(0.1),pe.hotkey('alt','tab'),time.sleep(0.1),pe.click(766,580),time.sleep(1),pe.moveTo(1088,499,1),pe.click(1088,499),time.sleep(2)

# pe.click(1202,544,1),time.sleep(0.3),pe.typewrite("C:\\Users\\Adams Tech Guide\\Desktop"),time.sleep(2),pe.press('enter'),time.sleep(2),pe.press('tab'),time.sleep(0.2),pe.press('tab'),time.sleep(0.2),pe.press('tab'),time.sleep(0.2),pe.press('tab'),time.sleep(0.2),pe.press('tab'),time.sleep(0.2),pe.press('tab'),time.sleep(0.2),pe.press('tab')

# pe.typewrite('Microsoft Windows 10 Pro x64BiT'),time.sleep(0.1),pe.press('enter'),time.sleep(3),pe.moveTo(964,633,1),pe.click(964,633,1),time.sleep(2),pe.moveTo(932,596,1),pe.click(932,596),time.sleep(1),pe.moveTo(1001,599,1),pe.click(1001,599)