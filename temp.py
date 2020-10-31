import re

a, b = '56465323', '53465-56'
d = b

if '-' in d:
    d = d.split('-')[0]
pass