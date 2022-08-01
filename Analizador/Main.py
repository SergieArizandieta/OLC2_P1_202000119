import Gramatica as g
f = open("./entrada.txt", "r")
input = f.read()

instrucciones = g.parse(input)