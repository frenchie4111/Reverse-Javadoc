import ReverseDoc

class ClassName():

    def __init__(self):
        self.comments = ""
        self.title = ""

    def __repr__(self):
        if self.comments:
            self.comments = str(self.comments) + "\n */\n"
        return self.comments + str(self.title)



def find_class_name(soup):
    """
    method find_class_name

    finds a returns the name of the class on the page
"""
    my_class = ClassName()
    my_class.title = str(soup.find("pre").text).split('\n')[0]
    if soup.find("div", {"class": "description"}).find("div", {"class": "block"}):
        my_class.comments = ReverseDoc.create_comment(str(soup.find("div", {"class": "block"}).text), False)
    return my_class