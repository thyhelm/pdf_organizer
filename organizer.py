from PyPDF2 import PdfFileReader, PdfFileMerger
import sys
import os

try:
    output = PdfFileMerger()
    for i in range(len(sys.argv)-2):
        with open(str(sys.argv[i+2]), "rb") as f:
            inputFile = PdfFileReader(f)
            output.append(inputFile)
        print("Usuwam plik: "+str(sys.argv[i+2]))
        os.remove(str(sys.argv[i+2]))
    output.write(str(sys.argv[1]))
    print("Utworzono plik pdf o nazwie "+str(sys.argv[1]))

except Exception as e:
    print("Błąd zapisu - "+e)