# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:37:15 2019

@author: Admin
"""

mainFile = open("products.csv", "r", encoding="utf-8")
Lines = mainFile.readlines()
for Line in Lines:
    Line = Line.split()
    print(Line)
mainFile.close()