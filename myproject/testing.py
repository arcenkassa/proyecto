
'''def solution(n):

    for i in n:
        max = 0
        lista = []
        largo = 0
        i=bin(i)
        i=i.split("b")[1]
        largo=len(i)
        print i
        print largo
        for a in i:
            if a == '0':
                max = max +1
            elif largo == 0:
                break

            elif max != 0:
                lista.append(max)
                max = 0
            largo= largo - 1


        lista = sorted(lista)
        print lista
        return lista[-1]



a = [1545642,147,483,647,23432,32432543265,4356456]
print solution(a)'''

'''def solution(A):
    veces=0
    for i in A:
        for x in A:
            if i == x:
                veces=veces+1
        if veces == 1:
            return i
        else:
            veces=0




lista=[9, 3, 9, 3, 9, 7, 9]
print solution(lista)'''



'''CyclicRotation
def solution(A, K):
    lista=A
    for x in range(0,K):
        lista.insert(0,lista[-1])
        lista.pop(-1)
    return lista



A = [3, 8, 9, 7, 6]
K = 3
solution(A,K)'''




