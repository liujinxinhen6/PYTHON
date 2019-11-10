def show_magcians(names):
    for name in names:
        print(name)
def make_greet(unmake,commake):
    while unmake:
        curmake="the great: "+unmake.pop()
        commake.append(curmake)
magicians=['a','b','c']
commake=[]
make_greet(magicians,commake)
show_magcians(commake)