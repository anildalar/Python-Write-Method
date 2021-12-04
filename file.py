
# Open function return a file object
#1. Always Open the file
fo = open("text1.txt","r")

lst = fo.readlines()
# l is infact a list
# so we can loop through the list with for in
#print(l[2])

for ln in lst:
    print(ln+" MCA Students")

#2. Always Close the file
fo.close()