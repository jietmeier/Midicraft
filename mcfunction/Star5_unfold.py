from math import cos,sin,pi,pow

particle = 'end_rod'

count = 0
acc = 36

file = '5s.mcfunction'
file = open(file,'w')

while count < acc:
    th = 2*pi/acc*count
    r = 1/6*(sin(5*th)+6)

    (x,y) = (
        round(r*cos(th),5), round(r*sin(th),5)
    )


    file.write(f'particle {particle} ~ ~ ~ {x} {y} 0 0.05 0 force\n')
    count+=1

file.close()