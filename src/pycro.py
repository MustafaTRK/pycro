import sys, os, random, time, threading
try:
  from pynput.keyboard import KeyCode, Listener, Key
  from pynput.mouse import Button, Controller
except ImportError as error:
  raise ImportError("'pynput' not found in modules! Please install 'pynput'")

class pycro(threading.Thread):
  def __init__(self, cps, button, limit):
    super(pycro, self).__init__()
    self.mouseController = Controller()
    self.delay = 1 / cps
    self.button = button
    self.limit = limit
    self.clickCounter = 0
    self.clickingState = False
    self.programState = True

  def toggleClicking(self):
    if self.clickingState:
      self.clickingState = False
    else:
      self.clickingState = True

  def exitPycro(self):
    self.clickingState = False
    self.programState = False
    sys.exit()

  def run(self):
    while self.programState:
      while self.clickingState:
        if (self.limit > 0 and self.limit == self.clickCounter):
          self.clickingState = False
          self.clickCounter = 0
        else:
          self.mouseController.click(self.button)
          self.clickCounter += 1
          time.sleep(self.delay)
      time.sleep(0.5)

if __name__ == '__main__':
  if os.name == "nt":
    clear = lambda: os.system("cls")
  else:
    clear = lambda: os.system("clear")

  print("How many times do you want to click per second?")
  cpsRaw = input("CPS (Only integers): ")
  try:
    cps = int(cpsRaw)
  except ValueError as error:
    raise TypeError("CPS must be a integer!")
    exit()
  clear()

  print("Which button will be used to activate and deactivate the macro?")
  toggleKeyRaw = input("Key (Only letters): ")
  if len(toggleKeyRaw) > 1:
    raise ValueError("You can only specify one letter at a time!")
    exit()
  else:
    if toggleKeyRaw.isalpha():
      toggleKey = KeyCode(char=toggleKeyRaw)
    else:
      raise TypeError("You can only use letters!")
      exit()
  clear()

  print("How many clicks will it stop after it starts clicking?")
  limitRaw = input("Limit (Only integers, typing 0 for unlimited): ")
  try:
    limit = int(limitRaw)
  except ValueError as error:
    raise TypeError("Limit must be a integer!")
    exit()
  if limit == 0:
    limitRaw = "Unlimited"
  clear()

  print("Which button will the macro click on? (l = left, r = right, m ​​= middle)")
  buttonRaw = input("Key (Only l = left or r = right or m ​​= middle): ")
  if (buttonRaw == "l" or buttonRaw == "left"):
    buttonRaw = "Left"
    button = Button.left  
  elif (buttonRaw == "r" or buttonRaw == "right"):
    buttonRaw = "Right"
    button = Button.right
  elif (buttonRaw == "m" or buttonRaw == "middle"):
    buttonRaw = "Middle"
    button = Button.middle
  else:
    raise TypeError("You must enter a valid mouse button!")
    exit()
  clear()

  print("Which key will you use to instantly close the macro under any circumstances?")
  exitKeyRaw = input("Key (Only letters): ")
  if len(exitKeyRaw) > 1:
    raise ValueError("You can only specify one letter at a time!")
    exit()
  else:
    if exitKeyRaw.isalpha():
      exitKey = KeyCode(char=exitKeyRaw)
    else:
      raise TypeError("You can only use letters!")
      exit()
  clear()

  macro = pycro(cps, button, limit)
  macro.start()
  
  print("Pycro is started ;)")
  print(
    """
      CPS: {cps}
      Aktive/Deaktive Key: {toggleKey}
      Clicking Limit: {limit}
      Selected Mouse Button: {mouseButton}
      Exit Key: {exitKey}
    """.format(cps = cps, toggleKey = toggleKeyRaw.upper(), limit = limitRaw, mouseButton = buttonRaw, exitKey = exitKeyRaw.upper()))

  def keyInput(key):
    if (key == toggleKey or str(key).lower() == str(toggleKey).lower()):
      macro.toggleClicking()
    elif (key == exitKey or str(key).lower() == str(exitKey).lower()):
      print("Pycro is stopped :o")
      keyListener.stop()
      macro.exitPycro()

  with Listener(on_press=keyInput) as keyListener:
    keyListener.join()
