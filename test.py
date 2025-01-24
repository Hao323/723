#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:22:30 2025

@author: haojiacheng
"""

def c_gcd(a , b): #Define a function Calculate the greatest common divisor of two integers using Euclidean algorithm
    
    # Determine whether it is an integer
    if not (isinstance(a, int) and isinstance(b, int)):
        return"Both inputs must be integers."
        
    # Determine whether it is a positive integer
    if a <= 0 or b <= 0:
        return"Both inputs must be positive integers."
    

    while b != 0 :
        r = a % b #calculate remainder of a / b 
        a , b = b , r #Update a and b
         
    print(f"The GCD of the given numbers is: {a}") #return
    return a

def calculate_gcd_with_extension(a, b):

     # Calculate the GCD
   gcd = c_gcd(a, b)

    # If GCD calculation failed due to invalid input, return the error message
   if isinstance(gcd, str):
        return gcd

    # Check if the numbers are relatively prime
   if gcd == 1:
        print("The numbers are relatively prime.")
   else:
        print("The numbers are not relatively prime.")

   return gcd