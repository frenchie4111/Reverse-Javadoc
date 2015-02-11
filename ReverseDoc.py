#!/usr/bin/python3
from bs4 import BeautifulSoup
import re


class Comment():
    """
    class comment

    comment stores a comment for later printing

    slots:
        comment_type - The type of comment. Either "line" or "block"
        comment_lines - The lines of the comment. If comment_type==line then comment_lines should only have one index
"""

    def __init__(self, indent):
        self.indent = indent
        self.comment_lines = list()


    def __repr__(self):
        """
        method __repr__(self)

        if comment_type is "block" returns comment string in format:
            /**
             * self.comment_lines
             */
        if comment_type is "line" returns comment string in format:
            # self.comment_lines[0]
        """
        if self.indent:
            new_str = "\t/**\n"
            for comment_line in self.comment_lines:
                new_str += "\t * " + comment_line + "\n"
            # new_str += "\t */\n"
        else:
            new_str = "/**\n"
            for comment_line in self.comment_lines:
                new_str += " * " + comment_line + "\n"
            # new_str += " */\n"
        return new_str


class ClassName():
    def __init__(self):
        self.comments = ""
        # self.comments.header = True
        self.public = True
        self.title = ""

    def __repr__(self):
        if self.public:
            class_type = "public"
        else:
            class_type = "private"
        return str(self.comments) + " */\n" + class_type + " " + str(self.title)


class Method():
    """
    class method

    Method stores information about a particular method for later printing

    slots:
        comments - the comments from the javadoc about the method
        return_type - the type it returns
        method_name - the name of the method
"""

    def __init__(self):
        self.comments = ""
        # self.instance_type = ""
        self.name = ""
        self.return_type = ""
        self.sig = ""
        self.parameters = ""
        self.returns = ""


    def __repr__(self):
        """
        method __repr__(self)

        Returns the method text in this format:
        /**
         * self.comments
         */
         public self.return_type self.name {
            //Body
        }
        """
        # if self.public:
        # class_type = "public"
        # else:
        # class_type = "private"
        if self.return_type.find("private") == -1:
            self.return_type = "public " + self.return_type

        return str(self.comments) + "\t */\n" + "\t" + self.return_type + " " + self.name + \
               " {" + "\n\t\t" + "//TODO Add method body for " + self.name + "\n\t" + "}\n\n"

class Constructor():
    def __init__(self):
        self.sig = ""
        self.comments = ""
        self.parameters = list()

    def __repr__(self):
        return str(self.comments) + parameter_print(self.parameters) + "\t */\n" + "\t" + self.sig

class StaticField():
    """
    class static_field

    Stores a single static field of a class for later printing

    slots:
        comment - the comments from the javadoc about the method
        instance_type - the type of the static variable
        name - the name of the variable
"""

    def __init__(self):
        self.comments = ""
        # self.comments.header = False
        self.instance_type = ""
        self.name = ""


    def __repr__(self):
        """
        method __repr__(self)

        Returns the field as a string in this format:
        //comment
        self.instance_type self.name
    """
        return str(self.comments) + "\t */\n "+ "\t" + self.instance_type + " " + self.name + ";\n\n"


class WrittenClass(object):
    """
    class writen_class

    Stores class for later printing

    slots:
        head_text - the name of the method along with what it implements and extends
        methods - a python list filled with type method used to store the methods of this class
        fields - a python list filled with type fields used to store the static fields of this class
    """

    def __init__(self):
        self.head_text = ""
        self.methods = list()
        self.fields = list()
        self.constructor = ""


    def __str__(self):
        """
        method __repr__(self)

        Returns the class as a string in the format:
        class self.head_text + {
            str_list( self.fields )

            str_list( self.methods )
        }
    """
        return "" + str(self.head_text) + " {\n\n" + str_list(self.fields) + "\n\n" + str_list(self.methods) + "\n}"

def parameter_print(parameter_list):
    new_list = list()
    for parameter in parameter_list:
        new_list.append("\t * @param " + parameter[0] + parameter[1] + "\n")
    return str_list(new_list)

def str_list(pyList):
    """
    method str_list

    Return a string containing the str( ) of the items in the given pyList

    Arguments:
        pyList - python list to be converted to string
"""
    new_str = ""
    for list_item in pyList:
        new_str += str(list_item)
    return new_str


def create_comment(comment_text, indent):
    """
    method create_comment

    Creates a comment object from a given string

    Arguments:
        comment_text - the text to be in the comment
"""
    new_comment = Comment(indent)

    for line in comment_text.split("\n"):
        new_comment.comment_lines.append(str(line).replace("Returns:", "@return "))

    return new_comment



