import ReverseDoc

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
        return str(self.comments) + "\n */\n" + class_type + " " + str(self.title)



def find_class_name(soup):
    """
    method find_class_name

    finds a returns the name of the class on the page
"""
    my_class = ClassName()
    class_header = str(soup.find("pre").text).split('\n')[0].split()
    my_class.title = class_header[-1]
    if class_header[0] == "private":
        my_class.public = False
    my_class.comments = ReverseDoc.create_comment(str(soup.find("div", {"class": "block"}).text), False)
    return my_class