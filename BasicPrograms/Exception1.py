'''while True:
    try:
        n=int(input("Please enter an integer"))
        m=int(input("Please enter an integer:"))
        z=n/m
    except Exception as e:

        print("Not an integer! Please again 123")
        print(e)
    except ValueError:
        print("Not an integer! Please try again 456")

    finally:
        print("You successfully entered an integer")'''
try:
    klu1 = open("file.txt","w+")
    try:
        klu1.write("XYZ THIS IS SECTION17 CRT CLASS")
    finally:
        klu1.close()
except IOError:
    print("FILE NOT FOUND")
else:
    print("The file is opened successfully")
    klu1.close()