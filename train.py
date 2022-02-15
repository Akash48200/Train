# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:38:08 2022

@author: Aakash Tiwari
"""

t=input("Do you need Training?")
if t=="yes":
    print("Let's start the training")
    x=int(input("how many months of training will you like to have?"))
    print("The cost of that would be {}".format(x*1000))
elif t=="no":
    print("Already trained, nice!")
else:
    print("Please give a valid response")



