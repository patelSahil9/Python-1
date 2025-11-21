#check if a file contains a specific word
# with open("00_first.py") as f:
#     content=f.read()
#     if("print" in content):
#         print("The file contains print statement")
#     else:
#         print("The file does not contain print statement")
        
# program to let user play game and return score as an integer value and store in the txt file
# import random
# def play_game():
#     print("you are playing game")
#     score = random.randint(0, 100)
#     with open("game_score.txt") as f:
#         sscore = f.read()
#         if sscore != "":
#             sscore = int(sscore)
#         else:
#             sscore = 0
#     print(f"Your score is: {sscore}")
#     if sscore < score:
#         with open("game_score.txt", "w") as f:
#             f.write(str(score))
#     return sscore
# play_game()

# def generate_table(n):
#     table = ""  # an empty string
#     for i in range(1, 11):
#         table += f"{n} x {i} = {n*i}\n"
#     with open(f"tables/table_of_{n}.txt", "w") as f:
#         f.write(table)
#     return table
# for i in range(2, 21):
#     generate_table(i)



# function to replace words in a file with *****
# def changeword(words):
#     """
#     This function takes a list of words and replaces them with ***** in the file 'ex/word.txt'

#     Parameters:
#     words (list): list of words to replace

#     Returns:
#     None
#     """
#     with open("ex/word.txt","r+") as f:
#         content = f.read()
#         # iterate over each word in the list
#         for w in words:
#             # replace the word with *****
#             content = content.replace(w, "*****")
#         # go to the beginning of the file
#         f.seek(0)
#         # write the new content
#         f.write(content)
#         # truncate the file to the new length
#         f.truncate()
# changeword(word)
nord=["python","schedule"]
with open ("ex/word.txt","r") as f:
    content = f.readlines()
    found = False
    for i,line in enumerate(content):
        if any(word in line for word in nord):
            print(f"Yes word is present at line number: {i+1}")
            found = True
    if not found:
        print("wait bruh")

