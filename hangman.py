import random


print('''

  _    _          _   _  _____ __  __          _   _ 
 | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
 | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
 |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
 | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
 |_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|
                                                     
                                                    
''')

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar ' 
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
           'goose hawk lion lizard llama mole monkey moose mouse mule newt ' 
           'otter owl panda parrot pigeon python rabbit ram rat raven ' 
           'rhino salmon seal shark sheep skunk sloth snake spider ' 
           'stork swan tiger toad trout turkey turtle weasel whale wolf '
             'wombat zebra ').split()
lives=6
selected_word=random.choice(words)
encrypted_word=[]
guess_word=[]

for letter in selected_word:
     guess_word.append(letter)
     encrypted_word.append("_")


def matchword(_userin):
   ismatch=False
   for index,letter in enumerate(guess_word):
      if (letter ==_userin):
        encrypted_word[index]=letter
        ismatch=True
   if (ismatch==True):
         return True
   else: return False
   
def controlgame(isguesstrue):
   global lives
   if(isguesstrue==False):
      print(f"wrong {lives} and chance left")
      print(encrypted_word)
      print(HANGMANPICS[6-lives])

      if(lives==0):
         print("game is over")
         print(f"the word is {selected_word}")
         return True
      else :
         lives-=1
         return False
   elif(lives!=0):
      print("good job enter your next move")
      wordleft=encrypted_word.count("_")
      if(wordleft==0):
         print("you win")
         print(f"the word was{encrypted_word}")
         return True
      else:
         print(encrypted_word)
         return False
      



def callguess():
   userin=input("Guess your word: ")
   #output=matchword(userin)
   if(len(userin))!=1:
      return False
   userin=userin.lower()
   return userin
      


print(f" your word will be this length:{encrypted_word}")

while True:
   userin=callguess()
   
   if(userin!=False):
        state= matchword(userin)
        if( controlgame(state)):
            break
        