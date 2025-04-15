import tkinter, tkinter.messagebox
import tkinter.tix
import pygame
import time

pygame.init()
pygame.mixer.init()
root = tkinter.Tk()

lavaChicken = pygame.mixer.Sound("lavaChicken.wav")
chickenJocky = pygame.mixer.Sound("chicken_jockey.wav")
myMessage = tkinter.Label(root, text = "CHICKEN JOCKEY!!!")
myMessage.pack()

def hangLabel(label):
    pass

def soundSpam():
    lavaChicken.play()
    for i in range(40):
        chickenJocky.play()
        time.sleep(0.8)

print(soundSpam())

#Notes: Currently stuck on getting "Chicken Jockey" message to pop up alongside with soundSpam(). Need them to run concurrently with each other!!1

