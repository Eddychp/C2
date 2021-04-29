class Suma_de_matrizes:
    a =[[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    b =[[9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]]
def sumar_matrices(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):

        m3 = []
        for i in range(len(m10)):
            m3.append([])
            for j in range (len(m1[0])):
                m3[i].append(m1[i][j+m2[i][j]])
        return m3
    else:
        return None
    c = sumar_matrices(a, b)
    if c == None:
        print("")
    else:
        for fila in c:
            print("[", end="")
            for elementos in fila:
                print(elementos,end="")
            print("]")



