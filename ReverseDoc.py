#!/usr/bin/python2
import sys
from bs4 import BeautifulSoup

class comment:
    """
        comment stores a comment for later printing
        
        slots:
            comment_type - The type of comment. Either "line" or "block"
            comment_lines - The lines of the comment. If comment_type==line then comment_lines should only have one index
    """
    __slots__ = ("comment_type", "comment_lines")

    def __init__(self):
        self.comment_type = ""
        self.comment_lines = list()

    def __str__(self):
        if (self.comment_type == "block"):
            new_str = "\t/**\n"
            for comment_line in comment_lines:
                new_str += "\t * " + comment_line + "\n"
            new_str += "\t */\n"

class method:
    """
        Method stores information about a particular method for later printing

        slots:
            comments - the comments from the javadoc about the method
            return_type - the type it returns
            method_name - the name of the method
    """
    __slots__ = ("comments", "return_type", "method_name")

    def __init__(self):
        self.comments = ""
        self.return_type = ""
        self.method_name = ""

    def get_method_text(self):
        """
            Returns the method text in this format:
            /**
             * self.comments
             */
             public self.return_type self.method_name {
                //Body
            }
        """
        return self.comments + "\n\tpublic " + self.return_type + " " + self.method_name + " {" + "\n\t\t" + "//Body" + "\n\t" + "}"

    def __str__(self):
        return self.get_method_text()

class static_field:
    """
        Stores a single static field of a class for later printing
        
        slots:
            comment - the comments from the javadoc about the method
            instance_type - the type of the static variable
            name - the name of the variable
    """
    __slots__ = ("comment","instance_type","name")
 
    def __init__(self):
        self.instance_type = ""
        self.name = ""

    def __str__(self):
        """
            Returns the field in this format:
            //comment
            self.instance_type self.name
        """
        return "\t" + self.instance_type + " " + self.name + "\n";

class written_class:
    __slots__ = ("head_text", "methods", "fields")

    def __init__(self):
        self.head_text = ""
        self.methods = list()
        self.fields = list()

    def __str__(self):
        return "class " + self.head_text + " {\n\n" + print_fields( self.fields ) + "\n\n" +  print_methods( self.methods )  + "\n}"

def find_methods_summary( html_summary ):
    method_list = list()
    for table_row in html_summary.find_all("tr"):
        if( table_row.text.strip() != "Method Summary"):
            current_method = method()
            for table_code in table_row.find_all("code", recursive="true"):
                if( current_method.return_type == "" ):
                    current_method.return_type = table_code.text.strip().replace(u'\xa0', u' ')
                else:
                    current_method.method_name = table_code.text.strip().replace(u'\xa0', u' ')
            method_list.append(current_method)
    return method_list

def find_methods_details( methods_list, html_full ):
    pass

def find_methods( html ):
    methods_list = list()
    soup = BeautifulSoup( html )
    method_summary = soup.find("a", {"name":"method_summary"} ,recursive="true").findNext("table")
    method_list = find_methods_summary( method_summary )
    find_methods_details(methods_list, html)    
    return method_list

def find_fields( html ):
    fields_list = list()
    soup = BeautifulSoup( html )
    for table_row in soup.find("a", {"name":"field_summary"}, recursive="true").findNext("table").find_all("tr", recursive="true"):
        if( table_row.text.strip() != "Field Summary" ):
            new_field = static_field()
            for table_code in table_row.find_all("code", recursive="true"):
                if( new_field.instance_type == "" ):
                    new_field.instance_type = clean_string(table_code.text)
                else:
                    new_field.name = clean_string(table_code.text)
            fields_list.append(new_field)
    return fields_list

def print_methods( method_list ):
    new_str_methods = ""
    for method in method_list:
        new_str_methods += str( method )
    return new_str_methods

def print_fields( field_list ):
    new_str_fields = ""
    for field in field_list:
        new_str_fields += str( field )
    return new_str_fields

def clean_string( string ):
    return string.strip().replace(u'\xa0', u' ')

def find_class_name( html ):
    soup = BeautifulSoup( html )
    my_class = soup.find("pre").text.strip('\n').strip('java.lang.Object')
    return my_class

def ReverseDoc( html ):
    my_class = written_class()
    my_class.head_text = find_class_name( html )
    my_class.fields = find_fields( html )

    my_class.methods = find_methods( html )
    print str( my_class ) 
    

def main():
    input_html = sys.stdin.read()
    ReverseDoc( input_html )

if(__name__ == '__main__'):
    main()
