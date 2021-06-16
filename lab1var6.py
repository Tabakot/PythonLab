import re

s = "Hello$@ Pyt1-2$3%45ahon3& how^ much for{} the maple syrup? $20.99? That's[] ricidulous!!!"
print(s)
s1 = re.sub("[^A-Za-z| ]", "", s)
print(s1)

