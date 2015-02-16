import ReverseDoc
import sys
from bs4 import BeautifulSoup


class Java():
    def __init__(self):
        self.name = ""
        self.location = ""

    def __str__(self):
        return self.location


def findClasses(soup):
    classes = soup.find("h2", {"title": "Class Hierarchy"})
    java_class_list = list()
    if classes:
        classes = classes.findNext("ul").findNext('ul')
        class_list = classes.find_all("li")
        for java_class in class_list:
            new_class = Java()
            new_class.name = str(java_class.find("span", {"class": "typeNameLink"}).text)
            new_class.location = str(java_class.find("a").get("href"))
            java_class_list.append(new_class)
            print(new_class)
    return java_class_list


def findInterfaces(soup):
    interfaces = soup.find("h2", {"title": "Interface Hierarchy"})
    interface_list = list()
    if interfaces:
        interfaces = interfaces.findNext("ul")
        temp_list = interfaces.find_all("li")
        for temp_class in temp_list:
            new_class = Java()
            new_class.name = str(temp_class.find("span", {"class": "typeNameLink"}).text)
            new_class.location = str(temp_class.find("a").get("href"))
            interface_list.append(new_class)
            print(new_class)
    return interface_list


def main():
    if len(sys.argv) > 1:
        htmlfile = sys.argv[1]
    else:
        # htmlfile = input("Enter file name with path: ")
        htmlfile = "./tests/overview-tree.html"
    with open(htmlfile) as f:
        htmltext = f.read()
    soup = BeautifulSoup(htmltext)
    class_list = findClasses(soup)
    interface_list = findInterfaces(soup)


if __name__ == '__main__':
    main()