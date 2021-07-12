import os 
import textract

PDFS_PATHS = ['pdf_files/']

pdfs=[]
for root in PDFS_PATHS:
    pdfs = pdfs + [os.path.join(root, file) for file in os.listdir(root)]

for pdf in pdfs:
    print(pdf)
    text = textract.process(pdf,encoding='UTF-8')
    text = text.decode("utf-8", "ignore")
    dirname = os.path.dirname(pdf)
    base_txt = os.path.join(dirname, "txt")
    if not os.path.exists(base_txt):
        os.mkdir(base_txt)
    basename = os.path.basename(pdf).replace(".pdf", ".txt")
    final_name = os.path.join(base_txt, basename)
    f = open(final_name, "w+")
    f.write(text)
    f.close()
    