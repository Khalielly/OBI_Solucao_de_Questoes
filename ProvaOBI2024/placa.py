# #respota 1

# placa = input()

# if placa[0:3].isupper() and placa[3] == '-' and placa[5:].isdigit() and len(placa)==8:
#     print(1)

# elif placa[0:3].isupper() and placa[3].isdigit() and placa[4].isupper() and placa[5:].isdigit() and len(placa) ==7:
#     print(2)

# else:
#     print(0)

# reposta 2

import re

placa = input()

placa_brasil = r'[A-Z]{3}-[0-9]{4}'
placa_mercosul = r'[A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2}'

if re.match(placa_brasil, placa):
    print(1)
    
elif re.match(placa_mercosul, placa):
    print(2)
    
else:
    print(0)