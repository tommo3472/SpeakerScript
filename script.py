from time import *
from pyautogui import *

"""
    Check out https://pyautogui.readthedocs.io/en/latest/index.html
    for the pyautogui api

"""

def move_to_click(img, b):
    sleep(2) # sleep to wait for the window to load.
    
    x, y = locateCenterOnScreen(img, confidence=0.7)
    click(x, y, button=b)
    

def click_enchancement(img):


    # offset to click in the box.
    x, y, w, h = locateOnScreen(img)
    click(10-x, 5+y, button='left')


def main():
    
    move_to_click('soundIcon.png', 'right')
    move_to_click('openSound.png', 'left')
    move_to_click('soundControlPanel.png', 'left')
    move_to_click('speakerOption.png', 'left')
    move_to_click('properties.png', 'left')
    move_to_click('enchancements.png', 'left')
    click_enchancement('loudnessClicked.png')
        


if __name__ == "__main__":
    main()




        
