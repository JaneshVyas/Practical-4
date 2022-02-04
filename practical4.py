# Id-20CS102            Name-Janesh Vyas

# Total numbers and string of numbers are taken as input 
total_num=int(input())
str=input()
# String of numbers are stored in list
str_list=str.split()
# list of numbers are converted to integer and stored in another list
num_list=[]
for i in str_list:
    num_list.append(int(i))

# Maximum number from the list is stored in max_num variable
max_num=0

for j in num_list:
    if j>max_num:
        max_num=j

# Runnerup variable is declared and initialised to 0.
# Whole list is checked and if the number in the list is less than max_num and
# greater than runnerup it is stored in runnerup and is displayed 
runnerup=0

for k in num_list:
    if k<max_num:
        if k>runnerup:
            runnerup=k

print(runnerup)

