import ReverseDoc
class StaticField():
    """
    class static_field

    Stores a single static field of a class for later printing

    slots:
        comment - the comments from the javadoc about the method
        instance_type - the type of the static variable
        name - the name of the variable
"""

    def __init__(self):
        self.comments = ""
        # self.comments.header = False
        self.instance_type = ""
        self.name = ""


    def __repr__(self):
        """
        method __repr__(self)

        Returns the field as a string in this format:
        //comment
        self.instance_type self.name
    """
        return str(self.comments) + "\t */\n "+ "\t" + self.instance_type + " " + self.name + ";\n\n"

def find_fields_details(fields_list, soup):
    for field in fields_list:
        field_details = soup.find("a", {"name": field.name})
        field.comments = ReverseDoc.create_comment(str(field_details.findNext("div", {"class": "block"}).text), True)



def find_fields(soup):
    """
    method find_fields

    Finds all of the fields and returns them as a python list of type static_field
    """
    fields_list = list()
    field_summary = soup.find("a", {"name": "field.summary"}, recursive="true")
    if field_summary:
        for table_row in field_summary.findNext("table").find_all("tr", recursive="true"):
            if table_row.text.strip() != "Modifier and Type\nField and Description":
                new_field = StaticField()
                for table_code in table_row.find_all("code", recursive="true"):
                    if new_field.instance_type == "":
                        new_field.instance_type = str(table_code.text)
                    else:
                        new_field.name = str(table_code.text)
                fields_list.append(new_field)
        find_fields_details(fields_list, soup)
    return fields_list