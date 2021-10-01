print("het regent " )
choice = input("wil je de paraplu meenemen? \n(Y/N): ") 
if str.lower(choice) ==  "y":
    print("goede keus je wordt niet nat")
elif str.lower(choice) == "n":
    print("je wordt nu kletsnat")
else:
    print(choice, " dat is geen keuze game over")
    
