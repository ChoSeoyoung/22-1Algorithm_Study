# 1991, Silver 1
# https://www.acmicpc.net/problem/1991

import sys

N=int(sys.stdin.readline())

D={}
root='A'

for level in range(N):
    nodes=sys.stdin.readline().rstrip().split()
    
    if nodes[0] not in D:
        D[nodes[0]]=[]
    if nodes[1]!='.':
        if nodes[1] not in D:
            D[nodes[1]]=[]
    D[nodes[0]].append(nodes[1])
    if nodes[2]!='.':
        if nodes[2] not in D:
            D[nodes[2]]=[]
    D[nodes[0]].append(nodes[2])
    
preorder_traversal=[]
def preorder(root):
    if root and root!='.':
        preorder_traversal.append(root)
        preorder(D[root][0])
        preorder(D[root][1])

inorder_traversal=[]
def inorder(root):
    if root and root != '.':
        inorder(D[root][0])
        inorder_traversal.append(root)
        inorder(D[root][1])

postorder_traversal=[]
def postorder(root):
    if root and root != '.':
        postorder(D[root][0])
        postorder(D[root][1])
        postorder_traversal.append(root)


preorder(root)
print(''.join(preorder_traversal))
inorder(root)
print(''.join(inorder_traversal))
postorder(root)
print(''.join(postorder_traversal))