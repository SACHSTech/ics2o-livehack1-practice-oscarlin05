"""
------------------------------------------------------------------------------
Name:   days_hours.py
Purpose:  a program that convers the amount of hours to days 
 
Author: Lin.O
 
Created: 08/02/2021
------------------------------------------------------------------------------
"""
#get temperature 
temperature = int(input("What is your Celcius? "))

#get windspeed 
windspeed = int(input("What is your windspeed? "))

wc = 13.12 + (0.6215*temperature) - (11.37*windspeed ** 0.16) + (0.3965*temperature*windspeed ** 0.16)

number = round(wc,2)

#output
print(number)
