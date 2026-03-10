# finally clause ensures execution of a block of code inspective of the exception
def main():
    try:
        a = int(input("enter number: "))
        print(a)
    except Exception as e:
        print(e)

    finally:            # this gets executed regardless of errors
        print("hi micro")

main()