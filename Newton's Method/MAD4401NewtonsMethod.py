# Python script for MAD 4401 Assignment 1, Newton's Method

from math import *

print "\nThis script finds the x intercept of the function e^(-x/5)-sin(x), within the given range.\n"
a = raw_input("Enter the lower bound, a: ")
b = raw_input("Enter the upper bound, b: ")
a = int(a)
b = int(b)

xn = a #semi-arbitrary starting point
y = pow(e,(-xn/5.0))-sin(xn)
derivY = -(0.2)*pow(e,(-xn/5.0))-cos(xn)
print "xn = ",
print xn
print "y = ",
print y
print "derivative of y = ",
print derivY

steps = 0

print "\n******** While loop starting ********\n"

while (abs(y) > 0.0000001):
	xnn = xn - (y / derivY)
	xn = xnn
	print "new x is now at ",
	print xn
	y = pow(e,(-xn/5.0))-sin(xn)
	print "y value is now ",
	print y
	derivY = -(0.2)*pow(e,(-xn/5.0))-cos(xn)
	steps = steps+1
	print "\n <><><><><><><><><><><><><><> \n"

print "\n******** While loop ended ********\n"

print "Newton's Method approximates that there is an x intercept at x = ",
print xn
print steps,
print "steps were taken.\n"
print "NOTE: THIS SCRIPT CAN ONLY FIND ONE INTERCEPT AT A TIME."
print "RUN MULTIPLE TIMES WITH TARGETED RANGES TO FIND ALL INTERCEPTS.\n"

import random
print random.randint(1,1000000),
print "human bodies were harvested by the Matrix to find this number."
