try:
    score = int(input("Score:"))
except:
    print("Input integer")
else:
    print("Score input:", score)
    if score >= 80:
        print("Pass")
    else:
        print("Fail")