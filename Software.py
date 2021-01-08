#Importing necessary modules
from gtts import gTTS
import pygame
from pygame import mixer
from tempfile import TemporaryFile
import serial
import pymysql.cursors
import os
import time

#Database connection
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='robo',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
ser = serial.Serial(port='COM12', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=10)

#Initializing Pygame module
pygame.init()

#Initializing UI
displayWidth = 1200
displayHeight = 600
black = (0,0,0)
white = (255,255,255)
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Robo Hazel')

#Setting clock and images' path
clock = pygame.time.Clock()
currentPath = os.path.dirname(__file__)
eyeFolderPath = os.path.join(currentPath, 'images')
eyeOpened = pygame.image.load(os.path.join(eyeFolderPath, 'opened.png'))
eyeClosed = pygame.image.load(os.path.join(eyeFolderPath,"closed.png"))
isEyeClosed = true

def hazelloop(eyeCurrentImage):
  
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameExit = True
        gameDisplay.fill(white)

        #Eye Blinking
        if (isEyeClosed == true):
            gameDisplay.blit(eyeOpened, (200, 200))
            time.sleep(0.5)
        if (isEyeClosed == false):
            gameDisplay.blit(eyeClosed, (200, 200))
            time.sleep(3)
        if (isEyeClosed == false):
            isEyeClosed = true
        else:
            isEyeClosed = true

        #Reading serial port's data    
        if (ser.isOpen()):
            string=ser.readline().decode('ascii')
            print(string)
            
            #If the data string exists
            if len(string)>0:
              
                #Parsing string
                for i in range(0, len(string)):
                    if string[i] == ':':
                        check = string[i - 1]
                        
                        #If the flag is 'e', fetch the text message from the database and convert it into speech
                        if check == 'e':
                            with connection.cursor() as cursor:
                                # Reading the last text message from the database 
                                sql = "SELECT `message` FROM `robo` ORDER BY 'id' DESC LIMIT 1"
                                cursor.execute(sql)
                                message = str(cursor.fetchone())
                                print(message)
                                serial_message=message[13:len(message) - 2]

                            #Converting the text message into speech and saving it in a file     
                            tts = gTTS(text=serial_message, lang='en-us')
                            mixer.init()
                            sf = TemporaryFile()
                            tts.write_to_fp(sf)
                            sf.seek(0)
                            mixer.music.load(sf)
                            pygame.time.Clock().tick(10)
                          
                        #If the flag is 'w', play the saved audio  
                        elif check == 'w':
                            mixer.music.play()
                            while pygame.mixer.music.get_busy():
                                print("Playing")
                                pygame.time.Clock().tick(10)
                        
        pygame.display.flip()
        clock.tick(120)

hazelloop(eyeCurrentImage)
pygame.quit()
quit()
