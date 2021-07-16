import display


try:
    eInk = display.display()
    eInk.show_image('image.jpg') 

except IOError as e:
    print(e)
    
except KeyboardInterrupt:    
    print("ctrl + c:")
    exit()