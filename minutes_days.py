"""
------------------------------------------------------------------------------
Name:   days_hours.py
Purpose:  a program that convers the amount of hours to days 
 
Author: Lin.O
 
Created: 08/02/2021
------------------------------------------------------------------------------
"""
print("*****Minutes to Days and Hours *****")

#get minutes 
minutes = int(input("How many mintues are you calculating? "))
days = minutes//1440
hours = (minutes%1440 - days)//60
minutess = minutes%60

#output
print(str(minutes) + " minutes = " + str(days) + " days " + str(hours) + " hours " + str(minutess) + " minutes ")
