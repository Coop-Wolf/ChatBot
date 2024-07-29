#pip install



from chatterbot import ChatBot
from chatterbot.traners import ListTrainer

import time
time.clock = time.time

bob = ChatBot("SimpleBot")
trainer = ListTrainer(bob)

trainer.train(["What's your name?",
                  "My name is Alex",
               "How old are you?",
                  "I am 2000 years old"])

exit_conditions = ("quit", "exit")

while True:
  user_input = input("You: ")
  if user_input in exit_conditions:
    break
  else:
   responce = bob.get_response(user_input)
   print(" :", responce)