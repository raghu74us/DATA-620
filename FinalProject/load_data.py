# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 12:47:16 2018

@author: raghu
"""
import os
from urllib.request import urlretrieve

# Assign variable with specific path/file info
url = "http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/"
path = "./reviews_Health_and_Personal_Care_5.json.gz"
filename = "reviews_Health_and_Personal_Care_5.json.gz"


def retrieve_data(filename, url, path):
    if not os.path.exists(path):
        filename, _ = urlretrieve(url+filename, filename)
        print("Data Succesfully Retrieved!")
    else:
        print("Your data already exists in the directory. Enjoy.")


if __name__ == "__main__":
    retrieve_data(filename, url, path)