N = int(input())
tree = {}
for i in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
    if root in tree:
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root in tree:
        inorder(tree[root][0])
    if root != '.':
        print(root, end='')
    if root in tree:
        inorder(tree[root][1])

def postorder(root):
    if root in tree:
        postorder(tree[root][0])
        postorder(tree[root][1])
    if root != '.':
        print(root, end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')
