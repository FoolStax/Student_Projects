# Here, we are importing all the various different code we can use later on, especially pynput keyboard.
import tkinter as tk
import random
import time
from pynput.keyboard import Key, Controller, KeyCode
from pynput import keyboard


class snake_play:
# Here, we are creating a window that we can put our snake game into. We are naming the window itself 'snake', and putting a start button in it called 'play', that will bring up a second window with the actual game when pressed.
  def __init__(self):
    self.window=tk.Tk()
    
    self.button=tk.Button(text="play", width=25, height=5, bg="white",foreground="green", command=lambda:self.start())
    self.button.pack()

  def start(self):
    board = game_window()
    self.window.destroy()
    

# We are now creating an initial dirrection for the snake to start off with, which is horizontally and to the right.


# In this section, we are making it to where when a certain arrow key is pressed, the direction of the snake will change accordingly. 
    
# In this piece of code, we are making the actual snake window and destroying the starting 'play' window when the play button is pressed. We also set the properties of the snake window accordingly to have a certain height, width, and to be blue.



class game_window(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Snake")
    self.canvas = tk.Canvas(self,width=600, height= 400, bg="black")
    self.canvas.pack()
    self.actors = []
    self.snake = snake(self.canvas, self)
    self.apple = apple(self.canvas, self)
    self.actors.append(self.snake)
    self.actors.append(self.apple)
    self.running=True
    self.step()
  
  def step(self):
    try:
      for a in self.actors:
        a.step()
      self.after(200, self.step)
    except:
      pass

  def restart_snak(self):
    sp = snake_play()
    self.destroy()
    
    
class snake:
  def __init__(self, canvas, board):
    self.xDirection = 290
    self.yDirection = 190
    self.snaketot = []
    self.canvas = canvas
    self.board = board
    self.grow()
    self.direction="x+"
    self.listener = keyboard.Listener(on_press=self.on_press)
    self.listener.start()
    
  def grow(self):
    rectangle=self.canvas.create_rectangle(self.xDirection, self.yDirection,20+self.xDirection,20+self.yDirection, fill="#00ff00", outline="#00ff00", width=1) 
    self.snaketot.append(rectangle)
  
  def on_press(self,key):
    if key == keyboard.Key.up:
      self.direction = "y+"
    elif key == keyboard.Key.down:
      self.direction = "y-"
    elif key == keyboard.Key.right:
      self.direction = "x+"
    elif key == keyboard.Key.left:
      self.direction = "x-"
      
  def checkOverlap(self):
    #https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas-methods.html
    
    
    overlapsnak = self.canvas.find_overlapping(self.xDirection +5, self.yDirection+5, 15+self.xDirection, 15+self.yDirection)
    if len(overlapsnak)==1:
      self.canvas.delete(self.snaketot.pop(0))
    elif len(overlapsnak)==2 and self.canvas.type(overlapsnak[0])=="rectangle":
      #self.canvas.delete(self.snaketot.pop(0))
      self.board.restart_snak()
      #pass #restart
   # else: 
    #  pass
       #send signal to game_window to restart game

    
    # for x in overlapsnak:
    #   print(overlapsnak[0])
    # if (self.canvas.type(overlapsnak[0])) == "rectangle":
    #   self.canvas.delete(self.snaketot.pop(0))
    # else:
    #   pass
  
      
      #
      ##Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

      #Base it off of the object I.D. Find the snake object I.D, and if it overlaps with it, then end the game.
# self.canvas.find_overlapping(self.xDirection +1,self.yDirection+1,19+self.xDirection,19+self.yDirection)              if canvas.type()==rectangle
 

 
  
  def step(self):
    if self.direction == "y+":
      self.yDirection -=20
    elif self.direction == "y-":
      self.yDirection +=20
    elif self.direction == "x+":
      self.xDirection +=20
    elif self.direction == "x-":
      self.xDirection -=20
      
    self.grow()
    self.checkOverlap()

    
class apple:
# In this piece of code, we are creating a listener that acts on the direction that the snake is going. If the direction is up, it will go up 20 pixels. If the direction is right, it will go to the right 20 pixels. All of this is activated by the initial press of the specific arrow key.
  # put under keyinput class
  def __init__(self, canvas, board):
    self.canvas = canvas
    self.board = board
    self.circle = 0
    self.randomize()
  
  def randomize(self):
    parawidth=random.randrange(20,580,20)
    paraheight=random.randrange(20,380, 20)
    self.circle = self.canvas.create_oval(parawidth, paraheight, parawidth-1,   paraheight-1,  fill="red", outline="red", width=20)
    overlapapp=self.canvas.find_overlapping(parawidth+1,paraheight+1,19+parawidth,19+paraheight)
    if len(overlapapp)==2:
      self.canvas.delete(self.circle)
      self.randomize()
      
  def step(self):  
    pass
#INSIDE STEP: its looping, so find if its overlappinng annd then delete thhe apple and randomize it...
# During this, we are creating the 'snake', and settinng its parameters to be green and 20 pixels wide by 20 pixels in length. 
#put under snake_sprite class
    # rectangle=canvas.create_rectangle(xDirection, yDirection,20+xDirection,20+yDirection, fill="#00ff00", outline="#00ff00", width=1) 
    # snaketot.append(rectangle)
    
    
      
    
# Here, we are setting the amount of time it takes for the snake to move 1 'block'. We set this to a good .2 seconds, which gives the player enough time to react.
    #board.update()
   # canvas.delete(rectangle)
    #time.sleep(0.200)
# This line of code tells python to repeat the entire thihng over again, or 'loop' the code.
    
#window.mainloop() 

class border:
  def __init__(self,canvas,board):
    self.xDirection = 290
    self.yDirection = 190
    self.snaketot = []
    self.canvas = canvas
    self.board = board
    self.grow()
    self.direction="x+"
    self.listener = keyboard.Listener(on_press=self.on_press)
    self.listener.start()
    border=self.canvas.create_rectangle(self.xDirection, self.yDirection,20+self.xDirection,20+self.yDirection, fill="blue", outline="blue", width=1) 
    self.snaketot.append(rectangle)
    pass
    
sp = snake_play()
