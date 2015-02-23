__author__ = 'andrew'
from urllib.request import urlopen
import urllib.error

try:
    new_class = urlopen("http://www.cs.rit.edu/~csci142/Projects/01/src/perp/tree/stu/ActionSequence.java")
except urllib.error.HTTPError:
    print("Success")
except urllib.error.HTTPError:
    print("haha now whatcha gonna do")