is_lab5_clean = input("is lab 5 clean yes/no").lower()
is_lab6_clean = input("is lab 6 clean yes/no").lower()

if is_lab5_clean == "no" and is_lab6_clean == "yes":
    print("Clean lab 5")
elif is_lab5_clean == "yes" and is_lab6_clean == "no":
   print("Clean lab 6")
elif is_lab5_clean == "no" and is_lab6_clean == "no":
   print("Clean both the labs!")
else:
   print("Business done!!!")
