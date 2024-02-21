import tkinter as tk
from game import Game
import time
from PIL import ImageTk, Image
import os

#create launcher window, and some cosmetic detail
root = tk.Tk()
root.title("Launcher")
root.configure(bg="black")
root.geometry("500x250")
papyrus_netural = ImageTk.PhotoImage(Image.open("Assets/neutral.png"))

#declaring variables to store values input by user
input_width = tk.IntVar()
input_height = tk.IntVar()
input_seed = tk.IntVar()

#Get the variables and start the game
def startInstance(): 
    papyrus_anger = ImageTk.PhotoImage(Image.open("Assets/the_wrath_of_the_gods.png"))
    papyrus_confused = ImageTk.PhotoImage(Image.open("Assets/confused.png"))

    error_label = tk.Label(root, text = "", fg="red", bg="black", font=("papyrus", 10, "bold"))
    error_label.grid(row=4, column=0)

    #Error handling
    try: #Check for valid integer
        width = input_width.get()
        height = input_height.get()
        seed = input_seed.get()
    except:
        error_label.configure(text="UM. THOSE FIELDS ...\nSHOULD HAVE NUMBERS.")
        papyrus.configure(image=papyrus_confused)
        papyrus.image = papyrus_confused

    if seed == 0:
        seed = int(time.time()) #this will give a different seed every execution unless user can stop time.
    if width <= 1 or height <= 1: #Check for values of 1 or below. a 1x1 maze is too small and 0x0 or any negative value would likely result in error.
        error_label.configure(text="HEY! IS THIS AN INSULT?! \nTHAT'S WAY TOO SMALL!")
        papyrus.configure(image=papyrus_anger)
        papyrus.image = papyrus_anger

    if width >= 2 and height >= 2: #Width and height should be atleast 2 before creating an instance.
        instance = Game(width, height, seed)
        return instance

#Create labels and names for text fields
width_label = tk.Label(root, text = "ENTER WIDTH", fg="white", bg="black", font=("papyrus", 10, "bold"))
width_entry = tk.Entry(root, textvariable= input_width, font=("papyrus", 10, "normal"))

height_label = tk.Label(root, text = "ENTER HEIGHT", fg="white", bg="black", font=("papyrus", 10, "bold"))
height_entry = tk.Entry(root, textvariable= input_height, font=("papyrus", 10, "normal"))

seed_label = tk.Label(root, text = "ENTER SEED \n(OR DON'T! ZERO IS FINE TOO!)", bg="black", fg="white", font=("papyrus", 10, "bold"))
seed_entry = tk.Entry(root, textvariable= input_seed, font=("papyrus", 10, "normal"))

papyrus = tk.Label(root, image=papyrus_netural)

#button to enter values
button = tk.Button(root, text="START!", command= startInstance, font=("papyrus", 10, "bold"))

width_label.grid(row=0,column=0)
width_entry.grid(row=0,column=1)

height_label.grid(row=1,column=0)
height_entry.grid(row=1,column=1)

seed_label.grid(row=2,column=0)
seed_entry.grid(row=2,column=1)

button.grid(row=3,column=1)

papyrus.grid(row=4,column=1)

root.mainloop()

if __name__ == "__main__":
    instance = startInstance()
    instance.run_game_loop()