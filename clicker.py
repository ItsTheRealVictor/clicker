import pyautogui as pag
from time import sleep

sleep(5)

continueButton = (1499, 977)
countryButton = (913, 716)


# First page: Autofill with Resume
def firstPage():
    pag.click(continueButton)
# firstPage()

# #second page: My information
def myInformation():
    pag.click(countryButton)
    pag.press('enter')
    sleep(1)
    pag.press('tab')
    sleep(.5)
    pag.press('tab')
    sleep(.5)
    pag.press('tab')
    sleep(.5)
    pag.write('12420 NW Barnes Rd # 255')
    pag.press('tab')
    pag.write('Portland')
    pag.press('tab')
    pag.write('OR')
    sleep(1)
    pag.press('tab')
    pag.write('97229')

# myInformation()

#Page 3: My Experience
def myExperience():

    jobTitleButton = (853,834)
    pag.click(jobTitleButton)
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.write('052021')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.write('music')
    pag.press('enter')
    sleep(.5)
    pag.press('enter')
    sleep(.5)
    pag.press('enter')
    sleep(2)
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.write('electrical engineering')
    pag.press('enter')
    sleep(.5)
    pag.press('enter')
    sleep(.5)
    pag.press('enter')
    sleep(2)
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.write('electrical engineering')
    pag.press('enter')
    sleep(.5)
    pag.press('enter')
    sleep(.5)
    pag.press('enter')
    sleep(2)

# myExperience()

#page 4: application questions
def applicationQuestions():
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
    sleep(.5)
    pag.press('tab')
    sleep(.5)
    pag.press('down')
    pag.press('down')
    pag.press('down')
    sleep(.5) 
    pag.press('enter') #16) No

     
# applicationQuestions()

listOfFunctions = [firstPage(), myInformation(), myExperience(), applicationQuestions()]

for function in listOfFunctions:
    while True:
        confirm = input("Continue to next page? y/n")
        if confirm == 'y':
            function    
            pag.click(continueButton)
        elif confirm == 'n':
            print("Ok. We'll wait")


    
