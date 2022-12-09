
import os,sys


fileName = sys.argv[0].split("/")[::-1][0].split(".")[1]

if (fileName == "py"):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
else:
    __location__ = os.getcwd()



itemCount = len((os.listdir(__location__+"\\data")))

items = os.listdir(__location__+"\\data")

for i in range(itemCount):

    with open(__location__+"\\data\\"+items[i],"r") as r:
        contents = r.read()


    with open(__location__+"\\data\\total.txt","a") as a:
        a.write(contents)


with open(__location__+"\\data\\total.txt","r") as r:
        contents = r.read()
        contents.replace("\n\n","\n")
        print(contents)
        
with open(__location__+"\\data\\total.txt","w") as w:
        w.write(contents)



