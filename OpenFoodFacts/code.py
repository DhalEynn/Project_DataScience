# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:35:23 2019

@author: robin
"""
import pandas as pd
def show():
    df=pd.read_csv("en.openfoodfacts.org.products.csv",delimiter="\t")
    for i in df:
        print(i)
    a= df["carnitine_100g"].isnull()
    print(a)
    print(df[a])
    
def filtre(produit, file, delimit):    
    df=pd.read_csv(file, delimiter= delimit)
    string=produit+"_100g"
    newdf=df[df[string].isnull()]
    newdf.to_csv("produit_pour_le_client_detail.csv",sep=";",encoding="utf-8")
    print("Filtre " + produit + " termine\n")
    return()
    
def copie():
    df=pd.read_csv("produit_pour_le_client_detail.csv",delimiter=";")
    df.to_csv("test.csv",sep=";",encoding="utf-8")
    return()
    

def master_filtre(*args):
    filtre(args[0], "en.openfoodfacts.org.products.csv", "\t")
    if (len(args) > 1):
        copie()
        for arg in args:
            filtre(arg, "test.csv", ";")
            copie()
    print("END")
    return()
    