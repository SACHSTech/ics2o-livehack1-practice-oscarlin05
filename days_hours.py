"""
------------------------------------------------------------------------------
Name:   days_hours.py
Purpose:  a program that convers the amount of hours to days 
 
Author: Lin.O
 
Created: 08/02/2021
------------------------------------------------------------------------------
"""
print("****** Hours to Days and Hours ******")

#get hours
hours = int(input("How many hours are you calculating to days? "))
days = hours//24
hourss = hours%24

#output
print(str(hours) + " hours = " + str(days) + " days " + str(hourss) + " hours ")