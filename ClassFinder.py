import ReverseDoc
import sys
from bs4 import BeautifulSoup


def findClasses(soup):


def main():
    if len(sys.argv) > 1:
        htmlfile = sys.argv[1]
    else:
        htmlfile = input("Enter file name with path: ")
    with open(htmlfile) as f:
        htmltext = f.read()
    soup = BeautifulSoup(htmltext)
    overview = findClasses(soup)





if __name__ =='__main__':
    main()