import tkinter as tk
import threading
import pygame
import time
import random
import os, sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

pygame.init()
pygame.mixer.init()
root = tk.Tk()

lava_chicken = pygame.mixer.Sound(resource_path("assets/lava_chicken.wav"))
chicken_jocky = pygame.mixer.Sound(resource_path("assets/chicken_jockey.wav"))
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

def lava_chicken_spam():
    lava_Chicken_duration = lava_chicken.get_length()
    lava_chicken.play()
    time.sleep(lava_Chicken_duration - 1)
    root.quit()

def chicken_jockey_spam():
    for i in range(50):
        chicken_jocky.play()
        time.sleep(0.8)

def label_spam():
    for i in range(50):
        top = tk.Toplevel()
        top.geometry(f"300x200+{random.randint(0, screen_width - 300)}+{random.randint(0, screen_height - 200)}")
        top.title("I AM STEVE!!!")
        myMessage = tk.Label(top, text="CHICKEN JOCKEY!!!", font=("Fixedsys", 20))
        myMessage.pack(pady=70)
        time.sleep(0.8)

def run_all():
    threading.Thread(target = lava_chicken_spam, daemon = True).start()
    threading.Thread(target = chicken_jockey_spam, daemon = True).start()
    threading.Thread(target = label_spam, daemon = True).start()

run_all()

root.mainloop()
