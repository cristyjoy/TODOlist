print("Use Yes Or No For Answers That Require It") 
from datetime import datetime #imports time package count=0 #sets count to 0 
while True: 
        count +=1 
        if count >3: 
            break 
        name=input("what is your name\n") 
        yob=int(input("what is your yob\n")) 
        year = datetime.now().year #sets year 
        age=year-yob # sets age as a constant 
        print("so you are",age,) 
        user_input=input ("is this correct\n") 
        if user_input==("yes"): 
            print("nice")
            with open('file.txt', 'a') as outfile:
                outfile.write("%s\t%d\t%d\n"%(name, yob, year))
        else: 
            print("oops, you must be",age-1)