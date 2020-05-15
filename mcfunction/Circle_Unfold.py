from math import cos,sin,pi

particle = 'end_rod'

count = 0
acc = 60
r = 3

file = 'circle.mcfunction'
file = open(file,'w')
while count < acc:
    th = 2*pi/acc*count
    (x,y) = (
        round(r*cos(th),5), round(r*sin(th),5)
    )
    file.write(f'particle {particle} ~ ~ ~ {x} 0 {y} 0.05 0 force\n')
    count+=1

file.close()








