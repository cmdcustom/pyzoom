import os, pyautogui
userp = os.environ['USERPROFILE']
zoomdriver = userp + r"\AppData\Roaming\Zoom\bin\Zoom.exe"

def Allowed(): #check if let in meeting
  if (pyautogui.locateOnScreen('prtc.png') is not None):
    commandres = "acep"
    return commandres
  elif (pyautogui.locateOnScreen('prtc.png') is None):
    commandres = "not yet"
    return commandres
  
 
     
  
 
  
