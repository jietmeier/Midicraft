from itertools import combinations



def n_equal_parts(A,B,n):
    i = 0
    point_list = []
    while i <= n:
        point_i = (
            (
                round((i/n) * A[0] + ((n-i) / n) * B[0],8)
            ),
            (
                round((i/n) * A[1] + ((n-i) / n) * B[1],8)
            ),
            (
                round((i/n) * A[2] + ((n-i) / n) * B[2],8)
            )
        )

        point_list.append(point_i)
        i += 1
    
    return point_list

def judge(A,B): # 判断有几个坐标相同
    count=0
    if A[0] == B[0]:
        count+=1
    if A[1] == B[1]:
        count+=1
    if A[2] == B[2]:
        count+=1
    return count

def block(posx,posy,posz,tick,particle):
    
        
    top=[
        (0.5,0.5,0.5),
        (0.5,0.5,-0.5),
        (0.5,-0.5,0.5),
        (0.5,-0.5,-0.5),
        (-0.5,0.5,0.5),
        (-0.5,0.5,-0.5),
        (-0.5,-0.5,0.5),
        (-0.5,-0.5,-0.5),
    ]

    comb = combinations(top,2)
    
    file = open(f'ticknote/{tick}.mcfunction',mode='a')

    for x in comb:
        if judge(x[0],x[1]) == 2:
            p_list = n_equal_parts(x[0],x[1],5)
            # print(type(p_list))
            for p in p_list:

                cmd =f'particle minecraft:{particle} {posx} {posy} {posz} {p[0]} {p[1]+2} {p[2]} 0.1 0 force'
                file.write(cmd+'\n')

    file.close()





        


    









