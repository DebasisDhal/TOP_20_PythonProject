import pyttsx3
import PyPDF2

file =open("Resume_.pdf",mode="rb")
pdf_reader = PyPDF2.PdfFileReader(file)
pages = pdf_reader.numPages
print(pages)

melo =pyttsx3.init()
page = pdf_reader.getPage(1)
text = page.extractText()
melo.say(text)
melo.runAndWait()