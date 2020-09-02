import random
def start_game():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat
def add_new_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while(mat[r][c]!=0):
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2
def compress(mat):
    changed=False
    new_mat=[]
    for i in range(4):
        new_mat.append([0]*4)
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]
                if j!=pos:
                    changed=True
                pos+=1
    return new_mat,changed
def reverse(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
    return new_mat
def transpose(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat
def merge(mat):
    changed=False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                changed=True
                mat[i][j]*=2
                mat[i][j+1]=0
    return mat,changed
def move_up(grid):
    a=transpose(grid)
    b,changed1=compress(a)
    c,changed2=merge(b)
    changed=changed1 or changed2
    d,temp=compress(c)
    e=transpose(d)
    return e,changed
def move_down(grid):
    a=transpose(grid)
    k=reverse(a)
    b,changed1=compress(k)
    c,changed2=merge(b)
    changed=changed1 or changed2
    d,temp=compress(c)
    r=reverse(d)
    e=transpose(r)
    return e,changed
def move_left(grid):
    b,changed1=compress(grid)
    c,changed2=merge(b)
    changed=changed1 or changed2
    d,temp=compress(c)
    return d,changed
def move_right(grid):
    k=reverse(grid)
    b,changed1=compress(k)
    c,changed2=merge(b)
    changed=changed1 or changed2
    d,temp=compress(c)
    r=reverse(d)
    return r,changed
    

def get_current_status(mat):
    for i in range(4):
        for j in range(4):
            if(mat[i][j]==16):
                return 'WON'
    for i in range(4):
        for j in range(4):
            if(mat[i][j]==0):
                return 'GAME NOT OVER'
    for i in range(3):
        for j in range(3):
            if(mat[i][j]==mat[i+1][j] or mat[i][j]==mat[i][j+1]):
                return 'GAME NOT OVER'
    for j in range(3):
        if(mat[3][j]==mat[3][j+1]):
                return 'GAME NOT OVER'
    for i in range(3):
        if(mat[i][3]==mat[i+1][3]):
                return 'GAME NOT OVER'
    return 'LOST'
        
        
    
