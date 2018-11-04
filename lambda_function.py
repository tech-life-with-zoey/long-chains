#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def compute_short_chain(number):
    """Compute a short chain

    Arguments:
        number {int} -- Requested number for which to compute the square

    Returns:
        int -- Value of the square/short chain for the given number
    """

    return number * number

def compute_long_chain(number):
    """Compute a long chain

    Arguments:
        number {int} -- Requested number for which to compute the cube

    Returns:
        int -- Value of the cube/long chain for the given number
    """

    return number * number * number

def lambda_handler(event, context):
    pass
