from bs4 import BeautifulSoup

def clean_string(string):
    """
    method clean_string

    Cleans a string of unicode characters and newlines

    Arguments:
        string - string to be cleaned and returned
"""
    return string.strip().replace(u'\xa0', u' ')

def ReverseDoc(html):
    """
    method ReverseDoc

    takes a pages html and prints out the class that's described on the page

    Arguments:
        html - the pages html
"""
    # my_class = written_class()
    soup = BeautifulSoup(html)
    print(str(soup.find("a", {"name": "field.detail"}, recursive="true")))


def main():
    # html_file = input("File to be reversed: ")
    htmlfile = "./tests/Dragster.html"
    with open(htmlfile) as f:
        htmltext = f.read()
        ReverseDoc(htmltext)
main()