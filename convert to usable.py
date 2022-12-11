from PyPDF2 import PdfFileReader
import os,sys
import re

fileName = sys.argv[0].split("/")[::-1][0].split(".")[1]

if (fileName == "py"):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
else:
    __location__ = os.getcwd()

itemCount = len((os.listdir(__location__+"\\data")))

items = os.listdir(__location__+"\\data")
fulltext = ""

for i in range(itemCount):
    fulltext = ""
    # Open the PDF file for reading
    input_file = PdfFileReader(open(__location__+'\\data\\'+items[i], 'rb'))

    # Loop through each page of the input file
    for page in input_file.pages:
    # Extract the text from the page
        text = page.extractText()
        fulltext += text.replace("\n", " ")


    fulltext = re.sub("(?:[^~])*Tossups",">",fulltext)

    #firstPower = re.findall("1\.(?:[^>])*\(\*\)",fulltext)
    power = re.findall(">(?:[^>])*\(\*\)", fulltext)

    hint = re.findall("\(\*\)(?:[^>])+ANSWER: ", fulltext)

    answer = re.findall("ANSWER:(?:[^>])+<", fulltext)
    #print(fulltext)
    for i in range(len(power)):
        power[i] = re.sub("","",power[i])
        power[i] = power[i].replace("(*)","")
        power[i] = re.sub(">(?:[^.])*\.","",power[i])
        power[i] = re.sub("\((?:[^)])*\)","",power[i])
       


    for i in range(len(hint)):
        hint[i] = hint[i].replace("ANSWER: ","")
        hint[i] = hint[i].replace("(*)","")
        hint[i] = re.sub("\((?:[^)])*\)","",hint[i])

    for i in range(len(answer)):
        answer[i] = answer[i].replace("ANSWER: ","")
        answer[i] = answer[i].replace("<","")
        answer[i] = re.sub("\[.*\]","",answer[i])
        answer[i] = re.sub("\(.*\)","",answer[i])
        answer[i] = re.sub("\((?:[^)])*\)","",answer[i])

    for i in range(len(answer)):
        try:
            with open(__location__+"\\fullQs.txt","a", encoding="utf-8") as f:
                f.write("['"+answer[i]+"', '"+power[i]+"||"+hint[i]+"']"+"\n")
            print("['"+answer[i]+"', '"+power[i]+"||"+hint[i]+"']"+"\n")
        except:
            break