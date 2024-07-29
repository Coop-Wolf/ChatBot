#pip install



from chatterbot import ChatBot
from chatterbot.traners import ListTrainer

import time
time.clock = time.time

bob = ChatBot("SimpleBot")

exit_conditions = ("quit", "exit")

while True:
  user_input = input("You: ")
  if user_input in exit_conditions:
    break
  else:
   responce = bob.get_response(user_input)
   print(" :", responce)