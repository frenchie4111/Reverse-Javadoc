#!/usr/bin/python2
import sys
from bs4 import BeautifulSoup

"""
    class comment

    comment stores a comment for later printing
    
    slots:
        comment_type - The type of comment. Either "line" or "block"
        comment_lines - The lines of the comment. If comment_type==line then comment_lines should only have one index
"""
class comment:
    __slots__ = ("comment_type", "comment_lines")

    def __init__(self):
        self.comment_type = ""
        self.comment_lines = list()

    """
        method __str__(self)

        if comment_type is "block" returns comment string in format:
            /**
             * self.comment_lines
             */
        if comment_type is "line" reutrns comment string in format:
            # self.comment_lines[0]
    """
    def __str__(self):
        if (self.comment_type == "block"):
            new_str = "\t/**\n"
            for comment_line in self.comment_lines:
                new_str += "\t * " + comment_line + "\n"
            new_str += "\t */\n"
            return new_str
        if (self.comment_type == "line"):
            new_str = "\t# " + self.comment_lines[0];
        return ""

"""
    class method

    Method stores information about a particular method for later printing

    slots:
        comments - the comments from the javadoc about the method
        return_type - the type it returns
        method_name - the name of the method
"""
class method:
    __slots__ = ("comments", "return_type", "method_name")

    def __init__(self):
        self.comments = comment()
        self.return_type = ""
        self.method_name = ""

    """
        method __str__(self)

        Returns the method text in this format:
        /**
         * self.comments
         */
         public self.return_type self.method_name {
            //Body
        }
    """        
    def __str__(self):
       return str( self.comments ) + "\tpublic " + self.return_type + " " + self.method_name + " {" + "\n\t\t" + "//Body" + "\n\t" + "}\n\n"

"""
    class static_field

    Stores a single static field of a class for later printing
    
    slots:
        comment - the comments from the javadoc about the method
        instance_type - the type of the static variable
        name - the name of the variable
"""
class static_field:
    __slots__ = ("comment","instance_type","name")
 
    def __init__(self):
        self.instance_type = ""
        self.name = ""

    """
        method __str__(self)

        Returns the field as a string in this format:
        //comment
        self.instance_type self.name
    """
    def __str__(self):
        return "\tpublic " + self.instance_type + " " + self.name + "\n";

"""
    class writen_class

    Stores class for later printing

    slots:
        head_text - the name of the method along with what it implements and extends
        methods - a python list filled with type method used to store the methods of this class
        fields - a python list filled with type fields used to store the static fields of this class
"""
class written_class:
    __slots__ = ("comment","head_text", "methods", "fields")

    def __init__(self):
        self.head_text = ""
        self.methods = list()
        self.fields = list()
        self.comment = comment()

    """
        method __str__(self)

        Returns the class as a string in the format:
        class self.head_text + {
            str_list( self.fields )

            str_list( self.methods )
        }
    """
    def __str__(self):
        return "class " + self.head_text + " {\n\n" + str_list( self.fields ) + "\n\n" +  str_list( self.methods )  + "\n}"

"""
    method find_methods_summary

    Searches through the methods summary section of the JavaDoc and returns a list of methods without comments

    Arguments:
        html_summary - BeautifulSoup string of just the method summary area
"""
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

"""
    method find_methods_details

    Adds comments from the method details area of the javadocs to the methods

    Arguments:
        methods_list - list of all of the methods
        html - string of whole page
"""
def find_methods_details( methods_list, html ):
    soup = BeautifulSoup( html )
    for method in methods_list:
        method_details = soup.find("a", {"name":method.method_name}, recursive="true")
        if( method_details ):
            method.comments = create_comment( clean_string( method_details.findNext("dl").text ) )

"""
    method create_comment

    Creates a comment object from a given string

    Arguments:
        comment_text - the text to be in the comment
"""
def create_comment( comment_text ):
    new_comment = comment()

    new_comment.comment_type = "block"

    for line in comment_text.split("\n"):
        new_comment.comment_lines.append( clean_string( line ) )

    return new_comment

"""
    method find_methods

    Finds all of the methods and then all of their comments and returns a list containing them

    Arguments:
        html - string of the page source
"""
def find_methods( html ):
    methods_list = list()
    soup = BeautifulSoup( html )
    method_summary = soup.find("a", {"name":"method_summary"} ,recursive="true").findNext("table")
    if( method_summary ):
        method_list = find_methods_summary( method_summary )
        find_methods_details(method_list, html)    
    return method_list

"""
    method find_fields

    Finds all of the fields and returns them as a python list of type static_field

    Arguments:
        html - string of the page source
"""
def find_fields( html ):
    fields_list = list()
    soup = BeautifulSoup( html )
    field_summary = soup.find("a", {"name":"field_summary"}, recursive="true")
    if( field_summary ):
        for table_row in field_summary.findNext("table").find_all("tr", recursive="true"):
            if( table_row.text.strip() != "Field Summary" ):
                new_field = static_field()
                for table_code in table_row.find_all("code", recursive="true"):
                    if( new_field.instance_type == "" ):
                        new_field.instance_type = clean_string(table_code.text)
                    else:
                        new_field.name = clean_string(table_code.text)
                fields_list.append(new_field)
    return fields_list

"""
    method str_list

    Return a string containing the str( ) of the items in the given pyList

    Arguments:
        pyList - python list to be converted to string
"""
def str_list( pyList ):
    new_str = ""
    for list_item in pyList:
        new_str += str( list_item )
    return new_str

"""
    method clean_string

    Cleans a string of unicode characters and newlines

    Arguments:
        string - string to be cleaned and returned
"""
def clean_string( string ):
    return string.strip().replace(u'\xa0', u' ')

"""
    method find_class_name

    finds a returns the name of the class on the page

    Arguments:
        html - the pages html
"""
def find_class_name( html ):
    soup = BeautifulSoup( html )
    my_class = clean_string( soup.find("pre").text )
    return my_class

"""
    method ReverseDoc

    takes a pages html and prints out the class that's described on the page

    Arguments:
        html - the pages html
"""
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
