X = [[1,2,3,1], 
     [4,5,6,0], 
     [7,8,9,-1]]

print("Matriz original:")
for row in X:
    print(row)
print("\n")

XT = list(map(lambda i: [row[i] for row in X], range(len(X[0]))))

print("Matriz transpuesta:")
for row in XT:
    print(row)