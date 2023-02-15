import PyPDF2
import glob
import os
 
path = os.getcwd()
filelist = glob.glob(path + '/pdf/*.pdf')
 
merger = PyPDF2.PdfFileMerger()
 
for file in filelist:
    merger.append(file)
 
merger.write(os.path.join(path, 'join.pdf'))
merger.close()