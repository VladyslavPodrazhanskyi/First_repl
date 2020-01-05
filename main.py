for i in range(1,6):
    for k in range(1,6):
        for x in range(1,6):
            print(i * k // (k * x) == i // x)