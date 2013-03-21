import sys
from bs4 import BeautifulSoup

class method:
    __slots__ = ("comments", "return_type", "method_name")

    def get_method_text(self):
        #Returns the text of the method
        return self.comments + "\n\tpublic" + self.return_type + self.method_name + "() {" + "\n" + "//Body" + "\n" + "}"

def find_methods_summary( html_summary ):
    print html_summary.prettify()
    for table_row in html_summary.find_all("tr"):
        print "ROW"

def find_methods( html ):
    methods_list = list()
    soup = BeautifulSoup( html )
    method_summary = soup.find("a", {"name":"method_summary"} ,recursive="true").findNext("table")
    find_methods_summary( method_summary )
    #first_method_return = method_summary.findNext("tr").findNext("tr").find("td").find("code").text.strip()

def main():
    print( "Hello, World" )
    input_html = sys.stdin.read()
    find_methods( input_html )

if(__name__ == '__main__'):
    main()
