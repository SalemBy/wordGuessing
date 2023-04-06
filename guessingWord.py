from sys import platform
import random 
import time
import os

# Clean terminal

if platform == "win32" or platform == "cygwin":
	clearcmd = "cls"
else:
	clearcmd = "clear"
        
 # Generate Word

rand = random.randint(1,5)
word = ''
rightLetter = ''
tries = 0


            
match rand:
    case 1:
        word = "perfume"
    case 2:
        word = "chocolate"
    case 3:
        word = "video"
    case 4:
        word ="regular"
    case 5:
        word = "item"



while True:
            
    # Get user input\guess
    letter = str(input("\nEnter a letter: "))
    size = len(letter)


    if size > 1:
        os.system(clearcmd)
        print("Enter only 1 letter")
        time.sleep(1)
        os.system(clearcmd)
        continue

    elif letter.isdigit():
        os.system(clearcmd)
        print("Enter only letters")
        time.sleep(1)
        os.system(clearcmd)
        continue

    # Check Letter
    tries += 1

    if letter in word:
        rightLetter += letter
    
    answer = ''
    for i in word:

        if i in rightLetter:
            answer += i

        else:
            answer += '*'
    print(answer)

    if answer == word:
        print( "You win!!")
        print(f"Tries = {tries}")
        print(f"The word was {word}")
        break

            
       

            
        
        
    
        


        

    
    
