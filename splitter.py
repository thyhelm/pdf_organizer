from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import os

try:
    inputFile = open(str(sys.argv[1]), "rb")
    inputpdf = PdfFileReader(inputFile)

    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        if os.path.isfile("%s_doc.pdf" % str(i+1)):
            with open("b_%s_doc.pdf" % str(i+1), "wb") as outputStream:
                output.write(outputStream)
            print("Strona nr. "+str(i+1))
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