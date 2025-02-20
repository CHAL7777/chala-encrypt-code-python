word_list=["ardwak","baboon","camel"]
import random
chosen_word=random.choice(word_list)
print(f"pssst, the solution is {chosen_word}")
display=[]
word_length=len(chosen_word)
for _ in range(word_length):
 display+="_"
end_of_game=False
while not end_of_game:
  guess=input("guess a letter: ").lower()
  for position in range(word_length):
    letter=chosen_word[position]
    # print(f"current position: {position}\n current letter: {letter}\n guessed letter: {guess}")
    if letter==guess:
      display[position]=letter
  print(display)
  if "_" not in display:
    end_of_game=True
    print("you win.")