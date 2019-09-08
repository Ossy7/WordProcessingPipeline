#A text processing pipeline
#-*- coding: utf-8 -*-
import re
import os
import sys
from textblob import Word
__version__ = "1.0.1"


def processTextFile(text_file):
    '''This functions cleans words espcially those containing unicode strings'''
    if os.path.isfile(text_file):
        if os.access(text_file, os.R_OK):
            txtFile = open(text_file, 'rb')
            reader = txtFile.read()
            cleaner = str(reader)
            cleaner = cleaner.lower()
            #remove unicode characters
            cleaner = re.sub(r'(\\u[0-9A-Fa-f]+)',r'', cleaner)
            cleaner = re.sub(r'[^\x00-\x7f]',r'', cleaner)

            
            cleaner = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', cleaner)
            cleaner = re.sub('@[^\s]+', 'AT_POSTER', cleaner)

            cleaner = re.sub('[\s]+', ' ', cleaner)
            cleaner = re.sub('[\n]+', ' ', cleaner)

            #Remove  white spaces
            cleaner = re.sub(r'[^\w]', ' ', cleaner)

            #remove hashtags
            cleaner = re.sub(r'#([^+s]+)', r'\1', cleaner)
            cleaner = re.sub(r'#([^\s]+)', r'\1', cleaner)

            cleaner = cleaner.replace(':)', '')
            cleaner = cleaner.replace(':(','')
            cleaner = ''.join([word for word in cleaner if not word.isdigit()])
            cleaner = re.sub(r"(\!)\1+", ' ', cleaner)
            cleaner = re.sub(r"(\?)\1+", ' ', cleaner)

            cleaner = re.sub("(\.)\+", ' ', cleaner)

            #lemmanitazion
            cleaner = " ".join([Word(i).lemmatize() for i in cleaner.split()])

            #Remove emoticons
            cleaner = re.sub(':\)|;\)|:-\)|\(-:|:-D|=D|:P|xD|X-­p|\^\^|:-*|\^\.\^|\^\-\^|\^\_\^|\,-\)|\)-:|:\'\(|:\(|:-\(|:\S|T\.T|\.\_\.|:<|:-\S|:-<|\*\-\*|:O|=O|=\-O|O\.o|XO|O\_O|:-\@|=/|:/|X\-\(|>\.<|>=\(|D:', '', cleaner)            
            cleaner = cleaner.strip('\'"')
            cleaned_txt = cleaner
            return cleaned_txt
        
def OutputFile(word_content, outFile):
    Fwriter = open(outFile, 'w')
    Fwriter.write(word_content)
    Fwriter.close()

def main():
    if len(sys.argv) == 2:
        text_file = sys.argv[1]
        outFile = "Output" + sys.argv[1]
        word_processor = processTextFile(text_file)
        OutputFile(word_processor, outFile)
        print("[]* Done! Check your current working folder for the output file.")
    else:
        print("USEAGE: word_processor.py REQUIRES AN ARGUMENT: A TEXTFILE")
if __name__ == '__main__':
    main()
        
                             
            
            
            
            

            
            
                
