import docx2txt
import PyPDF2
import os


path = r'C:\Users\kmrya\Desktop\screeningResume\inputFolder'
os.chdir(path)
 
fileName = 'selected4.pdf'
for fileName in os.listdir():
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
    for i in text:
        try:
            print(i,end='')
        except:
            print("",end='')

