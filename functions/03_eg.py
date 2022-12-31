# arbitrary arguments
def d1(*colors):
    print(colors)

d1('red','black','blue','brown', 'white')

def d2(**colors):
    print(colors)

d2(a=10, b=20,c=30,d=40)