for n1 in range(1, 10, 1):
    for n2 in range(2, 10, 1):
        print(n2, end='')
        print('x', end='')
        print(n1, end='')
        print('=', end='')
        print(n2 * n1, '\t', end='')
    print()
    
    #구구단 전체 출력하기