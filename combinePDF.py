#! python3

# pdfs must be in working directory

import PyPDF2

pdf1 = input('Enter pdf file no. 1 to combine: ')
pdf2 = input('Enter pdf file no. 2 to combine: ')

pdf1File = open(pdf1, 'rb')
pdf2File = open(pdf2, 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)
writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader1.numPages):
	page = reader1.getPage(pageNum)
	writer.addPage(page)

	
for pageNum in range(reader2.numPages):
	page = reader2.getPage(pageNum)
	writer.addPage(page)

output = input('Enter name of output file: ')
	
outputFile = open(output, 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()