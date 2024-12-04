file = open("exp_42","r")
content = file.read()
file.close()

def stock(content):
    liste = content.split("\n")
    return liste

def tup_dir(direction):
    liste = []
    for a in direction:
        for b in direction:
            liste.append((a,b))
    return liste

def search(input,d):

    cpt = 0

    for x in range(len(input)):
        for y in range(len(input[0])):
            if input[x][y]=="X":
                for dx, dy in d:
                    if mot(dx, dy, x, y, input):
                        cpt += 1

    return cpt


def mot(dx,dy,x,y,input):
    idx = 0
    find = "MAS"

    while 0 <= x+dx < len(input[0]) and 0 <= y+dy < len(input):

        a = input[x+dx][y+dy]

        if input[x+dx][y+dy]==find[idx]:
            idx += 1
            x += dx
            y += dy
            if find[idx]=="S":
                return True
        else:
            return False



directions = tup_dir([-1,0,1])
input = stock(content)
count = search(input,directions)
print(count)