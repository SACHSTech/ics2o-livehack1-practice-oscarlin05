"""
------------------------------------------------------------------------------
Name:   days_hours.py
Purpose:  a program that convers the amount of hours to days 
 
Author: Lin.O
 
Created: 08/02/2021
------------------------------------------------------------------------------
"""
#get minutes 
minutes = int(input("How many mintues are you calculating? "))
days = minutes//1440
hours = (minutes % 1440 - days)//60
minutess = minutes % 60

#output
print(minutes, "minutes = ", days, "days", hours, "hours", minutess ,"minutes")
