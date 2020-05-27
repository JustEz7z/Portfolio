def list_animals(animals):
    list = ''
    x = 1
    i = 0
    for j in animals:
        list += str(x) + '. ' + animals[i] + '\n'
        x+=1
        i+=1
    return list