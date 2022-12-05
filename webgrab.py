import random
from selenium import webdriver
import re
import os,sys


fileName = sys.argv[0].split("/")[::-1][0].split(".")[1]

if (fileName == "py"):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
else:
    __location__ = os.getcwd()

try:
    with open (__location__+"\\webs.txt", "r") as f:
        data = f.read()
except:
    print("Need to get the webs txt")

data = data.split("\n")

urlRand = random.randint(0, len(data)-1)


url = data[urlRand]

#url = "https://www.naqt.com/you-gotta-know/calculus-ideas.html"

driver = webdriver.Edge(executable_path="D:\\thepa\\Downloads\\edgedriver_win64\\msedgedriver.exe")

# Opening the URL
driver.get(url)
  
# Getting current URL source code
get_source = driver.page_source
driver.close()

if(get_source.__contains__('<footer>')):
    tempCat = get_source.split("<footer>",1)    

tempCat[1] = ""

get_source = "".join(tempCat)

titleBOOL = ""

if(get_source.__contains__("<section id=")):
    category = get_source.split('<section id="')
     
elif(get_source.__contains__('<ul class="ygk">')):
    category = get_source.split('<ul class="ygk">')

    header = category[0].split("<h1>")[1]
    header = header.split("</h1>")[0]
    titleBOOL = "True"
    

for i in range(len(category)):
    if(category[i].startswith("honorable-mention")):
        category.pop(i)


for i in range(len(category)-1):
    if(category[i].startswith('<html lang="en"><head>')):
        category.pop(i)

for i in range(len(category)-2):
    if(category[i].startswith('recommended-reading')):
        category.pop(i)

for i in range(len(category)-3):
    if(category[i].startswith('<p class="ygk-attribution">')):
        category.pop(i)

for i in range(len(category)):
    category[i] = category[i].split("</li>")


for i in range(len(category)):
    for ii in range(len(category[i])+1):
        try:
            category[i][ii] = category[i][ii].split("</",1)  
        
        except:
            pass 
    
for i in range(len(category)):
    for ii in range(len(category[i])):

        for iii in range(len(category[i][ii])):
            category[i][ii][iii] = category[i][ii][iii].replace('<span class="ygk-term">',"").replace('</span>',"").replace("</li>","").replace("\n","").replace("\t","").replace('<span class="label">',"").replace("</ul>","").replace("</section>","").replace("\u2009","").replace("&nbsp"," ").replace("span>","")
            category[i][ii][iii] = re.sub('s"><h2>[a-zA-Z]+</h2><ul class="ygk">',"",category[i][ii][iii])
            category[i][ii][iii] = re.sub('<[a-zA-Z0-9=":/.\-\?%()_ ]+>',"",category[i][ii][iii])

# [i] is the category, [ii] is the term, [iii] is the descriptor
category = list(filter(None,category))
array_len = 0



for i in range(len(category)):
    for ii in range(len(category[i])):
        try:
            category[i][ii+1][1] = category[i][ii+1][1].replace(category[i][ii+1][0],"This "+category[i][0][0])
            category[i][ii+1][1] = category[i][ii+1][1].replace(category[i][ii+1][0].lower(),"This "+category[i][0][0])
            
            for iv in range(len(category[i][ii+1][0].split(" "))):
                category[i][ii+1][1] = category[i][ii+1][1].replace(category[i][ii+1][0].split(" ")[iv],"*****")
                category[i][ii+1][1] = category[i][ii+1][1].replace(category[i][ii+1][0].split(" ")[iv].lower(),"*****")
        except: 
            pass



for i in range(len(category)):
    for ii in range(len(category)):
        if(category[i][ii]==""):
            category.pop(ii)

outer_len = len(category)

outerRand = random.randint(0,len(category)-1)

array_len = len(category[outerRand])-1
rand = random.randint(0,array_len)

answer = category[outerRand][rand][0]

answer = re.sub('[A-Za-z0-9]+">',"",answer)

arrayAnswer = answer.split(" ")

counter = 0
currentHint = ""
wasCorrect = ""

def inAnswer():
    global arrayAnswer,answer,Guess,wasCorrect
    for i in range(len(arrayAnswer)):
        if(Guess.lower() == arrayAnswer[i].lower()):
            wasCorrect= "True"


def giveAnswer():
    global counter,currentHint,Guess,titleBOOL,header


    currentHint += category[outerRand][rand][1].split(".")[counter] + "."


    if(titleBOOL=="True"):
        print("Category is:   "+header)
    else:
        print("Category is:   "+category[outerRand][0][0])
    
    print(currentHint)


    Guess = input("Take your Guess \n")


    inAnswer()
    if(wasCorrect=="True"):

        print("CORRECT!!!")
    else:

        counter += 1
        try:
            giveAnswer()
        except:
            Guess = ("No More Hints, Good Luck" + currentHint)
            inAnswer()
            if(wasCorrect=="True"):
                print("CORRECT!!!")
            else:
                print("ANSWER IS: \n\n"+answer+"\n\n")




giveAnswer()


input()

#try:

    
        





#except:
 #   print(category[outerRand][rand][1].split()[:10])




