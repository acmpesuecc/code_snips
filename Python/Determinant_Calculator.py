def DeterminantCalc(D):
    if len(D)>2:
        Determinant=0
        for i in range(len(D)):#Columns of D
            Minor=[]
            #Minor of D[0][i]:
            for j in range(len(D)):#Minor's rows
                if j!=0:
                    Minor.append([])
                    for k in range(len(D)):#Minor's columns
                        if k!=i:
                            if j>=len(Minor):
                                Minor[j-1].append(D[j][k])
                            else:
                                Minor[j].append(D[j][k])
            Determinant+=D[0][i]*(-1)**i * DeterminantCalc(Minor)
        return Determinant
    else:
        return D[0][0]*D[1][1] - D[0][1]*D[1][0]
Det=[]
from random import randint as r

while True:
    try:
        Detlen=int(input("Enter the size of the determinant (larger numbers will take a long time): "))
        break
    except:
        print("Invalid input, try again")

while True:
    try:
        Type=int(input("Enter 0 for autogenerated determinant or 1 for manual entries: "))
        if Type not in [0,1]:
            raise
        break
    except:
        print("Invalid input, try again")
        
for i in range(Detlen):
    Det.append([])
    for j in range(Detlen):
        Det[i].append(int(input("Enter value at {}x{}: ".format(i+1,j+1))) if Type else r(0,100))
for i in range(Detlen):
    print(Det[i])
print("Determinant:",DeterminantCalc(Det))