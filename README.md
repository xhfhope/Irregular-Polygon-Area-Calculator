# Irregular Polygon Area Calculator
 Given a list of vertices, calculate the area of a given polygon
 
Example input:
[(4, 2), (1, 4), (3, 8), (3, 1), (11, 4)]

Example output:
32.5

This program first generates an origin from the list of vertices and then calculates the angle of each vertex from the origin. Using this information, the vertices are sorted by the angle to form the correct edges between vertices, and lastly Gauss' shoelace formula is applied to generate the area.
