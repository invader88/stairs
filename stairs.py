a = 10
b = 5
k = 1
while k<5:
    print("@"*k*a+"@"*(a-1)+"x")
    for i in range(0, b):
        print("@"*((a-1)+a*k) + "x")
        i += 1
    k += 1
