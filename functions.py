
import random
def length_of_file():
    with open('answers.txt', 'r') as f: 
        length = 0
        for i in enumerate(f): 
            length+=1
            
    return int(length)


def check_same(guess, answer):
   
    
    if guess == answer:
    
        return True
    return False
    
def get_target():

    length = length_of_file()
    num_choice = random.randrange(1,length)

    print(num_choice)


    with open('answers.txt', 'r') as f: 
        for i, line in enumerate(f, start=1):
            if i == num_choice: 
                choice = line.strip()
                break
        f.close()
    return choice


def check_valid_word(word):
    if len(word) != 5: 
        return 2
    with open('valid.txt', 'r') as f: 
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if check_same(word, line):
                return 0
    return 1