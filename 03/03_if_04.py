def main() :
    tel = str(input())
    if len(tel) != 10 :
        return print("Not a mobile number")
    F = tel[0]+tel[1]
    T = ["06","08","09"]
    return print("{}".format("Mobile number" if F in T else "Not a mobile number"))

if __name__ == '__main__' :
    main()