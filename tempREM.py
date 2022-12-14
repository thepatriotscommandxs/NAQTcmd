import os,sys
fileName = sys.argv[0].split("/")[::-1][0].split(".")[1]

if (fileName == "py"):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
else:
    __location__ = os.getcwd()

itemCount = len((os.listdir(__location__+"\\data")))

items = os.listdir(__location__+"\\data")

hint = []
power = []

with open(__location__+"\\rams.txt", "r",encoding="utf-8") as f:
    fulltext = f.readlines()
print(fulltext)

for i in range(len(fulltext)):
    hint.append(fulltext[i].split(". ",1)[1])


print(hint)


#for i in range(len(hint)):
#    hint[i] = re.sub("AN+[a-zA-Z0-9 ]{4,5}: ","",hint[i])
#    hint[i] = hint[i].replace("(*)","")
#    hint[i] = re.sub("\[(?:[^]])*\]","",hint[i])
#    power.append(hint[i].split(". ")[0])
#    split = hint[i].split(". ")[0]
#    hint[i] = hint[i].replace(split,"")
#
#for i in range(len(answer)):
#    answer[i] = answer[i].replace("ANSWER: ","")
#    answer[i] = answer[i].replace("<","")
#    answer[i] = re.sub("\[.*\]","",answer[i])
#    answer[i] = re.sub("\(.*\)","",answer[i])
#    answer[i] = re.sub("\((?:[^)])*\)","",answer[i])
#
#for i in range(len(answer)):
#    try:
#        with open(__location__+"\\set"+str(c)+".txt","a", encoding="utf-8") as f:
#            f.write("['"+answer[i]+"', '"+power[i]+"||"+hint[i]+"']"+"\n")
#            f.close()
#    except:
#        break