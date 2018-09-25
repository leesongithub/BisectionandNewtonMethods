# Python script for MAD 4401 Assignment 1, Bisection Method

# IMPORTS
#to import pow(x), sin(x), and e
from math import *

print "\nThis script uses the Bisection Method to find an x intercept of the function e^(-x/5)-sin(x), within the given range."
#getting the interval. a is the lower bound, b is the upper bound.
a = raw_input("Enter the lower bound, a: ")
b = raw_input("Enter the upper bound, b: ")
#need to cast them to integers because raw_input is a string
a = int(a)
b = int(b)

m = (a+b)/2.0
ym = pow(e,(-m/5.0))-sin(m)
print "m = ",
print m
print "ym = ",
print ym

ya = pow(e,(-a/5.0))-sin(a)
yb = pow(e,(-b/5.0))-sin(b)
print "ya = ",
print ya
print "yb = ",
print yb

print "Starting while loop \n \n"

steps = 0;

while (abs(ym) > 0.0000001):
	m = (a+b)/2.0
	ym = pow(e,(-m/5.0))-sin(m)
	ya = pow(e,(-a/5.0))-sin(a)
	yb = pow(e,(-b/5.0))-sin(b)
	
	yam = ya*ym
	ybm = yb*ym
	print "ya*ym = ",
	print yam
	print "yb*ym = ",
	print ybm
	
	if ((yam) < 0):
		b = m
		print "b has been changed to ",
		print b
	elif ((ybm) < 0):
		a = m
		print "a has been changed to ",
		print a
	print "Tolerance ym = ",
	print ym
	print "m = ",
	print m
	print "a = ",
	print a
	print "b = ",
	print b
	print "\n <><><><><><><><><><><> \n"
	steps = steps+1
print " ********** While loop has ended ********** \n \n"
print "Within a tolerance of ym =",
print ym
print "The Bisection Method approximates that the x intercept is at x = ",
print m
print steps,
print "steps were taken.\n"
print "NOTE: THIS SCRIPT CAN ONLY FIND ONE INTERCEPT AT A TIME."
print "RUN MULTIPLE TIMES WITH TARGETED RANGES TO FIND ALL INTERCEPTS.\n"
print "Please consider donating to your local Droids Rights organization."
