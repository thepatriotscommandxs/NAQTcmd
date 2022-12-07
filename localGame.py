
import os,sys
import random
import ast
fileName = sys.argv[0].split("/")[::-1][0].split(".")[1]

if (fileName == "py"):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
else:
    __location__ = os.getcwd()

itemCount = len((os.listdir(__location__+"\\data")))

items = os.listdir(__location__+"\\data")

FileNumber = random.randint(0,itemCount)

FileName = items[FileNumber]

with open(__location__+"\\data\\"+FileName) as r:
    contents = r.readlines()

for i in range(len(contents)):
    contents[i] = contents[i].replace("\n","")


contents = ast.literal_eval(str(contents))

for i in range(len(contents)):
    contents[i] = contents[i].split("', '")

FileName = FileName.replace("-"," ").replace(".txt","")

try:
    with open(__location__+"\\streak.txt","r") as f:
        f.close()
except:
    with open(__location__+"\\streak.txt","w") as w:
        w.write("0")
        w.close()

outer_len = len(contents)

outerRand = random.randint(0,outer_len)

try:
    FullHint = str(contents[outerRand][1])
except:
    print(FileName)
    print(contents[outerRand])
    quit()

answer = str(contents[outerRand][0]).replace("['","")

array_answer = answer.split(" ")

if(type(array_answer)==list):
    for i in range(len(array_answer)):
        FullHint = FullHint.replace(array_answer[i],"**This Answer** ").replace("This Thing ","**This Answer** ")

counter = 0
currentHint = ""
wasCorrect = ""

hint_array = FullHint.split(".")

def inAnswer():
    global array_answer,answer,Guess,wasCorrect
    for i in range(len(array_answer)):
        if(Guess.lower() == array_answer[i].lower()):
            wasCorrect= "True"


def giveAnswer():
    global counter,currentHint,Guess,hint_array,FileName


    currentHint += hint_array[counter] + "."


    print("Category is:   "+FileName.upper())
    
    print(currentHint)


    Guess = input("Take your Guess \n")


    inAnswer()
    if(wasCorrect=="True"):
        print("CORRECT!!!")
        
        with open(__location__+"\\streak.txt","r") as x:
            streak = x.read()
            streak = int(streak)
            streak += 1
            x.close()
            
        with open(__location__+"\\streak.txt","w") as z:
            z.write(str(streak))
            
            z.close()
            
        print("Answer => "+answer+"\nCurrent Streak ===> "+str(streak))

    else:

        counter += 1
        try:
            giveAnswer()
        except:
            print("\nANSWER IS: \n\n"+answer+"\n\n")




giveAnswer()


input()
