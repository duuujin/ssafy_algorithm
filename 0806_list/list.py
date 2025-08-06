n = 3
m = 4
list_2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in range(n):
    for j in range(m):
        print(list_2[i][j + (m-1-(2*j)) * (i % 2)], end= " ")
    print()