"""
------------------------------------------------------------------------------
Name:   days_hours.py
Purpose:  a program that convers the amount of hours to days 
 
Author: Lin.O
 
Created: 08/02/2021
------------------------------------------------------------------------------
"""
#get Fahrenheit 
fahrenheit = float(input("What is your Fahrenheit? "))
celcius = 5/9 * (fahrenheit-32)

#output
number = round(celcius,2)
print("Your Celcius is: " + str(number))