import wireframe
import pygame

cubeNodes = [(x,y,z) for x in (0,1) for y (0,1) for z in (0,1)]
cube = Wireframe()
cube.addNodes(cube_nodes)
cube.addEdges([(n,n+4) for n in range(0,4)])
cube.addEdges([(n,n+1) for n in range(0,8,2)])
cube.addEdges([(n,n+2) for n in (0,1,4,5)])
