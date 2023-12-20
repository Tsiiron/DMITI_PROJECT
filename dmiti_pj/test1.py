import sys

try:
    a = 6 / 0
except Exception:
   e = sys.exc_info()[1].__class__.__name__
   print(type(e)) 
   print(e)
   
   