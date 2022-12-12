import random
from selenium import webdriver
import re
import os,sys
import time

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


for i in range(len(data)):
    tempCat = ""
    url = data[i]
    #url = "https://www.naqt.com/you-gotta-know/20th-century-paintings.html"

    driver = webdriver.Edge(executable_path="C:\\Users\\thepa\\Downloads\\msedgedriver.exe")

    # Opening the URL
    driver.get(url)
    
    # Getting current URL source code
    get_source = driver.page_source
    driver.close()
    driver.quit()

    if(get_source.__contains__('<footer>')):
        tempCat = get_source.split("<footer>",1)    

        tempCat[1] = ""

    get_source = "".join(tempCat)



    if(get_source.__contains__('<ul class="ygk">')):
        category = get_source.split('<ul class="ygk">')
    
    
    elif(get_source.__contains__('<dl class="ygk">')):
        
        category = get_source.split('<dl class="ygk">')
    else:
        print(url)
        break


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
        for ii in range(len(category[i])):
            category[i][ii] = category[i][ii].split("</",1)



    for i in range(len(category)):
        for ii in range(len(category[i])):
            for iii in range(len(category[i][ii])):
                category[i][ii][iii] = re.sub("<(?:[^>])*>","",category[i][ii][iii])
                category[i][ii][iii] = category[i][ii][iii].replace("\n","").replace("\t","").replace("\u2009","").replace("&nbsp"," ").replace("span>","").replace("i>","")

    for i in range(len(category)):
        for ii in range(len(category[i])):
            try:
                if(category[i][ii][0]==""):
                    
                    category[i].pop(ii)
            except:
                if(category[i][0]==""):
                    
                    category.pop(i)

    
    print(category)
    with open (__location__+"\\data\\"+url.replace("https://www.naqt.com/you-gotta-know/","").replace(".html","")+".txt", "w") as f:
        for i in range(len(category)):
            for ii in range(len(category[i])):
                tempText = str(category[i][ii]).replace("-",";").encode("ascii","ignore")
                tempText = tempText.decode()

                f.write(tempText+"\n")