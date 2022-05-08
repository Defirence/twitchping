'''Twitch Ping v0.1-dev by Defirence'''

import sys
import os
from tkinter import BOTH, Tk, Frame, Button, messagebox

TRL_HYPERLAYER_ZA = "Relay: Hyperlayer JHB,ZA -> LHR,UK"
TRL_HYPERLAYER_ZA_IP = "156.38.201.100"

class Window(Frame):
    """Main class that handles the Window Frame"""
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_window()

    def init_window(self):
        """Function to handle the buttons and window init"""
        self.master.title('Twitch Ping v0.1')
        self.pack(fill=BOTH, expand=1)
        ping_button = Button(self, text="Hyperlayer", command=self.trl_hyperlayer_za)
        ping_button.place(x=0, y=0)
        quit_button = Button(self, text='Quit', command=self.client_exit)
        quit_button.place(x=514, y=0)

    def trl_hyperlayer_za(self):
        """Function to handle the latency testing"""
        print("Pinging " + TRL_HYPERLAYER_ZA)
        response = os.system("ping " + TRL_HYPERLAYER_ZA_IP)
        if response == 0:
            result = "Ping Success"
        elif response != 0:
            result = "Ping Failure"
        if result == "Ping Success":
            messagebox.showinfo(title=result,
            message=TRL_HYPERLAYER_ZA + " is online.\n"
            + "Latency Results are:\n" + str("min=XYms\nmax=XYms\navg=XYms"))
        return self.parent

    def client_exit(self):
        """Does what it says on the box"""
        sys.exit(0)

root = Tk()
root.geometry("550x245")
app = Window(root)
root.mainloop()
