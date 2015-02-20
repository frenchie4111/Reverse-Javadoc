#!/usr/bin/python3
import ReverseDoc
import os
from bs4 import BeautifulSoup
import urllib


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
    return interface_list


def main():
    htmlfile = input("Enter url to main doc page: ")
    location = input("Enter complete location to output src files: ")
    if htmlfile[-1] != "/":
        htmlfile += "/"
    htmltext = urllib.request.urlopen(htmlfile + "overview-tree.html").read()
    soup = BeautifulSoup(htmltext)
    class_list = findClasses(soup)
    interface_list = findInterfaces(soup)
    for java_class in class_list:
        new_class = ReverseDoc.ReverseDoc(urllib.request.urlopen(htmlfile + java_class.location).read(), interface=False)
        path = os.path.join(output, java_class.location.replace(".html", "") + ".java")
        dirpath = path.rsplit("/", 1)[0] + "/"
        print(dirpath)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        print(path)
        with open(path, "w") as f:
            f.write(str(new_class))
    for interface in interface_list:
        new_interface = ReverseDoc.ReverseDoc(urllib.request.urlopen(htmlfile + interface.location).read(), interface=True)
        path = os.path.join(output, interface.location.replace(".html", "") + ".java")
        dirpath = path.rsplit("/", 1)[0] + "/"
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        with open(path, "w") as f:
            f.write(str(new_interface))


if __name__ == '__main__':
    main()