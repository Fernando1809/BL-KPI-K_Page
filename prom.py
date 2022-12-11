#COMPUTO 1
print("COMPUTO 1")
L1C1 = float(input("Ingrese L1 : "))
n1= L1C1*0.30
L2C1 = float(input("Ingrese L2 : "))
n2= L2C1*0.30
PC1= float(input("Ingrese P1 : "))
n3=PC1*0.40

prom1 = (n1+n2+n3)
promdiv=prom1/3
print("EL PROMEDIO COMPUTO 1 ES : ", prom1)


#COMPUTO 2
print("COMPUTO 2")
L1C2 = float(input("Ingrese L1 : "))
n1= L1C2*0.30
L2C2 = float(input("Ingrese L2 : "))
n2= L2C2*0.30
PC2= float(input("Ingrese P1 : "))
n3=PC2*0.40

prom2 = (n1+n2+n3)
promdv=prom2/3
print("EL PROMEDIO COMPUTO 2 ES : ", prom2)


#COMPUTO 3
print("COMPUTO 3")
L1C3 = float(input("Ingrese L1 : "))
n1= L1C3*0.30
L2C3 = float(input("Ingrese L2 : "))
n2= L2C3*0.30
PC3= float(input("Ingrese P1 : "))
n3=PC3*0.40

prom3 = (n1+n2+n3)
prmdv=prom3/3
print("EL PROMEDIO COMPUTO 3 ES : ", prom3)

c1=promdiv
c2=promdv
c3=prmdv

print("TOTAL")
promF=(c1+c2+c3)
pro= promF/3
if promF >=6.0:
    print("Felicidades, su nota es: ", promF)
    9
elif promF==5.9:
 print("Paga diferido... ", promF) 
else:
 print("Ni modo negro, tu nota: ", promF)

