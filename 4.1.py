def great(*num):
    g = 0
    for i in num:
        if i>g:
            g=i
    print(g)
great(30,40,50)