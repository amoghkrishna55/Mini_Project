def table(n):
    for j in range(1,n+1):
        print ("Multiplication table of %d" %(j))
        for i in range (1, 11):
            print ("%d * %d = %d" % (j, i, j * i))
        print ("")
a = int(input("Enter a number: "))
table(a)