def find_methods_details(methods_list, soup):
    """
    method find_methods_details

    Adds comments from the method details area of the javadocs to the methods

    Arguments:
        methods_list - list of all of the methods
    """
    for method in methods_list:
        method_details = soup.find("a", {"name": re.compile(method.name.split("(")[0])})
        method.comments = create_comment(str(method_details.findNext("div", {"class": "block"}).text), True)
        # method_parameters = method_details.findNext("dl")
        method_parameters = method_parameters.findNext("span", {"class": "paramLabel"})
        method_returns = method_details.findNext("span", {"class": "returnLabel"})
        if method_parameters: #.findNext("span", {"class": "paramLabel"}):
            for parameter in method_parameters.find_all("dd"):
                parameters_list = list()
                print(parameter.text)
                parameters_list.append([parameter.text.split("-", 1)[0].strip(),
                                        parameter.text.split("-", 1)[1].strip()])
            method.parameters = parameters_list
        if method_returns:
            method.returns = method_returns.findNext("dd").text

def find_methods(soup):
    """
    method find_methods

    Finds all of the methods and then all of their comments and returns a list containing them
    """
    method_list = list()
    summary = soup.find("a", {"name": "method.summary"}, recursive="true").findNext("table")
    for table_row in summary.find_all("tr"):
        if table_row.text.strip() != "Modifier and Type\nMethod and Description":
            current_method = Method()
            for table_code in table_row.find_all("code", recursive="true"):
                if current_method.return_type == "":
                    current_method.return_type = str(table_code.text).strip()
                else:
                    current_method.name = " ".join(str(table_code.text).replace("\n", "").split())
            method_list.append(current_method)
    find_methods_details(method_list, soup)
    return method_list


def find_fields_details(fields_list, soup):
    for field in fields_list:
        field_details = soup.find("a", {"name": field.name})
        field.comments = create_comment(str(field_details.findNext("div", {"class": "block"}).text), True)



def find_fields(soup):
    """
    method find_fields

    Finds all of the fields and returns them as a python list of type static_field
    """
    fields_list = list()
    field_summary = soup.find("a", {"name": "field.summary"}, recursive="true")
    if field_summary:
        for table_row in field_summary.findNext("table").find_all("tr", recursive="true"):
            if table_row.text.strip() != "Modifier and Type\nField and Description":
                new_field = StaticField()
                for table_code in table_row.find_all("code", recursive="true"):
                    if new_field.instance_type == "":
                        new_field.instance_type = str(table_code.text)
                    else:
                        new_field.name = str(table_code.text)
                fields_list.append(new_field)
        find_fields_details(fields_list, soup)
    return fields_list


def find_constructor(soup):
    constructor = soup.find("a", {"name": "constructor.detail"}, recursive="true")
    if constructor:
        new_constructor = Constructor()
        new_constructor.sig = " ".join(str(constructor.findNext("pre").text).replace("\n", "").split())
        constructor.findNext("dl").find_all()
        constructor_parameters = constructor.findNext("dl")
        if constructor_parameters:
            for parameter in constructor_parameters.find_all("dd"):
                parameters_list = list()
                parameters_list.append([parameter.text.split("-", 1)[0].strip(),
                                        parameter.text.split("-", 1)[1].strip()])
            new_constructor.parameters = parameters_list
        return new_constructor

def str_list(pyList):
    """
    method str_list

    Return a string containing the str( ) of the items in the given pyList

    Arguments:
        pyList - python list to be converted to string
"""
    new_str = ""
    for list_item in pyList:
        new_str += str(list_item)
    return new_str


def find_class_name(soup):
    """
    method find_class_name

    finds a returns the name of the class on the page
"""
    my_class = ClassName()
    class_header = str(soup.find("pre").text).split('\n')[0].split()
    my_class.title = class_header[-1]
    if class_header[0] == "private":
        my_class.public = False
    my_class.comments = create_comment(str(soup.find("div", {"class": "block"}).text), False)
    return my_class


def ReverseDoc(html):
    """
    method ReverseDoc

    takes a pages html and prints out the class that's described on the page

    Arguments:
        html - the pages html
"""
    my_class = WrittenClass()
    soup = BeautifulSoup(html)
    my_class.head_text = find_class_name(soup)
    my_class.fields = find_fields(soup)
    my_class.methods = find_methods(soup)
    my_class.constructor = find_constructor(soup)
    return my_class


def main():
    # html_file = input("File to be reversed: ")
    # htmlfile = "./tests/Dragster.html"
    htmlfile = "./tests/Dragster.html"
    with open(htmlfile) as f:
        htmltext = f.read()
    java = ReverseDoc(htmltext)
    # print(str(java))
    javaTitle = java.head_text.title
    with open(javaTitle + ".java", "w") as f:
        f.write(str(java))
        # pass
        # print(java)


if (__name__ == '__main__'):
    main()
