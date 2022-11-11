"""Test the calculatetip module"""
import calculatetip

assert calculatetip.calculate_tip(100,10) == 10, "Should be 10"
assert calculatetip.calculate_tip(100.10,10) == 10.01, "Should be 10.01"
assert calculatetip.calculate_tip(100.01,10) == 10.00, "Should be 10.00"
assert calculatetip.calculate_tip(100.09,10) == 10.01, "Should be 10.01"
assert calculatetip.calculate_tip(110.90,10) == 11.09, "Should be 11.09"

assert calculatetip.calculate_traditional_tip(110,5,5) == 5, "Should be 5"
assert calculatetip.calculate_traditional_tip(110.10,5,5) == 5.00, "Should be 5.00"
assert calculatetip.calculate_traditional_tip(110.90,5,5) == 5.05, "Should be 5.05"

assert calculatetip.calculate_cash_tip(110,5,5,10) == 6, "Should be 6"
assert calculatetip.calculate_cash_tip(110.90,5,5,10) == 6.04, "Should be 6.04"

