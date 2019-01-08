from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

def create_csv_file(input_path, output_path):
    text = convert_pdf_to_txt(input_path)
    idx = 0
    with open(output_path,'w') as file:
        for line in text.split("\n"):
            if line.strip():
                file.write(line)
                if idx % 2 == 0:
                    file.write(",")
                else:
                    file.write("\n")
                idx += 1


create_csv_file("submit_form_new_4.pdf", "submit_form_new_4.csv")

