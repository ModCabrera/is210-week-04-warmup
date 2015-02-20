#!usr\env\bin\ python
# -*- code: utf-8 -*-
""" Blood Pressure Monitor"""

BP_STATUS = raw_input('What is your blood pressure? ')

if  BP_STATUS <= 89:
    print 'LOW!'
if 90 >= BP_STATUS <= 119:
     print 'IDEAL!'
if 120 >= BP_STATUS <= 129:
    print 'WARNING!'
if 140 >= BP_STATUS <= 159:
    print 'HIGH!'
if 159 > BP_STATUS >= 160:
    print 'EMERGENCY!'
    
print 'You status if currently:{}'.format(BP_STATUS)
