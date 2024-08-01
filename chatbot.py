import re
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
time.clock = time.time

#string to copy file
play = ""
Hamlet_lines = []

# opening file and copying to string 
# this was done because I wasn't sure
# if I could use the file in the re.findall 
# function directly
with open("Hamlet.txt") as file:
  for line in file:
    for word in line.split():
      play += word + " "

# using regex to store only the lines of Hamlet
Hamlet = (re.findall("([A-Z][a-z\s][^\\.!?]*[\\.!?])", play))

# going through list and printing each line
for line in Hamlet:
  print(line)
  Hamlet_lines.append(line)
  

HamletBot = ChatBot("SimpleBot")
trainer = ListTrainer(HamletBot)
trainer.train(Hamlet_lines)
trainer.train(["What's your name?",
                  "My name is Hamlet",
               "How old are you?",
                  "I am 300 years old",
               "How are you?"
                  "Fine, thank you",
               "Who killed you",
                  "Laertes, he poisoned me",
               "What is the meaning of life?"
                  "To know, love and imitate Jesus"
               "Goodbye"
                  "Bye"])

exit_conditions = ("quit", "exit")

while True:
  user_input = input("You: ")
  if user_input in exit_conditions:
    break
  else:
   response = HamletBot.get_response(user_input)
   print("Hamlet:", response)
