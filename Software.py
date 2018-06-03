from gtts import gTTS
import pygame
from pygame import mixer
from tempfile import TemporaryFile
import serial
import pymysql.cursors
import os
import time
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='robo',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
ser = serial.Serial(port='COM12', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=10)
pygame.init()

display_width = 1200
display_height = 600
black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Robo Alex')
clock = pygame.time.Clock()
CurrentPath = os.path.dirname(__file__)
eyeFolderPath = os.path.join(CurrentPath, 'images')
m1 = pygame.image.load(os.path.join(eyeFolderPath, 'opened.png'))
#m1 = pygame.image.load(os.path.join("images","opened.png"))
m2 = pygame.image.load(os.path.join(eyeFolderPath,"closed.png"))
eyeCurrentImage = 1

def gameloop(eyeCurrentImage):
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameExit = True
        gameDisplay.fill(white)

        if (eyeCurrentImage == 1):
            gameDisplay.blit(m1, (200, 200))
            time.sleep(0.5)
        if (eyeCurrentImage == 2):
            gameDisplay.blit(m2, (200, 200))
            time.sleep(3)
        if (eyeCurrentImage == 2):
            eyeCurrentImage = 1
        else:
            eyeCurrentImage += 1

        if (ser.isOpen()):
            string=ser.readline().decode('ascii')
            print(string)
            if len(string)>0:
                for i in range(0, len(string)):
                    if string[i] == ':':
                        check = string[i - 1]
                        if check == 'e':
                            with connection.cursor() as cursor:
                                    # Read a single record
                                sql = "SELECT `message` FROM `robo` ORDER BY 'id' DESC LIMIT 1"
                                cursor.execute(sql)
                                message = str(cursor.fetchone())
                                print(message)
                                serial_message=message[13:len(message) - 2]

                            tts = gTTS(text=serial_message, lang='en-us')
                            mixer.init()
                            sf = TemporaryFile()
                            tts.write_to_fp(sf)
                            sf.seek(0)
                            mixer.music.load(sf)
                            pygame.time.Clock().tick(10)
                        if check == 'w':
                            #serial_signal = string[i + 2:len(string)]
                            #if (string[i + 2] == '1' and string[i + 4] == '1' and string[i + 6] == '1'):
                                #print("Announce")
                               #time.sleep(100)
                            mixer.music.play()
                            while pygame.mixer.music.get_busy():
                                print("Playing")
                                pygame.time.Clock().tick(10)
                        #else:
                            #print("Journey")
        pygame.display.flip()
        clock.tick(120)

gameloop(eyeCurrentImage)
pygame.quit()
quit()
