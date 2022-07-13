from pathlib import Path
from PIL import Image
import os
import ctypes
from datetime import datetime
import time


def update_pics(pics: list, numbers: int, zero_fill=2):
    for number in str(numbers).zfill(zero_fill):
        pics.append(number)


def play_clock():
    os.chdir(os.path.join(Path(__file__).parent))

    loc_y = 360
    while True:
        try:
            start = datetime.now()
            loc_x = 410  # (1920 - (7*20 + 8*120))/2
            img = Image.open("pics/bg.png")
            pics = []

            update_pics(pics=pics, numbers=start.hour)
            pics.append("period")
            update_pics(pics=pics, numbers=start.minute)
            pics.append("period")
            update_pics(pics=pics, numbers=start.second)

            for v in pics:
                img.paste(Image.open(f"pics/{v}.png"), (loc_x, loc_y))
                loc_x += 20 + 120

            img.save("pics/final.png")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(os.getcwd(), "pics/final.png"), 0)
            time.sleep(0.1)
        except OSError:
            pass


if __name__ == "__main__":
    play_clock()