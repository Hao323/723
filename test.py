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



#Simplify a fraction using the GCD.
def simplify_fraction(x , y):
   
    # Divide both numerator and denominator by the GCD
    gcd = c_gcd(x, y)
    up = x // gcd
    down = y //gcd
    
    print(f"Simplified fraction: {up} / {down}")
    return up , down


#Extension allows users to enter numbers
def user():
    
    #Provide options to let users choose the desired action
    while True:
        print("\nChoose an option:")
        print("1. Calculate GCD")
        print("2. Simplify a fraction")
        
        choice = input("Enter your choice (1-2): ")
        
        if choice == "1" :
        
            # Input two positive integers from the user
            try:
                num1 = int(input("Please enter a number"))
                num2 = int(input("please enter a number"))
                
                # Calculate GCD
                calculate_gcd_with_extension(num1, num2)
                
                
            except ValueError:
                print("Error: Please enter valid integers")
        
        elif choice == "2" :
            
            #Enter the numerator and denominator
            x = int(input("Enter the x : "))
            y = int(input("Enter the y : "))
            
            #Eliminate the invalid case where the denominator is equal to 0
            if y == 0:
                print("Error: y cannot be zero.")
                
            else:
                simplify_fraction(x , y )
            
                    
# Run the program
if __name__ == "__user__":
    user()