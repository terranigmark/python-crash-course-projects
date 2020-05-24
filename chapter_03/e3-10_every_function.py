
def main():
    tacos = ['asada', 'pescado', 'camaron', 'cochinita', 'pastor', 'chapulines', 'tripa']

    # accesing elements
    print(tacos[3])
    print(tacos[0])
    print(tacos[-1])

    # modify elements
    tacos[3] = 'birria'
    print(tacos[3])

    # append elements
    tacos.append('cabeza')
    # insert elements
    tacos.insert(3, 'carnitas')
    print(tacos)

    # remove elements
    ## del
    del tacos[-3]
    print(tacos)
    ## pop
    tacos.pop()
    print(tacos)
    ## remove
    tacos.remove('pastor')
    print(tacos)

    # sorting a list
    print(sorted(tacos))
    tacos.sort()
    print(tacos)
    tacos.reverse()
    print(tacos)

    # finding the lenght
    print(len(tacos))

    

if __name__ == "__main__":
    main()