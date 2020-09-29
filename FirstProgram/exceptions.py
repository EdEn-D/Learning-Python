while True:
    try:
        number = int(input("Enter num: \n"))
        print (69/number)
        break
    except (ValueError, ZeroDivisionError):
        print("Enter a number\n")
    finally:
        print("ffffaaaaa")