def transpose(matrix: list[list])->list[list]:
    matrix_t=[[ 0 for _ in range(5) ] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            matrix_t[j][i]=matrix[i][j]
    
    print("Transpose:")
    print(matrix_t)

def csvToMatrix(path: str) -> None:
    with open(path,"rt") as file:
        matrix=[]
        for line in file:
            row= line.strip().split(",")
            matrix.append(row)
        print("Orginal:")
        print(matrix)
        transpose(matrix)


csvToMatrix("market.csv")