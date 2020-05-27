def enough(cap, on, wait):
    on += wait
    if cap >= on:
        return 0
    else:
        cnttake = on - cap
        return cnttake
enough(100, 60, 50)
enough(10, 5, 5)