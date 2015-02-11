import ReverseDoc

class Constructor():
    def __init__(self):
        self.sig = ""
        self.comments = ""
        self.parameters = list()

    def __repr__(self):
        return str(self.comments) + parameter_print(self.parameters) + "\t */\n" + "\t" + self.sig

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