########
####Python for Informatics
####Assignment3B-“Looping, Searching, and Slicing”
####Kalyani Vaidya
########

avg_str = 'Average value read: 0.72903'
index=avg_str.find(":")
s=avg_str[index:]
index1=s.find(" ")
print(s[index1:])
num=float(s[index1:])
print(type(num))
