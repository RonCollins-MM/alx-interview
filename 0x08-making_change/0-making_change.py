#!/usr/bin/python3
"""
Simple function that calculates change (money)
"""


def makeChange(coins, total):
    """
    makeChange function
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    suma = 0
    no_of_coins = 0
    cnt = 0

    while cnt < len(coins) and suma != total:

        if suma + coins[cnt] > total:
            cnt += 1
        else:
            suma += coins[cnt]
            no_of_coins += 1

    if suma == total:
        return no_of_coins
    return -1
