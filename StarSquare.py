n = 3
len = 4*(n-1)+3
x = int(len)
a = 0
b = n-1
y = 0
for i in range(1,x+1):
    if i<len//2+1:
        if i%2==0:
            print("*     "*a + "            "*b + "*     "*a)
            b -= 1
        else:
            print("*     " * a + "*  " * x + "   *  " * a)
            a += 1
            x -= 4
            # print(0)

    else:
        if i%2==0:
            print("*     "*a + "            "*b + "*     "*a)
            b += 1
        else:
            a -= 1
            x += 4
            print("*     " * a + "*  " * x + "   *  " * a)




# * * * * * * * * * * *
# *                   *
# *   * * * * * * *   *
# *   *           *   *
# *   *   * * *   *   *
# *   *   *   *   *   *
# *   *   * * *   *   *
# *   *           *   *
# *   * * * * * * *   *
# *                   *
# * * * * * * * * * * *
