#!/usr/bin/python3
from bs4 import BeautifulSoup



class comment():
    """
    class comment

    comment stores a comment for later printing

    slots:
        comment_type - The type of comment. Either "line" or "block"
        comment_lines - The lines of the comment. If comment_type==line then comment_lines should only have one index
"""
    __slots__ = ("comment_type", "comment_lines")

    def __init__(self):
        self.comment_type = ""
        self.comment_lines = list()


    def __repr__(self):
        """
        method __repr__(self)

        if comment_type is "block" returns comment string in format:
            /**
             * self.comment_lines
             */
        if comment_type is "line" reutrns comment string in format:
            # self.comment_lines[0]
        """
        if (self.comment_type == "block"):
            new_str = "\t/**\n"
            for comment_line in self.comment_lines:
                new_str += "\t * " + comment_line + "\n"
            new_str += "\t */\n"
            return new_str
        if (self.comment_type == "line"):
            new_str = "\t# " + self.comment_lines[0];
        return ""


class class_name():

    def __init__(self):
        self.comments = comment()
        self.public = True
        self.title = ""

    def __repr__(self):
        if self.public:
            class_type = "\tpublic"
        else:
            class_type = "\tprivate"
        return str(self.comments) + class_type + " " + str(self.title)


class method():
    """
    class method

    Method stores information about a particular method for later printing

    slots:
        comments - the comments from the javadoc about the method
        return_type - the type it returns
        method_name - the name of the method
"""
    __slots__ = ("comments", "return_type", "name")

    def __init__(self):
        self.comments = comment()
        self.return_type = ""
        self.name = ""


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
        return str(
            self.comments) + "\tpublic " + self.return_type + " " + self.name + " {" + "\n\t\t" + "//TODO Add method body for " + self.name + "\n\t" + "}\n\n"


class static_field():
    """
    class static_field

    Stores a single static field of a class for later printing

    slots:
        comment - the comments from the javadoc about the method
        instance_type - the type of the static variable
        name - the name of the variable
"""
    __slots__ = ("comments", "instance_type", "name")

    def __init__(self):
        self.comments = comment()
        self.instance_type = ""
        self.name = ""


    def __repr__(self):
        """
        method __repr__(self)

        Returns the field as a string in this format:
        //comment
        self.instance_type self.name
    """
        return str(self.comments) + self.instance_type + " " + self.name + "\n";


class written_class(object):
    """
    class writen_class

    Stores class for later printing

    slots:
        head_text - the name of the method along with what it implements and extends
        methods - a python list filled with type method used to store the methods of this class
        fields - a python list filled with type fields used to store the static fields of this class
    """
    __slots__ = ("head_text", "methods", "fields")

    def __init__(self):
        self.head_text = ""
        self.methods = list()
        self.fields = list()


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


def find_methods_summary(html_summary):
    """
    method find_methods_summary

    Searches through the methods summary section of the JavaDoc and returns a list of methods without comments

    Arguments:
        html_summary - BeautifulSoup string of just the method summary area
"""
    method_list = list()
    for table_row in html_summary.find_all("tr"):
        if table_row.text.strip() != "Method Summary":
            current_method = method()
            for table_code in table_row.find_all("code", recursive="true"):
                if ( current_method.return_type == "" ):
                    current_method.return_type = table_code.text.strip().replace(u'\xa0', u' ')
                else:
                    current_method.name = table_code.text.strip().replace(u'\xa0', u' ')
            method_list.append(current_method)
    return method_list


def find_methods_details(methods_list, soup):
    """
    method find_methods_details

    Adds comments from the method details area of the javadocs to the methods

    Arguments:
        methods_list - list of all of the methods
    """
    for method in methods_list:
        method_details = soup.find("a", {"name": method.name}, recursive="true")
        if method_details:
            method.comments = create_comment(str(method_details.findNext("dl").text))


def create_comment(comment_text):
    """
    method create_comment

    Creates a comment object from a given string

    Arguments:
        comment_text - the text to be in the comment
"""
    new_comment = comment()

    new_comment.comment_type = "block"

    for line in comment_text.split("\n"):
        new_comment.comment_lines.append(str(line).replace("Returns:", "@return: "))

    return new_comment


def find_methods(soup):
    """
    method find_methods

    Finds all of the methods and then all of their comments and returns a list containing them
    """
    methods_list = list()
    method.summary = soup.find("a", {"name": "method.summary"}, recursive="true").findNext("table")
    if method.summary:
        method_list = find_methods_summary(method.summary)
        find_methods_details(method_list, soup)
    return method_list


def find_fields(soup):
    """
    method find_fields

    Finds all of the fields and returns them as a python list of type static_field
    """
    fields_list = list()
    field_summary = soup.find("a", {"name": "field.summary"}, recursive="true")
    if ( field_summary ):
        for table_row in field_summary.findNext("table").find_all("tr", recursive="true"):
            if ( table_row.text.strip() != "Field Summary" ):
                new_field = static_field()
                for table_code in table_row.find_all("code", recursive="true"):
                    print(table_code)
                    if ( new_field.instance_type == "" ):
                        new_field.instance_type = str(table_code.text)
                    else:
                        new_field.name = str(table_code.text)

                fields_list.append(new_field)
    find_methods_details(fields_list, soup)
    return fields_list


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


# def clean_string(string):
# """
#     method clean_string
#
#     Cleans a string of unicode characters and newlines
#
#     Arguments:
#         string - string to be cleaned and returned
# """
#     return string.strip().replace(u'\xa0', u' ')


def find_class_name(soup):
    """
    method find_class_name

    finds a returns the name of the class on the page
"""
    my_class = class_name()
    class_header = str(soup.find("pre").text).split('\n')[0].split()
    my_class.title = class_header[-1]
    if class_header[0] == "private":
        my_class.public = False
    my_class.comments = create_comment(str(soup.find("div", {"class": "block"}).text))
    return my_class


def ReverseDoc(html):
    """
    method ReverseDoc

    takes a pages html and prints out the class that's described on the page

    Arguments:
        html - the pages html
"""
    my_class = written_class()
    soup = BeautifulSoup(html)
    my_class.head_text = find_class_name(soup)
    my_class.fields = find_fields(soup)
    my_class.methods = find_methods(soup)
    return my_class


def main():
    # html_file = input("File to be reversed: ")
    htmlfile = "./tests/Dragster.html"
    # htmlfile = urllib.urlopen("/home/andrew/temp/Reverse-Javadoc/tests/Dragster.html")
    with open(htmlfile) as f:
        htmltext = f.read()
    java = ReverseDoc(htmltext)
    # print(str(java))
    javaTitle = java.head_text.title
    with open(javaTitle + ".java", "w") as f:
        f.write(str(java))
        pass
        # print(java)


if (__name__ == '__main__'):
    main()
