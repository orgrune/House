from decimal import Decimal

def numerize(s):
    multipliers = {'k': 10**3, 'm': 10**6, 'b': 10**9, 'K': 10**3, 'M': 10**6, 'B': 10**9}

    if s[-1] in multipliers:
        return Decimal(s[:-1]) * multipliers[s[-1]]
    else:
        return int(s)