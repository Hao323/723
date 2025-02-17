#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:50:20 2025

@author: haojiacheng
"""


import math  #Provides mathematical calculation functions





        
        


def calculate(x):
    global expression
    try:
        value = float(expression) #Convert input to floating-point numbers
        result = None
        
        if x == "tan":
            result = math.tan(math.radians(value)) #Angular Rotation (math.radians(value))
        elif x == "sin":
            result = math.sin(math.radians(value))
        elif x == "cos":
            result = math.cos(math.radians(value))
        
        elif x == "asin":
                if -1 <= value <= 1:
                    result = math.degrees(math.asin(value)) #radian to angle (math.degrees()).
                else:
                    raise ValueError("Invalid value, please enter a number in the range of 1 to -1")
        elif x == "acos":
                if -1 <= value <= 1:
                    result = math.degrees(math.acos(value))
                else:
                    raise ValueError("Invalid value, please enter a number in the range of 1 to -1")
        elif x == "atan":
                result = math.degrees(math.atan(value))
                
        entry_var.set(result) #Only -1 ≤ x ≤ 1 are allowed, otherwise a ValueError will be thrown and an error window will pop up.
        expression = str(result)
    except ValueError as ve:
        messagebox.showerror("Error", f"input error: {ve.}")
        expression = ""
        
        

    


    




