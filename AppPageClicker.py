import pyautogui as pag
from time import sleep


continueButton = (1499, 977)
countryButton = (913, 716)



def applicationQuestions():
    sleep(5)
    pag.press('tab')
    pag.press('tab')
    sleep(.5)
    pag.press('down')
    pag.press('down')
    pag.press('enter') # 1) yes
    sleep(.5)
    pag.press('tab')
    sleep(.5)
    pag.press('down')
    pag.press('down')
    pag.press('down')
    sleep(.5)
    pag.press('enter') # 2) No
    sleep(.5)
    pag.press('tab')
    sleep(.5)
    pag.press('down')
    pag.press('down')
    pag.press('down')
    sleep(.5)
    pag.press('enter') # 3) No
    sleep(.5)
    pag.press('tab')
    sleep(.5)
    pag.press('down')
    pag.press('down')
    pag.press('down')
    sleep(.5)
    pag.press('enter') # 4) No 
    sleep(.5)
    pag.press('tab')
    sleep(.5)
    pag.press('down')
    pag.press('down')
    pag.press('down')
    sleep(.5)
    pag.press('enter') # 5) No
    sleep(.5)
    pag.press('tab')
    sleep(.5)
    pag.press('down')
    pag.press('down')
    pag.press('down')
    sleep(.5)
    pag.press('enter') # 6) No
    sleep(.5)
    pag.press('tab')
    sleep(.5)
    pag.press('down')
    pag.press('down')
    pag.press('down')
    sleep(.5)
    pag.press('enter') # 7) No
    sleep(.5)
    pag.press('tab')
    sleep(.5)
    pag.press('down')
    pag.press('down')
    pag.press('down')
    sleep(.5)
    pag.press('enter') # 8) No
    sleep(.5)
    pag.press('tab')
    sleep(.5)
    pag.press('down')
    pag.press('down')
    pag.press('down')
    sleep(.5)
    pag.press('enter') # 9) No
    sleep(.5)
    pag.press('tab')
    sleep(.5)
    pag.press('down')
    pag.press('down')
    pag.press('down')
    sleep(.5)
    pag.press('enter') # 10) No
    sleep(.5)
    pag.press('tab')
    pag.press('tab')
    sleep(.5)
    pag.press('down')
    pag.press('down')
    pag.press('down')
    sleep(.5)
    pag.press('enter') # 12) No
    sleep(.5)
    pag.press('tab')
    sleep(.5)
    pag.press('down')
    pag.press('down')
    pag.press('down')
    sleep(.5) 
    pag.press('enter') # 13) No
    sleep(.5)
    pag.press('tab')
    sleep(.5)
    pag.press('down')
    pag.press('down')
    sleep(.5) 
    pag.press('enter') #14) Yes
    sleep(.5)
    pag.press('tab')
    sleep(.5)
    pag.press('down')
    pag.press('down')
    sleep(.5) 
    pag.press('enter') #15) Yes
    pag.scroll(-900)
    pag.moveTo(916,631,2) #trying some different shit here
    pag.click(916, 631)
    pag.moveTo(579, 750,2)
    pag.click(579, 750)
    pag.moveTo(1499, 977, 2)
    pag.click(1499, 977)


applicationQuestions()

print('over')
