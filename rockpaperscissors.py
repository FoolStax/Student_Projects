import tkinter as tk
from tkinter import ttk
import random
from _ast import If


class windows(tk.Tk):
  def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("RPS Player")

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=100, width=200)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}

        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (Main, win, Loss, Tie):

            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            #frame.pack()
            frame.grid(row=0, column=0, sticky="nsew")
        # Using a method to switch frames
        self.show_frame(Main)
  def show_frame(self, cont):

      frame = self.frames[cont]
      # raises the current frame to the top
      frame.tkraise()


class Main(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        text1 = tk.Label(self, text="choose an option")

        container = tk.Frame(self, height=100, width=200)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        text1.place(x=75, y=25)
        text1.pack()

        button1 = tk.Button(self,
                            text="rock",
                            command=lambda: Main.check(self, "rock"))
        button1.place(x=25, y=100)
        button1.pack()

        button2 = tk.Button(self, text="paper",
          command=lambda: Main.check(self, "paper"))
        button2.place(x=100, y=100)
        button2.pack()

        button3 = tk.Button(self, text="scissors",
          command=lambda: Main.check(self, "scissors"))
        button3.place(x=175, y=100)
        button3.pack()

    def check(self, choice):
        
        rps_gen=random.choice(['rock','paper', 'scissors'])
        print(rps_gen)

        if choice == rps_gen:

            self.controller.show_frame(Tie)
        elif choice == "rock":
            if rps_gen == "scissors":
                self.controller.show_frame(win)
            else:
                self.controller.show_frame(Loss)
        elif choice == "paper":
            if rps_gen == "rock":
                self.controller.show_frame(win)
            else:
              
                self.controller.show_frame(Loss)
        elif choice == "scissors":
            if rps_gen == "paper":

                self.controller.show_frame(win)
            else:
                self.controller.show_frame(Loss)
        else:
            self.controller.show_frame(Main)


class Tie(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Tie. You are a worthy foe")
        label.pack(padx=50, pady=50)
        switch_window_button = ttk.Button(
            self,
            text="Return to menu",
            command=lambda: controller.show_frame(Main))
        switch_window_button.pack(side="bottom", fill=tk.X)


class win(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="You win, ya brat")
        label.pack(padx=50, pady=50)
        switch_window_button = ttk.Button(
            self,
            text="Return to menu",
            command=lambda: controller.show_frame(Main))
        switch_window_button.pack(side="bottom", fill=tk.X)


class Loss(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="I win! Gotcha!")
        label.pack(padx=50, pady=50)
        switch_window_button = ttk.Button(
            self,
            text="Return to menu",
            command=lambda: controller.show_frame(Main))
        switch_window_button.pack(side="bottom", fill=tk.X)


#if __name__ == "tkniner classes":
testObj = windows()
testObj.mainloop()
