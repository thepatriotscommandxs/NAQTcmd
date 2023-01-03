import os,sys,re,PyPDF2

fileName = sys.argv[0].split("/")[::-1][0].split(".")[1]

if (fileName == "py"):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
else:
    __location__ = os.getcwd()

itemCount = len((os.listdir(__location__+"\\data")))

items = os.listdir(__location__+"\\data")

hint = []
power = []
answer = []
fulltext=''

# Open the PDF file in binary mode
with open(__location__+"\\data\\"+items[0], 'rb') as file:
    # Create a PDF object
    pdf = PyPDF2.PdfFileReader(file)

    # Get the number of pages in the PDF
    num_pages = pdf.getNumPages()

    # Iterate over each page
    for page_num in range(num_pages):
        # Get the page object
        page = pdf.getPage(page_num)

        # Extract the text from the page
        text = page.extractText()

        # Print the text


        fulltext += text
        
fulltext = fulltext.replace("\n","")
print(fulltext)
for i in range(len(fulltext)):
    try:
        fulltext[i] = fulltext[i].split(". ",1)[1]
        fulltext[i] = re.sub("\[(?:[^]])*\]","",fulltext[i])
        fulltext[i] = fulltext[i].replace("\n","")

        power.append(fulltext[i].split(". ",1)[0])
        hint.append(fulltext[i].split(". ",1)[1])
    except:
        pass

for i in range(len(hint)):
    answer.append(hint[i].split("ANSWER: ")[1])

for i in range(len(hint)):
    hint[i] = hint[i].split("ANSWER: ")[0]
    

for i in range(len(answer)):
    answer[i] = re.sub("\((?:[^)])*\)","",answer[i])

for i in range(len(answer)):
    try:
        with open(__location__+"\\set.txt","a", encoding="utf-8") as f:
            f.write("['"+answer[i]+"', '"+power[i]+" || "+hint[i]+"']"+"\n")
            f.close()
    except:
        break