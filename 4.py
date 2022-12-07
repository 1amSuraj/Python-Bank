def great(a,b,c):
    g=0
    if a>b and a>c:
        g=a
    elif b>a and b>c:
        g=b
    elif c>a and c>b:
        g=c
    print(g)
great(30,40,50)