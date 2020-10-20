import math

def gsort(vertices):
    #find origin
    originX = float(sum(x for x, y in vertices)) / len(vertices)
    originY = float(sum(y for x, y in vertices)) / len(vertices)
    
    sortedV = []
    #get each vertex's angle from origin
    for x, y in vertices:
        #atan2 - 2 argument arctan: angle between x axis and ray to point from origin
        angle = (math.atan2(y - originY, x - originX) + 2.0 * math.pi) % (2.0 * math.pi)
        sortedV.append((x - originX, y - originY, angle))
        
    # sort vertices by angle
    sortedV.sort(key = lambda k: k[2])
    area = 0.0
    for i in range(len(sortedV)):
        j = i + 1
        if j == len(sortedV):
            j=0
        area += sortedV[i][0] * sortedV[j][1]
        area -= sortedV[j][0] * sortedV[i][1]
    area = abs(area) / 2.0
    return area


vertices = [(4, 2), (1, 4), (3, 8), (3, 1), (11, 4)]
print(vertices)
print(gsort(vertices),end='\n\n')
