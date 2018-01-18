def nNodos(tree):
    if(tree is None):
        return 0
    else:
        return 1 + nNodos(tree[0]) + nNodos(tree[2])

def altura (tree):
    if(tree is None):
        return 0
    else:
        return 1 + max(altura(tree[0]), altura(tree[2]))

def maxT(tree):
    if(tree is None):
        return 0
    else:
        return max(maxT(tree[0]),tree[1],maxT(tree[2]))

def preorden(tree):
    if(tree is None):
        return []
    else:
        return [tree[1]] + preorden(tree[0]) + preorden(tree[2])

def nHojas(tree):
    if(tree is None):
        return 0
    if(tree[0] is None and tree[2] is None):
        return 1
    else:
        return nHojas(tree[0]) + nHojas(tree[2])

def suma(tree):
    if (tree is None):
        return 0
    else:
        return suma(tree[0]) + tree[1] + suma(tree[2])

def poda(tree):
    if(tree is None):
        return tree(None, None, None)
    if(tree[0] is None and tree[2] is None):
        return tree(None, tree[1], None)
    else:
        return tree(tree[0], tree[1], tree[2])
    
def zigzag(tree):
    if (tree is None):
        return None
    if (tree[0] is None):
        return tree[1]
    if (tree[0][2] is None):
        return tree[0][1]
    return zigzag(tree[0][2])



def esMinHeap(tree):
    if (tree is None):
        return true
    if (tree[0][1] <= tree[1]):
        return false
    if (tree[2][1] <= tree[1]):
        return false
    return esMinHeap(tree[0]) and esMinHeap(tree[2])

def toMinHeap(tree):
    
