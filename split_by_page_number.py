from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
import os


try:
    with open("input.pdf", 'rb') as infile:
        reader = PdfFileReader(infile)
        writer = PdfFileWriter()
        for page in range(reader.numPages):
            if page >=226: 
                writer.addPage(reader.getPage(page))

        with open('output.pdf', 'wb') as outfile:
            writer.write(outfile)

    print("Done!")

except Exception as e:
    print(e)
