#!/usr/bin/python3
import ReverseDoc
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.error



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
            if new_class.name.count(".") != 0:
                continue
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
            if new_class.name.count(".") != 0:
                continue
            new_class.location = str(temp_class.find("a").get("href"))
            interface_list.append(new_class)
    return interface_list


def main():
    # htmlfile = input("Enter url to main doc page: ")
    # output = input("Enter complete location to output src files: ")
    htmlfile = "http://www.cs.rit.edu/~csci142/Projects/01/doc/"
    javafile = htmlfile.replace("doc", "src")
    output = "/home/andrew/java/"
    if htmlfile[-1] != "/":
        htmlfile += "/"
    if output[-1] != "/":
        output += "/"
    output += "src/"
    htmltext = urllib.request.urlopen(htmlfile + "overview-tree.html").read()
    soup = BeautifulSoup(htmltext)
    class_list = findClasses(soup)
    interface_list = findInterfaces(soup)
    for java_class in class_list:
        # if java_class.location.count(".") != 1:
        #     continue
        try:
            new_class = (urlopen(javafile + java_class.location.replace("html", "java")).read(), "try")
        except:
            new_class = (ReverseDoc.ReverseDoc(urllib.request.urlopen(htmlfile + java_class.location).read()), "except")
        path = os.path.join(output, java_class.location.replace(".html", "") + ".java")
        dirpath = path.rsplit("/", 1)[0] + "/"
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        with open(path, "w") as f:
            if new_class[1] == "try":
                f.write(new_class[0].decode("utf-8"))
            else:
                f.write(new_class[0].__str__(False))
    for interface in interface_list:
        # if interface.location.count(".") != 1:
        #     continue
        try:
            new_interface = (urlopen(javafile + interface.location.replace("html", "java")).read(), "try")
        except urllib.error.HTTPError:
            new_interface = (ReverseDoc.ReverseDoc(urllib.request.urlopen(htmlfile + interface.location).read()), "except")
        path = os.path.join(output, interface.location.replace(".html", "") + ".java")
        dirpath = path.rsplit("/", 1)[0] + "/"
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        with open(path, "w") as f:
            if new_interface[1] == "try":
                f.write(new_interface[0].decode("utf-8"))
            else:
                f.write(new_interface[1].__str__(True))


if __name__ == '__main__':
    main()