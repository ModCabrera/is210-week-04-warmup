#!usr\env\bin\ python
# -*- code: utf-8 -*-
""" Blood Pressure Monitor"""

BP_STATUS = int(raw_input('What is your blood pressure? '))


if BP_STATUS <= 89:
    print 'Low'
elif BP_STATUS <= 119:
    print 'Ideal'
elif BP_STATUS <= 139:
    print 'Warning'
elif BP_STATUS <= 159:
    print 'High'
else:
    print 'Emergency'

print 'You status if currently:{}'.format(BP_STATUS)
