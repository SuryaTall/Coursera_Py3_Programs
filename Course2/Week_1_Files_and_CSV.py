#All txt files will be pre-defined in the Runestone Environment, so the errors regarding that can be ignored.

#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
# Find the total number of characters in the file and save to the variable num.

fileref = open("travel_plans.txt", "")
strings = fileref.read()
num = 0
for i in strings:
    num += 1
fileref.close()

#We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
#  Find the total number of words in the file and assign this value to the variable num_words.

num_words = 0
fileref = "emotion_words.txt"
with open(fileref, 'r') as file:
    for line in file:
        num_words += len(line.split())

#Assign to the variable num_lines the number of lines in the file school_prompt.txt.

fileref = open("school_prompt.txt", "") 
num_lines = 0
num_lines2 = fileref.readlines()
for i in num_lines2:
    num_lines += 1
fileref.close()

#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
fileref = open("school_prompt.txt", "") 
beginning_chars = fileref.read(30)
fileref.close()

#Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.

three = []
with open("school_prompt.txt", 'r') as f:
    three = [line.split()[2] for line in f]

#Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.

emotions = []
with open("emotion_words.txt", 'r') as x:
    line = x.readlines()
    for words in line:
        word = words.split()
        emotions.append(word[0])

#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

fileref = open("travel_plans.txt", "") 
first_chars = fileref.read(33)
fileref.close()

#Challenge: Using the file school_prompt.txt,
#  if the character ‘p’ is in a word, then add the word to a list called p_words.

fileref = open("school_prompt.txt", "") 
p_words = []
words = fileref.read().split()
p_words = [word for word in words if 'p' in word]
fileref.close()