import os

path = "C:\\Users\\ASUS\\Desktop\\pp2\\Lab6\\filehandling\\26\\Z.txt"

if os.access(path, os.F_OK):
    os.remove(path)