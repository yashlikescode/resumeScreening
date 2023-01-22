import docx2txt     # to convert docx files into text
import PyPDF2       # to convert pdf files into text
import os           # to read files from a folder/directory
import pandas as pd

def sort2list(list1, list2):
    zipped_pairs = zip(list2, list1)
    z = [x for _, x in sorted(zipped_pairs)]
    return z

keyfile = open('keywords.txt','r')
keyWords = keyfile.read()
keyWords = keyWords.lower()
keyfile.close()
keylist = list(keyWords.split(','))
keylen = len(keylist)

pathinp = r'.\inputFolder'
pathparent = r'..'
os.chdir(pathinp)

fileList = os.listdir()
fileScore = []
fileLen = len(fileList)

files = 0
indicator = 0
for fileName in fileList:
    files+=1
    if files%(fileLen//4) == 0:
        indicator+=25
        print("Processed {}%".format(indicator))

    keyfound = 0
    text=''
    try:
        resume = docx2txt.process(fileName)
        for i in resume:
                text+=i
    except:
        file = open(fileName,'rb')
        reader=PyPDF2.PdfReader(file)
        for pg in range(len(reader.pages)):
            page = reader.pages[pg]
            tex = page.extract_text()
            for i in tex:
                if type(i)==str:
                    text+=i
        file.close()

    text = text.lower()
    for ky in keylist:
        if text.find(ky) != -1:
            keyfound += 1
    fileScore.append(keyfound*100/keylen)

os.chdir(pathparent)

fileList = sort2list(fileList,fileScore)
fileScore.sort()

fileList.reverse()
fileScore.reverse()

df = pd.DataFrame({"File Names" : fileList, r"% Keywords Found" : fileScore})
df=df[df[r"% Keywords Found"]!=0]
df.to_csv("resumeResult.csv", index=False)
