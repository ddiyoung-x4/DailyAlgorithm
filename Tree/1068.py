N = int(input())
l = list(map(int, input().split()))
del_node = int(input())

tree = {}
root = -1
for i in range(N):
    if l[i] == -1:
        root = i
    elif l[i] in tree:
        org = tree[l[i]]
        org.append(i)
        tree[l[i]] = org
    else:
        tree[l[i]] = [i]

def is_leaf(node):
    if node in tree:
        return False
    else:
        return True
def num_leaf(root):
    cnt = 0
    if root not in tree:
        return 1
    for node in tree[root]:
        if is_leaf(node):
            cnt += 1
        else:
            cnt += num_leaf(node)
    return cnt

def delete_node(del_node, root):
    if del_node in tree:
        del tree[del_node]
    
    keys = []
    for key in tree:
        if del_node in tree[key]:
            orig = tree[key]
            orig.remove(del_node)
            tree[key] = orig
        if tree[key] == []:
            keys.append(key)
    for key in keys:
        del tree[key]

if del_node == root:
    print(0)
else:
    delete_node(del_node, root)
    print(num_leaf(root))