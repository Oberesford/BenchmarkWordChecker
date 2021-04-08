import easyocr
import pyautogui
import time
import cv2 
import numpy as np

reader = easyocr.Reader(['en'])
tag = 1
 
while True: 
    def wordcount(filename, listwords):

        file = open(filename, "r")

        read = file.readlines()
        file.close()

        for word in listwords:

            lower = word.lower()
         
            for sentance in read:
                line = sentance.split()

                for each in line:
                    line2 = each.lower()
                    line2 = line2.strip('""')

                    if lower == line2: 
                        

                        time.sleep(1)
                        print(f"\nWord Present:{lower}\n")
                        break
                    else:
                        time.sleep(1)
                        print(f"\nWord Not Present:\n")
                        break
    print("--------------------------------------------------------------------------")
    time.sleep(3)
    image = pyautogui.screenshot(region=(670,400,550,130))
    image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
    tag+=1

    img = cv2.imwrite(f"img/image{tag}.png", image)
    file_name = f"img/image{tag}.png"

    results = reader.readtext(file_name)

    text=""
    for result in results:
        text += result[1] + " "
        text =  text.strip("")


    file_object = open("wordlist.txt", "a")
    text = text.strip(" ")
    file_object.write(f'"{text}"\n')
    file_object.close()

    
    wordcount("wordlist.txt", [text])
    
        

    
    
