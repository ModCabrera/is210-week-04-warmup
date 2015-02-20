#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A complex testcase."""

EXPENSE = 14.23
LOOKS_NICE = True
MAX_EXPENSE = 12
GET_OUT_ALIVE = False


SACRIFICE = True

if LOOKS_NICE and EXPENSE <= MAX_EXPENSE:
    SACRIFICE = False
elif not LOOKS_NICE and EXPENSE >= MAX_EXPENSE:
    GET_OUT_ALIVE = False
