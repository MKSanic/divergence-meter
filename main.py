from pathlib import Path
from PIL import Image
import os
import ctypes
from datetime import datetime
import time
os.chdir(os.path.join(Path(__file__).parent,"pics"))
while(True):
    try:
        start = datetime.now()
        loc = 410 #(1920 - (7*20 + 8*120))/2
        y = 360
        img = Image.open("bg.png")
        pics = []

        
        if(len(str(start.hour)) == 1):
            pics.append("blank")
        for v in str(start.hour):
            pics.append(v)
        pics.append("period")
        if(len(str(start.minute)) == 1):
            pics.append("blank")
        for v in str(start.minute):
            pics.append(v)
        pics.append("period")
        if(len(str(start.second)) == 1):
            pics.append("blank")
        for v in str(start.second):
            pics.append(v)

        for v in pics:
            img.paste(Image.open(f"{v}.png"),(loc,y))
            loc += 20 + 120
        img.save("final.png")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(os.getcwd(),"final.png") , 0)
        time.sleep(0.1)
    except:
        pass

