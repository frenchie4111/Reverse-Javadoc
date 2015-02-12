import ReverseDoc

class ClassName():

    def __init__(self):
        self.comments = ""
        self.public = True
        self.title = ""

    def __repr__(self):
        if self.public:
            class_type = "public"
        else:
            class_type = "private"
        return str(self.comments) + "\n */\n" + str(self.title)



def find_class_name(soup):
    """
    method find_class_name

    finds a returns the name of the class on the page
"""
    my_class = ClassName()
    print(soup.find("pre").text)
    my_class.title = str(soup.find("pre").text).split('\n')[0]
    my_class.comments = ReverseDoc.create_comment(str(soup.find("div", {"class": "block"}).text), False)
    return my_class