from decimal import Decimal
import parce
new_exp=input("Calculate: ")
print(Decimal(parce.Parser(new_exp).parseExpression().calc()).normalize())
