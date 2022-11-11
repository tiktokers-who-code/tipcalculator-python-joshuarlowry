# tipcalculator-python-joshuarlowry
A tip calculator that accepts the subtotal of the meal, but calculates the tip percentage off of a variable array of factors.

## NAME
    calculatetip - This module provides different methods for calculating tip.

## FUNCTIONS

    calculate_cash_tip(subtotal, alcohol, tax, tip_percentage)
        Calculate the cash tip you should slip to your wait staff when a traditional tipper is paying.
    
    calculate_tip(subtotal, tip_percentage)
        Calculate the tip and return the tip value
    
    calculate_traditional_tip(subtotal, alcohol, tax)
        Calculate the tip minus alcohol and taxes even though tax was calculated on alcohol too.
