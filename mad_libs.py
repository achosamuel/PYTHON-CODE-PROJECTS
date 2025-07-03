import os

with open('story.txt','r') as f:
    story = f.read()

start_index = -1
words = set()

for i, char in enumerate(story):
    if char == '<' :
        start_index = i

    if char == '>' and start_index != -1:
        word = story[start_index: i+1]
        words.add(word)

for word in words:
    answer = input(f"Enter a word for {word[1:len(word) -1]}: ")
    story = story.replace(word,answer)
print(story)

save_option = input("you want to save your file(y/n)? ")
if save_option.lower() == 'y':
    while True:
        filename = input("give a name to your file: ")
        if os.path.exists(filename):
            print("This file already exist change the name!!")
        elif filename.lower() == 'q'
            break
        else:
            with open(filename, 'w') as f:
                f.write(story)
else:
    print("Thanks!, Bye!!!")
