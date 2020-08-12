from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2docx.main import parse
import sys
import os
import docx

try:
    inputFile = open(str(sys.argv[1]), "rb")
    inputpdf = PdfFileReader(inputFile)

    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        if os.path.isfile("%s_doc.pdf" % str(i+1)):
            pdf_file = "b_%s_doc.pdf" % str(i+1)
            with open(pdf_file, "wb") as outputStream:
                output.write(outputStream)
            print("Strona nr. "+str(i+1))
            docx_file = 'test.docx'
            parse(pdf_file, docx_file, start=0, end=1)
            doc = docx.Document(docx_file)
            if len(doc.paragraphs) == 0:
                os.remove(pdf_file)
                os.remove(docx_file)
                print("Pusta strona - usuwam")
            else:
                os.remove(docx_file)
        else:
            with open("%s_doc.pdf" % str(i+1), "wb") as outputStream:
                output.write(outputStream)
            print("Strona nr. "+str(i+1))
    print("Podzielono pdf na "+str(inputpdf.numPages)+" plików.")
    print("Usunięto plik: "+str(sys.argv[1]))
    inputFile.close()
    os.remove(str(sys.argv[1]))
except Exception as e:
    print("Bląd dzielenia pliku pdf-"+e)