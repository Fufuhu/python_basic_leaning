import sys


try:
    score = int(input("Score:"))
except:
    print("Input integer!")
    sys.exit()
    
if score >= 80:
    print("Pass")
else:
    print("Fail")