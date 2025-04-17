import tkinter as tk
import threading
import pygame
import time
import random

pygame.init()
pygame.mixer.init()
root = tk.Tk()

lava_chicken = pygame.mixer.Sound("assets\lavaChicken.wav")
chicken_jocky = pygame.mixer.Sound("assets\chicken_jockey.wav")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

def sound_spam():
    lava_chicken.play()
    for i in range(40):
        chicken_jocky.play()
        time.sleep(0.8)

def label_spam():
    for i in range(40):
        top = tk.Toplevel()
        top.geometry(f"300x200+{random.randint(0, screen_width - 300)}+{random.randint(0, screen_height - 200)}")
        top.title("I AM STEVE!!!")
        myMessage = tk.Label(top, text="CHICKEN JOCKEY!!!", font=("Fixedsys", 20))
        myMessage.pack(pady=70)
        time.sleep(0.6)

def runBoth():
    threading.Thread(target=sound_spam, daemon=True).start()
    threading.Thread(target=label_spam, daemon=True).start()

# Run both when GUI starts
runBoth()

# Start the Tkinter loop
root.mainloop()
