from bs4 import BeautifulSoup

def clean_string(string):
    """
    method clean_string

    Cleans a string of unicode characters and newlines

    Arguments:
        string - string to be cleaned and returned
"""
    return string.strip().replace(u'\xa0', u' ')

def find_fields(soup):
    field_summary = soup.find("a", {"name": "field.summary"}, recursive="true")
    if ( field_summary ):
        for table_row in field_summary.findNext("table").find_all("tr", recursive="true"):
            for table_code in table_row.find_all("code", recursive="true"):
                print(table_code.text)
                print()


def ReverseDoc(html):
    """
    method ReverseDoc

    takes a pages html and prints out the class that's described on the page

    Arguments:
        html - the pages html
"""
    # my_class = written_class()
    soup = BeautifulSoup(html)
    find_fields(soup)


def main():
    # html_file = input("File to be reversed: ")
    htmlfile = "./tests/Dragster.html"
    with open(htmlfile) as f:
        htmltext = f.read()
        ReverseDoc(htmltext)
main()