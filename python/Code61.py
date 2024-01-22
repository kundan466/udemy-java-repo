# Import library
import PyPDF2

# Create a file object for a pdf file.
pdfFile = open("example.pdf", "rb")

# Create an object for reading a file.
pdfReader = PyPDF2.PdfFileReader(pdfFile)

# Get the number of pages in the pdf file.
numPages = pdfReader.numPages

# Create an object to get the text from page 0.
page = pdfReader.getPage(0)

# Get text from the created object.
text = page.extractText()

# Print the number of pages and text data.
print("Number of Pages:", numPages)

print("Text:\n"+text)

