#The variable nested contains a nested list. Assign ‘snake’ to the variable output using indexing

nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output =""

for i in nested:
    for j in i:
        if j == "snake":
            output = j
            break

#Below, a list of lists is provided.
#  Use in and not in tests to create variables with Boolean values. See comments for further instructions.

lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
yellow = False
if "yellow" in lst[2]:
    yellow = True
    

#Test to see if 4 is in the second list of lst. Save to variable ``four``
four = False
if 4 in lst[1]:
    four = True
    

#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
orange = False
if "orange" in lst[0]:
    orange = True
    
#Below, we’ve provided a list of lists. 
# Use in statements to create variables with Boolean values - see the ActiveCode window for further directions.


L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
test1 = False
for i in L:
    if i == "hola":
        test1 = True
        break
            

# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2 = False
for i in L:
    if i == [5, 8, 7]:
        test2 = True
        break

# Test if 6.6 is in the third element of list L. Save to variable name test3
test3 = False
for i in L[2]:
    if i == 6.6:
        test3 = True
        break

#Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.


nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string 'data' is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data = False
for i in nested:
    if i == "data":
        data = True
        break
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour = False
for i in nested:
    for j in i:
        for k in j:
            if k == 24:
                twentyfour = True
                break

# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
whole = False
for i in nested:
    for j in i:
        if j == "whole":
            whole = True 
            break

# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
physics = False
for i in nested:
    for j in i:
        for k in j:
            for l in k:
                if l == "physics":
                    physics = True
                    break

#The variable nested_d contains a nested dictionary with the gold medal counts for the
#  top four countries in the past three Olympics. Assign the value of Great Britain’s gold medal count
#  from the London Olympics to the variable london_gold. Use indexing. Do not hardcode.

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
london_gold = nested_d['London']['Great Britain'] 

#Below, we have provided a nested dictionary.
#  Index into the dictionary to create variables that we have listed in the ActiveCode window.

sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}
v1 = sports['swimming'][2]
# Assign the string 'platform' to the name v2
v2 = sports['diving'][1]
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports['gymnastics']['women']
# Assign the string 'rings' to the name v4
v4 = sports['gymnastics']['men'][-1]

#Given the dictionary, nested_d, 
# save the medal count for the USA from all three Olympics in the dictionary to the list US_count.

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []
for i in nested_d:
    temp = nested_d[i]['USA']
    US_count.append(temp)

#Iterate through the contents of l_of_l and assign the third element of sublist to a new list called third.

l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third = []
for i in l_of_l:
    third.append(i[2])

#Given below is a list of lists of athletes. Create a list, t, that saves only the athlete’s name
#  if it contains the letter
#  “t”. If it does not contain the letter “t”, save the athlete name into list other.

t = []
other = []
athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
for lst in athletes:
    for name in lst:
        if 't' in name:
            t.append(name)
        else:
            other.append(name)
