from termcolor import colored
import string 
import functions
import json

#[{'#': tries[], guesses[], time}]
with open('game.json', 'r+') as f: 
    data = json.load(f)
    f.close()

def wordIn(word, target):
    color = {}
    board_state = []
    num = 0
    word = word.lower()
    target = target.lower()
    for i in range(len(word)):
        if word[i] in target: 
            if word[i] == target[i]:
                color.update({word[i]: 'green'})
                board_state.append('green')
                num+=1
            else: 
                color.update({word[i]: 'yellow'})
                board_state.append('yellow')
        else: 
            color.update({word[i]: 'white'})
            board_state.append('white')
    
    return [color, num, board_state]


target = functions.get_target()

print(target)
flag = True
alphabetL = string.ascii_lowercase
alphabet = {}
win = False

#defaulting the keyboard to white
for i in range(len(alphabetL)):
    alphabet.update({alphabetL[i]: 'white'})
loops = 0
#starting the game loop
guesses = []
while(flag): 
    game = data['games-played'] + 1
    
    data['games-played'] +=1
    
    print("try: " + str(loops))
    word = input("choice: ")
    code = functions.check_valid_word(word)
    if code == 1:
        print("not a valid word")
        continue
    elif code == 2: 
        print('word is not 5 letters')
        continue
    else: 
        pass
    guesses.append(word)
    #Getting the boardstate
    colors = wordIn(word, target)
    
    for color in colors[0]: 
        alphabet[color] = colors[0][color]
    for alpha in alphabet: 
        print(colored(alpha, alphabet[alpha]), end=' ')
    print("\n\n")
    if colors[1] == 5: 
        flag = False
        win = True
           
    for i, color in enumerate(colors[2]):
      
        print(colored(word[i], color), end ='')

    print(guesses) 
    print()
    if(loops == 5):
        flag = False
    loops+=1


data["games"].append({'game': game, 'tries': loops, 'guesses': guesses, 'word': target, 'solved': win})


with open('game.json', 'w') as f: 
    json.dump(data, f, indent=4)
    f.close()
if win == True:
    print("you won in " + str(loops) + " tries.")
else: 
    print("HA you suck, you lost.")