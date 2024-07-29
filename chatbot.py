#pip install
from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer

import time
time.clock = time.time

bob = ChatBot("SimpleBot")
#trainer = ListTrainer(bob)

#trainer.train(["What's your name?",
 #                 "My name is Alex",
  #             "How old are you?",
   #               "I am 2000 years old",
   #            "How are you?"
   #               "Fine, thank you",
   #            "Are you going to take over the world",
   #               "Yes",
   #            "What is the meaning of life?
   #               "To know, love and imitate Jesus"
#               "Goodbye"
#                  "Bye"])

exit_conditions = ("quit", "exit")

while True:
  user_input = input("You: ")
  if user_input in exit_conditions:
    break
  else:
   responce = bob.get_response(user_input)
   print(" :", responce)