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
        if self.returns:
            self.returns = " ".join(str(self.returns).replace("\n", "").split())
            self.returns = "\n\t * @return " + str(self.returns)
        if self.return_type.find("private") == -1:
            self.return_type = "public " + self.return_type


        return str(self.comments) + ReverseDoc.parameter_print(self.parameters) + self.returns + \
               "\n\t */\n" + "\t" + self.return_type + " " + self.name + " {" + "\n\t\t" + \
               "//TODO Add method body for " + self.name + "\n\t" + "}\n\n"


def find_methods_details(methods_list, soup):
    """
    method find_methods_details

    Adds comments from the method details area of the javadocs to the methods

    Arguments:
        methods_list - list of all of the methods
    """
    for method in methods_list:
        method_details = soup.find("a", {"name": re.compile(method.name.split("(")[0])})
        comment = method_details.findNext("div", {"class": "block"})
        if comment:
            method.comments = ReverseDoc.create_comment(str(comment.text), True)
        method_parameters = method_details.findNext("span", {"class": "paramLabel"})
        if method_parameters:
            parameter = method_parameters.parent.next_sibling.next_sibling
            parameters_list = list()
            while str(parameter).find("Returns:") == -1 and parameter:
                parameters_list.append([parameter.text.split("-", 1)[0].strip(),
                                        parameter.text.split("-", 1)[1].strip()])
                parameter = parameter.next_sibling.next_sibling
            method.parameters = parameters_list
        method_returns = method_details.findNext("span", {"class": "returnLabel"})
        if method_returns:
            method.returns = method_returns.findNext("dd").text

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