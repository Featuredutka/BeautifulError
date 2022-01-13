import glob, os
import xlrd
import pandas

SOURCE_FILE = ""

def main():
    os.chdir(os.getcwd())
    for file in glob.glob("*.txt"):
        SOURCE_FILE = file

    with open(SOURCE_FILE,'r', encoding='cp1251') as source: # Cyrillic encoding to handle Windows 
        text = source.readlines()
    source.close()
    
    # Strips the newline character
    for count, line in enumerate(text, start=1):
        print("Line{}: {}".format(count, line.strip()))

if __name__ == "__main__":
    main()