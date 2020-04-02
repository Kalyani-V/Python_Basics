########
####Python for Informatics
####Assignment3A-“Looping, Searching, and Slicing”
####Kalyani Vaidya
########

lst=[]
num=input("Please start entering numbers. If not then press 'done' : ")
if(num=="done"):
    exit(0)
else:
    lst.append(int(num))
    print(lst)    
    while(num!="done"):
        num=input("Enter any number : ")
        if(num=="done"):
            break
        else:
            lst.append(int(num))
            print(lst)

total=sum(lst)
avg=total/len(lst)
print("Total is: {}".format(total))
print("Average is : {}".format(avg))
print("Maximum of the list is : {}".format(max(lst)))
print("Minimum of the list is : {}".format(min(lst)))
    
