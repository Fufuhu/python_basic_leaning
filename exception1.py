import sys

try:
    score = int(input("Score:"))
except ValueError:
    print("Input Integer!")
    sys.exit()
    
if score >= 80:
    print("Pass")
else:
    print("Failed")