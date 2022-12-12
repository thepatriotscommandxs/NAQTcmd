import sys,os


fileName = sys.argv[0].split("/")[::-1][0].split(".")[1]

if (fileName == "py"):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
else:
    __location__ = os.getcwd()

itemCount = len((os.listdir(__location__+"\\converted")))

items = os.listdir(__location__+"\\converted")
fulltext = ""

for i in range(itemCount):
    with open(__location__+"\\converted\\"+items[i], "r",encoding="utf-8") as f:
        fulltext = f.read()


    with open(__location__+"\\total.txt","a",encoding="utf-8") as x:
        x.write(fulltext)
