print("Welcome to my computer quiz!")

correct_answer = 0
playing = input("do you want to play(y/n)?: ").lower()

if playing[0] != "y" :
    print("Bye!!")
    quit()

print("Super! let's play")

answer_1 = input("what is the capital of france?: ").lower()
if answer_1 == "paris":
    print("Correct answer")
    correct_answer += 1
else:
    print("Incorrect answer")

answer_2 = int(input("what is 2 * 12 ?: "))
if answer_2 == 24 :
    print("Correct answer")
    correct_answer += 1
else:
    print("Incorrect answer")

answer_3 = int(input("how many country are there in USA?: "))
if answer_3 == 54 :
    print("Correct answer")
    correct_answer += 1
else:
    print("Incorrect answer")

percentage = round((correct_answer / 3) *100,2)
print("You answered correct to: " + str(correct_answer) + " questions")
print (f"you got: {percentage}% correct")
