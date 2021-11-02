def string(s):   
    s = s[0:len(s)-1]
    if len(s) != 0:
        print(s)
        string(s)
    elif len(s) == 0:
        print(" ")
        return

zin = "Hallo ik ben een string en ik wordt opgegeten"
string(zin)