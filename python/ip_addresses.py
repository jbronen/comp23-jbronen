# ip_addresses.py
# Jared Bronen
# COMP 23 - Lab 2

n = 256
temp = ''

for i in range(n):
    a = str(i) + '.'
    for j in range(n):
        b = str(j) + '.'
        for k in range (n):
            c = str(k) + '.'
            for l in range(n):
                d = str(l)
                temp = a + b + c + d
                print temp
                
