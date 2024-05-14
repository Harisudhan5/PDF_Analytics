from pdf2docx import Converter
pdf = 'AADHAR.pdf'
docs = 'my.docx'
cv = Converter(pdf)
cv.convert(docs)