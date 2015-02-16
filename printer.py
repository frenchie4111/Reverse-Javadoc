__author__ = 'andrew'

from bs4 import BeautifulSoup


def main():
    # printer = input("Webpage to print: ")
    printer = "./tests/overview-tree.html"
    with open(printer) as f:
        htmltext = f.read()
    soup = BeautifulSoup(htmltext)
    print(soup.prettify())



if __name__ == '__main__':
    main()