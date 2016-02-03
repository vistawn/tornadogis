# -*- coding:utf-8 -*-

import math


def get_float_decimal_length(f):
    decimal_part = math.modf(abs(f))[0]
    decimal_length = 0
    while decimal_part < 1 :
        decimal_length = decimal_length + 1
        decimal_part = decimal_part * 10

    return decimal_length
