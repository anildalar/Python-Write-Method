

# 

msg = input("Please enter your message")

#.1 Lets create a file
fo = open('mymsg.txt','a')

print(msg)

fo.write('\n'+msg)


# Lets close the file
fo.close()
