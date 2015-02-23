import re
import ReverseDoc


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
        self.overrides = False
        self.method_body = ""


    def __repr__(self, interface):
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
        header = ""
        if self.comments:
            header += str(self.comments)
        if self.parameters:
            header += str(ReverseDoc.parameter_print(self.parameters))
        if self.returns:
            self.returns = " ".join(str(self.returns).replace("\n", "").split())
            self.returns = "\n\t * @return " + str(self.returns)
            header += self.returns
        if self.comments or self.parameters or self.returns:
            header += "\n\t */\n"
        if self.return_type.find("private") == -1 and self.return_type.find("protected") == -1:
            self.return_type = "public " + self.return_type
        if self.overrides:
            header += "\t@Override\n"
        if self.return_type.find("int") != -1:
            self.method_body = "\n\t\treturn 0;"
        if self.return_type.find("double") != -1:
            self.method_body = "\n\t\treturn 0.0;"
        if self.return_type.find("boolean") != -1:
            self.method_body = "\n\t\treturn False;"
        if self.return_type.find("String") != -1:
            self.method_body = '\n\t\treturn "";'
        if interface or self.return_type.find("abstract") != -1:
            return header + "\t" + self.return_type + " " + self.name + ";\n\n"

        return header + "\t" + self.return_type + " " + self.name + " {" + "\n\t\t" + \
               "//TODO Add method body for " + self.name + self.method_body + "\n\t" + "}\n\n"


def find_methods_details(methods_list, soup):
    """
    method find_methods_details

    Adds comments from the method details area of the javadocs to the methods

    Arguments:
        methods_list - list of all of the methods
    """
    for method in methods_list:
        method_details = soup.find("a", {"name": re.compile(method.name.split("(")[0])})
        method_details = method_details.findNext("ul")
        comment = method_details.find("div", {"class": "block"})
        if comment:
            method.comments = ReverseDoc.create_comment(str(comment.text), True)
        method_parameters = method_details.find("span", {"class": "paramLabel"})
        if method_parameters:
            parameter = method_parameters.parent.next_sibling.next_sibling
            parameters_list = list()
            while str(parameter).find("Returns:") == -1 and parameter:
                parameters_list.append([parameter.text.split("-", 1)[0].strip(),
                                        parameter.text.split("-", 1)[1].strip()])
                parameter = parameter.next_sibling.next_sibling
            method.parameters = parameters_list
        method_returns = method_details.find("span", {"class": "returnLabel"})
        if method_returns and method.return_type.find("void") == -1:
            method.returns = method_returns.findNext("dd").text
        override = method_details.find("span", {"class": "overrideSpecifyLabel"})
        if override and str(override.text) == "Overrides:":
            method.overrides = True


def find_methods(soup):
    """
    method find_methods

    Finds all of the methods and then all of their comments and returns a list containing them
    """
    method_list = list()
    summary = soup.find("a", {"name": "method.summary"}, recursive="true").findNext("table")
    if summary:
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