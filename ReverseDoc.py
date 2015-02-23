#!/usr/bin/python3
from bs4 import BeautifulSoup
import sys
import ClassName
import Fields
import Method
import Constructor


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

        Doesn't close the comment to allow addition of parameters and returns

        post-condition: cursor is at end of comment line, no \n has been inserted
        """
        if self.indent:
            new_str = "\t/**\n"
            for comment_line in self.comment_lines:
                new_str += "\t * " + comment_line + "\n"
        else:
            new_str = "/**\n"
            for comment_line in self.comment_lines:
                new_str += " * " + comment_line + "\n"
        return new_str[:len(new_str) - 1]  # removes new line character from end to prevent gaps in comments


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
        self.package = ""
        self.head_text = ""
        self.methods = list()
        self.fields = list()
        self.constructor = ""


    def __str__(self, interface):
        """
        method __repr__(self)

        Returns the class as a string in the format:
        class self.head_text + {
            str_list( self.fields )

            str_list( self.methods )
        }
    """
        javaClass = ""
        if self.package:
            javaClass += "package " + str(self.package) + ";\n"
        if self.head_text:
            javaClass += str(self.head_text) + " {\n\n"
        if self.fields:
            javaClass += str_list_no_int(self.fields) + "\n\n"
        if self.constructor:
            javaClass += self.constructor.__repr__(interface) + "\n\n"
        if self.methods:
            javaClass += str_list(self.methods, interface)
        return javaClass + "\n}"


def parameter_print(parameters_in):
    """
    Takes a list of parameters and turns it into a single string (with line breaks)

    The first item in the list is the parameter name and the second is the description.
    pre-condition: cursor is at the end of the previous line
    post-condition: cursor is at the end of the previous line
    """
    parameters_out = ""
    for parameter in parameters_in:
        parameter[1] = " ".join(
            str(parameter[1]).replace("\n", "").split())  # removes new line characters from a parameter's description
        parameters_out += "\t * @param " + parameter[0] + " " + parameter[1] + "\n"

    if parameters_out:
        return "\n" + parameters_out[:len(parameters_out) - 1]  # starts a new line for the first parameter to print
                                                                # removes last new line so cursor is at end of last line
    else:
        return ""


def str_list_no_int(pyList):
    new_str = ""
    for list_item in pyList:
        new_str += str(list_item.__repr__())
    return new_str


def str_list(pyList, interface):
    """
    method str_list

    Return a string containing the str( ) of the items in the given pyList

    Arguments:
        pyList - python list to be converted to string
"""
    new_str = ""
    for list_item in pyList:
        new_str += str(list_item.__repr__(interface))
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


def find_package(soup):
    package = soup.find("div", {"class": "subTitle"})
    if package:
        return package.text


def ReverseDoc(html, location):
    """
    method ReverseDoc

    takes a pages html and prints out the class that's described on the page

    Arguments:
        html - the pages html
"""
    my_class = WrittenClass()
    soup = BeautifulSoup(html)
    my_class.package = find_package(soup)
    my_class.head_text = ClassName.find_class_name(soup)
    my_class.fields = Fields.find_fields(soup, location)
    my_class.methods = Method.find_methods(soup)
    my_class.constructor = Constructor.find_constructor(soup)
    return my_class


def main(htmlfile=''):
    htmlfile = input("Enter file name with path: ")
    interface = input("Is this an interface? (y/n) ")
    if interface.upper() == "YES" or "Y":
        interface = True
    else:
        interface = False
    with open(htmlfile) as f:
        htmltext = f.read()
    java = ReverseDoc(htmltext, interface)
    print(htmlfile.split(".h")[0] + ".java")
    with open(htmlfile.split(".h")[0] + ".java", "w") as f:
        f.write(str(java))


if __name__ == '__main__':
    main()
