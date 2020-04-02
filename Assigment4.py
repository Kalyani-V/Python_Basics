import sys
import os
from os import path
filename = input("Enter the file name with extention : ")
filepath = "C:/Users/kalya/Desktop/Python/UCSD/"
fname = str(filepath+filename)
print(fname)

if os.path.isfile(fname):
    print("File exists on the path")
    fhand = open(fname)
    read_data = fhand.read()
    print ("\nContents of the file are : \n {}".format(read_data))
    line_list = read_data.splitlines()
    words=[]
    print("Length",lenth)
    for i in range(lenth):
        w=line_list[i].split()
        words.append(w)
    print("\n List of words are: \n {} \n".format(words))

    length=len(words)
    script_list = []
    print("Contents of the script_list :\n {} \n".format(script_list))
    for i in range(length):
        for j in range(len(words[i])):
            if words[i][j] in script_list:
                print("{} is already present in script_list".format(words[i][j]))
            else:
                lst = words[i][j].lower()
                script_list.append(lst)
    
    script_list.sort()
    print("\n After sorting, new list is : \n {} ".format(script_list))
    
else:
    print("File does not exist on the path")
    sys.exit()
    
def freq_count(search_str, script_list):
    lst_len = len(script_list)    
    print("Number of occurences of substring are: \n")
    for i in range(lst_len):
        cnt = 0
        if search_str in script_list[i]:
            cnt = script_list[i].count(search_str)
            print("{} {}".format(script_list[i],cnt))
        else:
            print("{} {}".format(script_list[i],cnt))
        
search_str = input("Enter any string : ")
freq_count(search_str,script_list)
                
