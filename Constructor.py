import ReverseDoc


class Constructor():
    def __init__(self):
        self.sig = ""
        self.comments = ""
        self.parameters = list()
        self.body = list()

    def __repr__(self, interface):
        if self.parameters:
            for parameter in self.parameters:
                self.body.append("\t\tthis." + parameter[0] + " = " + parameter[0] + ";\n")
        else:
            self.body = ""
        if self.comments and self.parameters:
            header = str(self.comments) + ReverseDoc.parameter_print(self.parameters) + "\n\t */\n"
        elif self.comments:
            header = str(self.comments) + "\n\t */\n"
        else:
            header = ""
        if interface:
            return header + "\t" + self.sig + ";"

        return header + "\t" + self.sig + " {" \
               + "\n" + "\t\t//TODO Check for accuracy\n" + ReverseDoc.str_list(self.body, interface) + "\n\t} \n\n"


def find_constructor(soup):
    constructor = soup.find("a", {"name": "constructor.detail"}, recursive="true")
    if constructor:
        new_constructor = Constructor()
        new_constructor.sig = " ".join(str(constructor.findNext("pre").text).replace("\n", "").split())
        if str(new_constructor.sig).find("(") - str(new_constructor.sig).find(")") != -1 and constructor.findNext("div",
                                                                                                                  {
                                                                                                                      "class": "block"}):
            new_constructor.comments = ReverseDoc.create_comment(
                str(constructor.findNext("div", {"class": "block"}).text), True)
            constructor_parameters = constructor.find("span", {"class": "paramLabel"})
            if constructor_parameters:
                parameters_list = list()
                constructor_parameters = constructor_parameters.parent
                for parameter in constructor_parameters.find_all("dd"):
                    if parameter.find("code") is not None:
                        print(parameter)
                        parameters_list.append([parameter.text.split("-", 1)[0].strip(),
                                                parameter.text.split("-", 1)[1].strip()])
                new_constructor.parameters = parameters_list
        else:
            return None
        return new_constructor