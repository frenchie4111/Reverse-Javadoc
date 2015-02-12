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
        return new_str[:len(new_str) - 1]


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
        javaClass = str(self.head_text) + " {\n\n"
        if self.fields:
            javaClass += str(self.fields) + "\n\n"
        if self.constructor:
            javaClass += str(self.constructor) + "\n\n"
        if self.methods:
            javaClass += str_list(self.methods)
        return javaClass + "\n}"

def parameter_print(parameter_list):
    new_list = list()
    for parameter in parameter_list:
        parameter[1] = " ".join(str(parameter[1]).replace("\n", "").split())
        new_list.append("\t * @param " + parameter[0] + " " + parameter[1] + "\n")

    parameters = str_list(new_list)
    if parameters:
        return "\n" + parameters[:len(parameters) - 1]
    else:
        return ""

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




def ReverseDoc(html):
    """
    method ReverseDoc

    takes a pages html and prints out the class that's described on the page

    Arguments:
        html - the pages html
"""
    my_class = WrittenClass()
    soup = BeautifulSoup(html)
    my_class.head_text = ClassName.find_class_name(soup)
    my_class.fields = Fields.find_fields(soup)
    my_class.methods = Method.find_methods(soup)
    my_class.constructor = Constructor.find_constructor(soup)
    return my_class


def main():
    if len(sys.argv) > 1:
        htmlfile = sys.argv[1]
    else:
        htmlfile = input("Enter file name with path: ")
    with open(htmlfile) as f:
        htmltext = f.read()
    java = ReverseDoc(htmltext)
    print(htmlfile.split("/")[-1].split(".")[0])
    with open(htmlfile.split("/")[-1].split(".")[0] + ".java", "w") as f:
        f.write(str(java))
        # pass
        # print(java)


if (__name__ == '__main__'):
    main()
