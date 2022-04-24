'''Twitch Ping v0.1-dev by Defirence'''
# Packages and Modules
import sys
import os
from tkinter import *
import tkinter
import tkinter.messagebox
# Variables
tw_region_za = "South Africa"
tw_region_za_ip = "151.101.226.167"
tw_region_usa = "United States of America"
tw_region_usa_ip = "127.0.0.1"
# Main class for the Window.
class Window(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_window()

    def init_window(self):
        self.master.title('Twitch Ping v0.1')
        self.pack(fill=BOTH, expand=1)
# Button functions for Tkinter go below this line.
        pingButton = Button(self, text="Ping!", command=self.twitch_server_za)
        pingButton.place(x=0, y=0)

        pingButtonUS = Button(self, text="US", command=self.twitch_server_usa)
        pingButtonUS.place(x=40, y=0)
        
        quitButton = Button(self, text='Quit', command=self.client_exit)
        quitButton.place(x=514, y=0)
# Main functions for servers go below this line.
    def twitch_server_za(self):
        print("Pinging Twitch Server located in " + tw_region_za)
        response = os.system("ping " + tw_region_za_ip)
        if response == 0:
            result = "Server Reachable"
        else:
            result = "Server Unreachable"

    def twitch_server_usa(self):
        print("Pinging Twitch Server located in " + tw_region_usa)
        response = os.system("ping " + tw_region_usa_ip)
        if response == 0:
            result = "Server Reachable"
        else:
            result = "Server Unreachable"            
# Empty space here for further functions
# and just for sanity while writing this
# to ensure this stays neat.
#
# Other functions go down here that rely
# on the functions above to return a
# response first.
        if result == "Server Reachable": tkinter.messagebox.showinfo(title=result, message="Ping Success")
        elif result == "Server Unreachable": tkinter.messagebox.showinfo(title=result, message="Ping Failure")
    
    def client_exit(self):
        sys.exit(0)
root = Tk()
root.geometry("550x245")
app = Window(root)
root.mainloop()
