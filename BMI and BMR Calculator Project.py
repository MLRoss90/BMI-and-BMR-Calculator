Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
'''
Name:Monique Ross
Email: mlross0001@student.stcc.edu
Date:09/27/2026
Course Number:113-D03
Course Name:Intro to Python Programmimg
Problem Number:Chapter 2 Project assignment 
Problem Description:A program that calculates a person's BMI and BMR based on user's input 
'''

'''
  I have read and understand the AI Acceptable Use Policy:
     https://cs.stcc.edu/~silvestri/AIAcceptableUsePolicy/
  I have submitted the required acknowledgment of this policy.
  The work contained in this submission is my own and follows the AI usage rules.

'''

#
# DO NOT REMOVE THE COMMENTS MADE IN THIS TEMPLATE!
#

# **********************************************
# imports here

... # **********************************************
... # Define as many constants you need here
... 
... # CHANGE THIS TITLE!!!
... TITLE = "BMI and BMR Calculations"
... 
... # **********************************************
... 
... print("Welcome to", TITLE)
... 
... # Start your coding here
... # Input
... weight_lbs = float(input("Enter weight in lbs: "))
... height_inches = float(input("Enter height in inches: "))
... age = int(input("Enter age in years: "))
...  
... # Unit conversions
... weight_kg = weight_lbs / 2.2
... height_cm = height_inches * 2.54
...  
... # BMI calculation
... bmi = (weight_kg / (height_cm ** 2)) * 10000
...  
... # BMR calculations
... male_bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
... female_bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161
...  
... # Moderately active caloric needs
... male_calories = male_bmr * 1.55
... female_calories = female_bmr * 1.55
...  
... # Output
... print(f"\nBMI: {bmi:.2f}")
... print(f"Male BMR: {male_bmr:.2f}")
... print(f"Female BMR: {female_bmr:.2f}")
... print(f"Calories needed for a moderately active male: {male_calories:.2f}")
... print(f"Calories needed for a moderately active female: {female_calories:.2f}")
... 
... print("Thank you for using", TITLE)
