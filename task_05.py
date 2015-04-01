#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Blood Pressure Monitor"""


BP_STATUS = int(raw_input('What is your blood pressure? '))


if BP_STATUS <= 89:
    BP_STATUS = 'Low'
elif int(BP_STATUS) <= 119:
    BP_STATUS = 'Ideal'
elif int(BP_STATUS) <= 139:
    BP_STATUS = 'Warning'
elif int(BP_STATUS) <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

print 'You status is currently:{}!'.format(BP_STATUS)
