#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 15:27:51 2022

@author: sawan
"""
import sys
import requests

def RomanNumeral():
    # asks the user for their Roman Numeral
    userInput = input("Enter a valid Roman Numeral (containing I, V, X, L, C, D, and  M): ")
    # prints out the value in decimal of the Roman Numeral by calling the RomanNumeralToDecimal function
    print("\nThe value of your Roman Numeral in decimal is",RomanNumeralToDecimal(userInput),"\n")
    # makes the variable numSum global
    global numSum 
    # assigns the output of the RomanNumeralToDecimal function to numSum
    numSum = RomanNumeralToDecimal(userInput)
    
# creates a dictionary with valid Roman Numerals
numerals = {"I": 1, "V": 5,"X": 10,"L": 50,"C": 100, "D": 500, "M": 1000}

# the main function, does the actual math converting Roman Numeral to decimal
def RomanNumeralToDecimal(romanNumeral):
    sumofnum = 0
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if numerals[left] < numerals[right]:
            sumofnum -= numerals[left]
        else:
            sumofnum += numerals[left]
    sumofnum += numerals[romanNumeral[-1]]
    return sumofnum

# function that asks the user whether they want to enter a Roman Numeral again
def playAgain():
    playAgain = input("Would you like to play again?: ").lower()
    if playAgain[0] == "y":
        print("\n")
        errorChecker()
    elif playAgain[0] == "n":
        print("\nThanks for playing!")
        sys.exit()
    else:
        print("\nI didn't understand that")
        playAgain()        

# function that checks if the user entered a valid Roman Numeral (if not calls the function playAgain)
def errorChecker():
    try:
        RomanNumeral()
        funFact(numSum)
        playAgain()
    except KeyError:
        print("\nInvalid Roman Numeral")
        playAgain()
        
# function that uses the Numbers API to return a fun fact related to the Roman Numeral the user entered
def funFact(sumofnum):
    funFact = input("Would you like to know a fun fact about your number? (some numbers might not have facts): ")
    if funFact[0].lower() == "y":
        typeAPI = input("\nWould you like to learn a trivia fact or a math fact about your number (enter t or m): ")
        if typeAPI[0].lower() == "t":
            response = requests.get("http://numbersapi.com/" + str(numSum))
            print("\n" + response.text+"\n")
        elif typeAPI[0] == "m":
            response = requests.get("http://numbersapi.com/" + str(numSum)+"/math")
            print("\n" + response.text+"\n")
        else:
            print("I didn't understand that, I guess I'll give you a trivia fact")
            response = requests.get("http://numbersapi.com/" + str(numSum))
            print("\n" + response.text+"\n")
    else:
        print("OK, thanks for your response")

# where the code is called
def main():
    errorChecker()


main()
