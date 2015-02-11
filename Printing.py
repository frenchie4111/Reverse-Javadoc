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
        method_parameters = method_details.findNext("dl")
        method_parameters = method_parameters.find_all("span", {"class": "paramLabel"})
        method_returns = method_details.findNext("span", {"class": "returnLabel"})
        if method_parameters:
            for parameter in method_parameters:
                parameters_list = list()
                parameters_list.append([parameter.findNext("dd").text.split("-")[0].strip(),
                                        parameter.findNext("dd").text.split("-")[1].strip()])
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
                    current_method.return_type = table_code.text.strip().replace(u'\xa0', u' ')
                else:
                    current_method.name = table_code.text.strip().replace(u'\xa0', u' ')
            method_list.append(current_method)
    # print(method_list)
    find_methods_details(method_list, soup)
    return method_list


def ReverseDoc(html):
    """
    method ReverseDoc

    takes a pages html and prints out the class that's described on the page

    Arguments:
        html - the pages html
"""
    # my_class = written_class()
    soup = BeautifulSoup(html)
    find_methods(soup)


def main():
    # html_file = input("File to be reversed: ")
    htmlfile = "./tests/Dragster.html"
    with open(htmlfile) as f:
        htmltext = f.read()
        ReverseDoc(htmltext)
main()