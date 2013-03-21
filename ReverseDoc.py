import sys
from bs4 import BeautifulSoup

class method:
    __slots__ = ("comments", "return_type", "method_name")

    def __init__(self):
        self.comments = ""
        self.return_type = ""
        self.method_name = ""

    def get_method_text(self):
        #Returns the text of the method
        return self.comments + "\n\tpublic " + self.return_type + " " + self.method_name + "() {" + "\n\t\t" + "//Body" + "\n\t" + "}"

    def __str__(self):
        return self.get_method_text()

def find_methods_summary( html_summary ):
    method_list = list()
    for table_row in html_summary.find_all("tr"):
        if( table_row.text.strip() != "Method Summary"):
            current_method = method()
            for table_code in table_row.find_all("code", recursive="true"):
                if( current_method.method_name == "" ):
                    current_method.method_name = table_code.text.strip()
                else:
                    current_method.return_type = table_code.text.strip()
            method_list.append(current_method)
    return method_list

def find_methods_details( methods_list, html_full ):
    

def find_methods( html ):
    methods_list = list()
    soup = BeautifulSoup( html )
    method_summary = soup.find("a", {"name":"method_summary"} ,recursive="true").findNext("table")
    method_list = find_methods_summary( method_summary )
    print_methods( method_list )

def print_methods( method_list ):
    for method in method_list:
        print str( method )

def main():
    input_html = sys.stdin.read()
    find_methods( input_html )

if(__name__ == '__main__'):
    main()
