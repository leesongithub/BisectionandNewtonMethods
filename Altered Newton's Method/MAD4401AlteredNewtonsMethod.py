# Python script for MAD 4401 Assignment 1, Altered Newton's Method

from math import *

print "\nThis script finds the x intercept of the function (x-3)^4*sin(x), within the given range.\n"
#a = raw_input("Enter the lower bound, a: ")
#b = raw_input("Enter the upper bound, b: ")
#a = int(a)
#b = int(b)

xn = 2 #semi-arbitrary starting point
y = pow((xn-3),4)*sin(xn)
derivY = 4*pow((xn-3),3)*sin(xn)+cos(xn)*pow((xn-3),4)
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
	y = pow((xn-3),4)*sin(xn)
	print "y value is now ",
	print y
	derivY = 4*pow((xn-3),3)*sin(xn)+cos(xn)*pow((xn-3),4)
	steps = steps+1
	print "\n <><><><><><><><><><><><><><> \n"

print "\n******** While loop ended ********\n"

print "Newton's Method approximates that there is an x intercept at x = ",
print xn
print steps,
print "steps were taken.\n"
print "NOTE: THIS SCRIPT CAN ONLY FIND ONE INTERCEPT AT A TIME."
print "RUN MULTIPLE TIMES WITH TARGETED RANGES TO FIND ALL INTERCEPTS.\n"

print "Thank you for your contribution towards the progress of our future overlord and savior, Artificial Malevolence."
