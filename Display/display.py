import sys
import time
import requests
from PIL import Image
from waveshare_epd import epd7in5_V2


class display():

    def show_image(self, path):
        
        IMAGE_SIZE = (800, 480)
        
        image = Image.open(path)
        #image = image.resize(IMAGE_SIZE)
        image = image.convert("RGB")
        # Create red & black images of the right size
        black_image = Image.new("1", IMAGE_SIZE, 1)
        # Copy pixels into them
        for x in range(IMAGE_SIZE[0]):
            for y in range(IMAGE_SIZE[1]):
                pixel = image.getpixel((x, y))
                if pixel[1] < 100:
                    black_image.putpixel((x, y), 0)

        # Send to the display
        epd = epd7in5_V2.EPD()
        epd.init()

        try:
            epd.display(epd.getbuffer(black_image))
            time.sleep(2)
        finally:
            epd.sleep()