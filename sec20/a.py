from decimal import Decimal
from importlib import reload
import sec20.b
gretting = 'Hello!'

def print_hello():
    print(gretting)
    print(Decimal('3.232')+Decimal('3.2111'))

print_hello()
print(sec20.b.now)
sec20.b.print_b_time()
