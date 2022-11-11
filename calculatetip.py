"""This module provides different methods for calculating tip."""

def calculate_tip(subtotal, tip_percentage):
    """Calculate the tip and return the tip value"""
    return round(subtotal * (tip_percentage/100),2)

def calculate_traditional_tip(subtotal, alcohol, tax):
    """Calculate the tip minus alcohol and taxes even though tax was calculated on alcohol too."""
    return round(calculate_tip(subtotal-alcohol-tax, 5),2)

def calculate_cash_tip(subtotal, alcohol, tax, tip_percentage):
    """Calculate the cash tip you should slip to your wait staff when a traditional tipper is paying."""
    return calculate_tip(subtotal, tip_percentage) - calculate_traditional_tip(subtotal, alcohol, tax)
    