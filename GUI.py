#Import Packages

from tkinter import * # * Means all
import tkinter as tk
from tkinter import ttk
import random
import os
#from gtts import gTTS
import warnings
#from mutagen.mp3 import MP3
import time
import pygame
import sys
print(sys.path[0])
pygame.mixer.init()

#Make Some Fonts
LARGE_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 10)

    
#Make Something To Display All Pages :)
class SeaofBTCapp(tk.Tk):
        
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, runRetailTycoon2InfoGatherer):
        
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')
            
        self.show_frame(StartPage)
        
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()















#Make A Welcome Page :D
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.grid(row = 0, column = 3, columnspan = 2)
        
        returnBackwardsButton = tk.Button(self, text="<--", padx=15, pady=10, command=lambda: controller.show_frame(StartPage), state=DISABLED)
        returnBackwardsButton.grid(row=0, column=0)
        
        button1 = tk.Button(self, text="runRetailTycoon2InfoGatherer",width = 30, height = 5, command=lambda: controller.show_frame(runRetailTycoon2InfoGatherer))
        button1.grid(row = 1, column = 1)


class runRetailTycoon2InfoGatherer(tk.Frame):
    def __init__(self, parent, controller):
        global counter
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Run Retail Tycoon 2 Information Collector", font=LARGE_FONT)
        label.grid(row = 0, column = 3, columnspan = 1)

        returnBackwardsButton = tk.Button(self, text="<--", padx=15, pady=10, command=lambda: controller.show_frame(StartPage))
        returnBackwardsButton.grid(row=0, column=0)

        import retailTycoon2InfoGathererForGUI
        def executeFile():
            print(":P")
        
        button1 = tk.Button(self, text="Run Retail Tycoon 2 Information Collector",width = 50, height = 5, command=lambda: executeFile)
        button1.grid(row = 1, column = 1)

        answer_box = Entry(self, width = 50)
        answer_box.grid(row = 1, column = 2)

        message_box = Entry(self, width = 50)
        message_box.grid(row = 1, column = 3)


        def validateProduct(product):
            valid = False
            if len(product) > 3:
                for character in product:
                    if character in "aeiou":
                        valid = True
                
            return valid

        file = open("ProductsToValidate.txt", "r+")
        filesLines = file.readlines()
        file.close()
        try:
            message = (("Is %s a new item?")%( filesLines[0] ))
            message_box.insert(0,message)
        
        except:
            print("Unable to receive input.")
        def collectAnswer(file):

##            for i in range(len( filesLines )):
##                word = False
##                valid = validateProduct(filesLines[i])
##                if valid == False:
##                    print("Invalid boi")
##                    filesString.replace( filesLines[i] , "")


            fileReadLines = (filesLines)
            print(fileReadLines)

            message_box = Entry(self, width = 100)
            message_box.grid(row = 1, column = 3)
            anyDone = False
            while anyDone != True:
                if fileReadLines[0] != "\n" and fileReadLines[0] != "":
                    anyDone = True
                    message = (("Is %s a new item?")%( fileReadLines[0] ))
                    message_box.insert(0,message)

                    answer = answer_box.get()
                    answer = answer.lower()
                    if answer == "yes":
                        for item in fileReadLines:
                            
                            print("Item =",item)
                            if item != fileReadLines[0] and len(item) > 2:

                                file = open("validatedProducts.txt", "a")
                                file.write("\n"+item)
                                file.close()
                        
                    fileReadLines.pop(0)
                    print(fileReadLines)
                else:
                    fileReadLines.pop(0)
                
        
        submit_button = Button(self, text="Submit", command=lambda: collectAnswer(file), padx=128)

        submit_button.grid(row=2, column=2, columnspan=1)

        # Writes out question straight away
##
##        collectAnswer(line)



        def validateNewProducts():
            import retailTycoon2InfoGathererForGUI
            
            validationRequired, newProdcutRequest = retailTycoon2InfoGathererForGUI.executeProgram()

            for product in newProdcutRequest:

                message = (("Is %s a new item?")%(item))
                message_box.insert(0,answer)

                answer_box.insert(0,"Enter your message: (Yes or No)")
                answer = answer_box.get()
                answer = answer.lower()
                
                if answer == "yes":
                    retailTycoon2InfoGathererForGUI.validateNewProduct(product)
                





#Run The Loop :D
app = SeaofBTCapp()
app.mainloop()




