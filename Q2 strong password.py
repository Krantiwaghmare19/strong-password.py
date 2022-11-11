print("create a strong password" )
ch=input("enter the uppercase letter")
if ch>="A" and ch<="Z":
    print(ch)
    ch2=input("enter the lowercase letter")
    if ch2>="a" and ch2<="z":
        print(ch2)
        num=int(input("enter the number"))
        if num>=1 and num<=100:
            print(num)
            sc=input("enter the sc")
            if sc=="@" or sc=="#":
                print(sc)
                s=input("enter")
                if s=="gmail.com" or s=="navgurukul.org" or s=="company.com":
                    print(s)
                    password=(ch+ch2+str(num)+sc+s)
                    print(password)
                    print("This is strong password")
                else:
                    print("incorrect mail")
            else:
                print("incorrect sc")
        else:
            print("incorrect number")                                                                                                                                              
    else:
        print("incorrect ch2")
else:
    print("incorrect ch")
    