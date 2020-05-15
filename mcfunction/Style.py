from math import cos,sin,pi,pow



def circle(th,r=1):
    (x,y) = (
        round(r*cos(th),r), round(r*sin(th),r)
    )
    return (x,y)

def five_pointed_star(th,r=1):
    a = 6
    r = r/a*(sin(5*th)+a)
    (x,y) = (
        round(r*cos(th),r), round(r*sin(th),r)
    )
    return (x,y)








