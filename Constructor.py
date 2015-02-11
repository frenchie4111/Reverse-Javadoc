import ReverseDoc

class Constructor():
    def __init__(self):
        self.sig = ""
        self.comments = ""
        self.parameters = list()
        self.body = list()

    def __repr__(self):
        if self.parameters:
            for parameter in self.parameters:
                self.body.append("\t\tself." + parameter[0] + " = " + parameter[0] + "\n")
        else:
            self.body = ""
        return str(self.comments) + ReverseDoc.parameter_print(self.parameters) + "\n\t */\n" + "\t" + self.sig + " {" \
               + "\n" + ReverseDoc.str_list(self.body) + "\n\t} \n\n"

def find_constructor(soup):
    constructor = soup.find("a", {"name": "constructor.detail"}, recursive="true")
    if constructor:
        new_constructor = Constructor()
        new_constructor.sig = " ".join(str(constructor.findNext("pre").text).replace("\n", "").split())
        new_constructor.comments = ReverseDoc.create_comment(str(constructor.findNext("div", {"class": "block"}).text), True)
        constructor_parameters = constructor.findNext("dl")
        if constructor_parameters:
            parameters_list = list()
            for parameter in constructor_parameters.find_all("dd"):
                parameters_list.append([parameter.text.split("-", 1)[0].strip(),
                                        parameter.text.split("-", 1)[1].strip()])
            new_constructor.parameters = parameters_list
        return new_constructor