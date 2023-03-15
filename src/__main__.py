import pyautogui
import cv2
import time
import os
import keyboard

width, height = pyautogui.size()
ImagesPath = os.path.join(os.path.abspath(os.curdir), 'src\\images\\')

def clickCenterButton(imageRoute, region, grayscale, confidence):
    centerPosition = pyautogui.locateCenterOnScreen(imageRoute, region = region, grayscale = grayscale, confidence = confidence)
    if centerPosition is not None:
        pyautogui.moveTo(centerPosition)
        time.sleep(0.1)
        pyautogui.leftClick()
        return True
    return False

def pressKeyIFFound(imageRoute, region, grayscale, confidence, key):
    centerPosition = pyautogui.locateCenterOnScreen(imageRoute, region = region, grayscale = grayscale, confidence = confidence)
    if centerPosition is not None:
        pyautogui.press(key)
        time.sleep(0.1)
        return True
    return False

def main():
    
    time.sleep(5)

    while not keyboard.is_pressed('q'):

        pyautogui.moveRel(100, -100)

        #Character Selection Button
        clickCenterButton(f'{ImagesPath}1-select-character-button.JPG', (0, 0, width, height), False, 0.8)

        #New Button
        if clickCenterButton(f'{ImagesPath}2-new-button.JPG', (0, 0, width, height), False, 0.9):
            time.sleep(0.8)

        #Missions Button
        clickCenterButton(f'{ImagesPath}3-missions-button.JPG', (0, 0, width, height), False, 0.9)
        
        #Olympus Button
        clickCenterButton(f'{ImagesPath}4-olympus-button.JPG', (0, 0, width, height), False, 0.9)
        
        #Tutorial Node Button
        if clickCenterButton(f'{ImagesPath}5-tutorial-node-button.JPG', (0, 0, width, height), False, 0.9):
            time.sleep(0.8)
        
        #Hard Button
        clickCenterButton(f'{ImagesPath}6-hard-button.JPG', (0, 0, width, height), False, 0.98)
        
        #Hardcore Button
        clickCenterButton(f'{ImagesPath}7-hardcore-button.JPG', (0, 0, width, height), False, 0.9)
        
        #Claim Prospect Button
        clickCenterButton(f'{ImagesPath}8-claim-prospect-button.JPG', (0, 0, width, height), False, 0.9)
        
        #Confirm loadout Button
        clickCenterButton(f'{ImagesPath}9-confirm-loadout-button.JPG', (0, 0, width, height), False, 0.9)
        
        #Yes Confirm loadout Button
        clickCenterButton(f'{ImagesPath}10-yes-confirm-loadout-button.JPG', (0, 0, width, height), False, 0.9)
        
        #Mission Panel
        pressKeyIFFound(f'{ImagesPath}11-mission-panel.JPG', (0, 0, width, height), False, 0.9, "f")

        #Return Station Button
        clickCenterButton(f'{ImagesPath}12-return-station-button.JPG', (0, 0, width, height), False, 0.8)

        #Yes Return Station Button
        clickCenterButton(f'{ImagesPath}13-yes-return-station-button.JPG', (0, 0, width, height), False, 0.9)

        time.sleep(0.1)




if __name__ == '__main__':
    main()