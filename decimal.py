import decimal 
decimal.getcontext().prec = 3
yogo = decimal.Decimal(2.00000001)*decimal.Decimal('0.09')
print yogo
yogo =  yogo.quantize(decimal.Decimal("0.00"))
print yogo