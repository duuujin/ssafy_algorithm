def preorder(v):
    if v:
        print(v, end= " ")
        preorder(left[v])
        preorder(right[v])

def inorder(v):
    if v:
        inorder(left[v])
        print(v, end=' ')
        inorder(right[v])

def postorder(v):
    if v:
        postorder(left[v])
        postorder(right[v])
        print(v, end=" ")

V = int(input())
arr = list(map(int,input().split()))
left = [0]*(V+1)
right = [0]*(V+1)

for i in range(0, len(arr),2):
    p,c = arr[i],arr[i+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

preorder(1)
print()
inorder(1)
print()
postorder(1)