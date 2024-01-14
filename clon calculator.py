while True:
    def clonAT():
        while True:
            clon1 = int(input("Put your base stats: "))
            clon2 = int(input("Put your clon stats: "))

            isinstance(clon1, int)
            isinstance(clon2, int)

            check = str((input("Your base stats is {} and clon stats is {}? [Y/N]: ".format(clon1, clon2))))

            if check.startswith(("Y")) or check.startswith(("y")):
                    ("Ok")
            else:
                continue
            break

        while True:
            levelclon = int(input("Put your clonlevel: "))
                    
            if(levelclon > 15):
                print("Your level clon is invalid.")
                continue
            elif(levelclon < 1):
                print("Your level clon is invalid.")
                continue
            break

        finalvalue = (clon2 / clon1 * 100)
        print("%2f" % finalvalue,"%")

        def missingAT(x):
            perfect = (clon1 * x)
            ATTotal = perfect - clon2
            return int(ATTotal)

        def result(x, y, z):
                if(finalvalue > x):
                    return print("This is not a valid clon. (Higher % than maximum value possible)")
                elif(finalvalue > y):
                    return print("Your clon is perfect!")
                else:
                    return print("Your clon is not perfect! You are missing", int(missingAT(z)), "Attack")

        def checkar (a, b, c, d):
            if(levelclon == a):
                resultado = result(b, c, d)

        checkar(15, 144, 143, 1.44)
        checkar(14, 129, 128, 1.29)
        checkar(13, 114, 113, 1.14)
        checkar(12, 99, 98, 0.99)
        checkar(11, 84, 83, 0.84)
        checkar(10, 69, 68, 0.69)
        checkar(9, 54, 53, 0.54)
        checkar(8, 44, 43, 0.44)
        checkar(7, 34, 33, 0.34)
        checkar(6, 24, 23, 0.24)
        checkar(5, 19, 18, 0.19)
        checkar(4, 14, 13, 0.14)      
        checkar(3, 9, 8, 0.09)
        checkar(2, 6, 5, 0.06)
        checkar(1, 3, 2, 0.02)       
    def clonCT():
        while True:
            clon1 = float(input("Put your base stats: "))
            clon2 = float(input("Put your clon stats: "))

            isinstance(clon1, int)
            isinstance(clon2, int)

            check = str((input("Your base stats are {} and clon stats are {}? [Y/N]: ".format(clon1, clon2))))

            if check.startswith(("Y")) or check.startswith(("y")):
                        print("Ok")
            else:
                continue
            break

        while True:
            levelclon = int(input("Put your clonlevel: "))
                    
            if(levelclon > 15):
                print("Your level clon is invalid.")
                continue
            elif(levelclon < 1):
                print("Your level clon is invalid.")
                continue
            break

        finalvalue = (clon2 / clon1 * 100)
        print("%2f" % finalvalue, "%")

        def missingAT(x):
            perfect = (clon1 * x)
            ATTotal = perfect - clon2
            return (ATTotal)

        def result(x, y, z):
                if(finalvalue > x):
                    return print("This is not a valid clon. (Higher % than maximum value possible)")
                elif(finalvalue > y):
                    return print("Your clon is perfect!")
                else:
                    return print("Your clon is not perfect! You are missing", round(missingAT(z)), "%", "Critical Rate")

        def checkar (a, b, c, d):
            if(levelclon == a):
                resultado = result(b, c, d)

        checkar(15, 720, 719, 7.20)
        checkar(14, 645, 644, 6.45)
        checkar(13, 570, 569, 5.70)
        checkar(12, 495, 494, 4.95)
        checkar(11, 420, 419, 4.20)
        checkar(10, 345, 344, 3.45)
        checkar(9, 270, 269, 2.70)
        checkar(8, 220, 219, 2.20)
        checkar(7, 170, 169, 1.70)
        checkar(6, 120, 119, 1.20)
        checkar(5, 95, 94, 0.95)
        checkar(4, 70, 69, 0.70)      
        checkar(3, 45, 44, 0.45)
        checkar(2, 30, 29, 0.30)
        checkar(1, 15, 14, 0.15)
    def clonHP():
        while True:
            clon1 = int(input("Put your base stats: "))
            clon2 = int(input("Put your clon stats: "))

            isinstance(clon1, int)
            isinstance(clon2, int)

            check = str((input("Your base stats are {} and clon stats are {}? [Y/N]: ".format(clon1, clon2))))

            if check.startswith(("Y")) or check.startswith(("y")):
                print("Ok")
            else:
                continue
            break

        while True:
            levelclon = int(input("Put your clonlevel: "))
                    
            if(levelclon > 15):
                print("Your level clon is invalid.")
                continue
            elif(levelclon < 1):
                print("Your level clon is invalid.")
                continue
            break

        finalvalue = (clon2 / clon1 * 100)
        print("%2f" % finalvalue,"%")

        def missingAT(x):
            perfect = (clon1 * x)
            ATTotal = perfect - clon2
            return int(ATTotal)

        def result(x, y, z):
                if(finalvalue > x):
                    return print("This is not a valid clon. (Higher % than maximum value possible)")
                elif(finalvalue > y):
                    return print("Your clon is perfect!")
                else:
                    return print("Your clon is not perfect! You are missing", int(missingAT(z)), "Health Points")
        
        def checkar (a, b, c, d):
            if(levelclon == a):
                resultado = result(b, c, d)

        checkar(15, 54, 53, 0.54)
        checkar(14, 49, 48, 0.49)
        checkar(13, 44, 43, 0.44)
        checkar(12, 39, 38, 0.39)
        checkar(11, 35, 34, 0.35)
        checkar(10, 31, 30, 0.31)
        checkar(9, 27, 26, 0.27)
        checkar(8, 23, 22, 0.23)
        checkar(7, 19, 18, 0.19)
        checkar(6, 15, 14, 0.15)
        checkar(5, 12, 11, 0.12)
        checkar(4, 9, 8, 0.09)      
        checkar(3, 6, 5, 0.06)
        checkar(2, 4, 3, 0.04)
        checkar(1, 2, 1, 0.02)
    def clonEV():
        while True:
            clon1 = float(input("Put your base stats: "))
            clon2 = float(input("Put your clon stats: "))

            isinstance(clon1, int)
            isinstance(clon2, int)

            check = str((input("Your base stats are {} and clon stats are {}? [Y/N]: ".format(clon1, clon2))))

            if check.startswith(("Y")) or check.startswith(("y")):
                        print("Ok")
            else:
                continue
            break

        while True:
            levelclon = int(input("Put your clonlevel: "))
                    
            if(levelclon > 15):
                print("Your level clon is invalid.")
                continue
            elif(levelclon < 1):
                print("Your level clon is invalid.")
                continue
            break

        finalvalue = (clon2 / clon1 * 100)
        print("%2f" % finalvalue, "%")

        def missingAT(x):
            perfect = (clon1 * x)
            ATTotal = perfect - clon2
            return (ATTotal)

        def result(x, y, z):
                if(finalvalue > x):
                    return print("This is not a valid clon. (Higher % than maximum value possible)")
                elif(finalvalue > y):
                    return print("Your clon is perfect!")
                else:
                    return print("Your clon is not perfect! You are missing", int(round(missingAT(z))), "%", "Evasion")

        def checkar (a, b, c, d):
            if(levelclon == a):
                resultado = result(b, c, d)

        checkar(15, 576, 575, 5.76)
        checkar(14, 516, 515, 5.16)
        checkar(13, 456, 455, 4.56)
        checkar(12, 396, 395, 3.96)
        checkar(11, 336, 335, 3.36)
        checkar(10, 276, 275, 2.76)
        checkar(9, 216, 215, 2.16)
        checkar(8, 176, 175, 1.76)
        checkar(7, 136, 135, 1.36)
        checkar(6, 96, 95, 0.96)
        checkar(5, 76, 75, 0.76)
        checkar(4, 56, 55, 0.56)      
        checkar(3, 36, 35, 0.36)
        checkar(2, 24, 23, 0.24)
        checkar(1, 12, 11, 0.12)
         
    while True:
        select = str(input("Select what clon you want to calculate [AT/HP/CT/BL/EV]: "))

        if select.startswith(("at")) or select.startswith(("AT")) or select.startswith(("At")):
            clonAT()
        if select.startswith(("ct")) or select.startswith(("CT")) or select.startswith(("Ct")) or select.startswith(("Cr")) or select.startswith(("cr")) or select.startswith(("CR")):
            clonCT()
        if select.startswith(("HP")) or select.startswith(("hp")) or select.startswith(("Hp")) or select.startswith(("He")) or select.startswith(("he")) or select.startswith(("HE")):
            clonHP()
        if select.startswith(("ev")) or select.startswith(("EV")) or select.startswith(("Ev")):
            clonEV()
        else:
            continue
        break