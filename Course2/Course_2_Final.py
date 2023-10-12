#Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv
# which has the fake generated twitter data (the text of a tweet,
# the number of retweets of that tweet, and the number of replies to that tweet). 
#Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. 
#Copy the code from the code windows above, and put that in the top of this code window. 
#Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets,
# Number of Replies, Positive Score (which is how many happy words are in the tweet), 
#Negative Score (which is how many angry words are in the tweet), and the Net Score (
# how positive or negative the text is overall) for each tweet. The file should have those headers in that order. 
#Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets 
#and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, 
#if you’re accessing this textbook from Coursera.

#THIS IS THE FINAL PROGRAM PUT ALL TOGETHER. IGNORE ALL TEXT FILE AND PARAMETER ERRORS, THIS PROGRAM WORKS IN THE RUNESTONE
#ENVIRONMENT


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(x):
    for i in x:
        if i in punctuation_chars:
            x = x.replace(i, "")
    return x

def get_pos(x):
    x = x.lower()
    d = 0
    words = x.split()
    for word in words:
        word = strip_punctuation(word)
        if word in positive_words:
            d += 1
    return d
def get_neg(x):
    c=0
    x = x.lower()
    words=x.split()
    for word in words:
        word= strip_punctuation(word)
        if word in negative_words:
            c += 1
    return c

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
outfile = open("resulting_data.csv","w")
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write('\n')


fileconnection = open("project_twitter_data.csv", 'r')

lines = fileconnection.readlines()
print(lines)
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    
    vals = row.strip().split(',')
    row_string = '{},{},{},{},{}'.format(vals[1],vals[2],get_pos(vals[0]),get_neg(vals[0]),get_pos(vals[0])-get_neg(vals[0]))
    outfile.write(row_string)
    outfile.write('\n')


outfile.close()

