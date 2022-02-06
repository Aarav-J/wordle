from re import L
import subprocess
import random
def length_of_file():
    sub = subprocess.Popen("wc -l answers.txt", shell=True, stdout=subprocess.PIPE)
    subprocess_return = sub.stdout.read()
    answer = subprocess_return.decode('utf-8')
    nanswer = ""
    for i in range(len(answer)):
        if answer[i] == ' ':
            nanswer+='MM'
        else: 
            nanswer +=answer[i]
            
    num = 0
    length = ''
    for i in range(len(nanswer)):
        try: 
            if nanswer[i] != 'M':
                num += int(nanswer[i])
                length += nanswer[i] 
        except: 
            continue
            
    return int(length)


def check_same(guess, answer):
    if len(guess) != len(answer):
        return False
    
    if guess == answer:
    
        return True
    return False
    
    
length = length_of_file()
num_choice = random.randrange(1,length)

print(num_choice)


with open('answers.txt', 'r') as f: 
    for i, line in enumerate(f, start=1):
        if i == num_choice: 
            choice = line.strip()
            break
    f.close()
print(choice)


guess = input("Your guess: ")
with open('valid.txt', 'r') as f: 
    for i, line in enumerate(f, start=1):
        line = line.strip()
        if check_same(guess, line): 
            if check_same(guess, choice):
                print('congrats')
                break
        
    f.close()
        
