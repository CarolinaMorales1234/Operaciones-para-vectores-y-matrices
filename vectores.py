from sys import stdin
import numerosComplejos as a
def suma_vectores(vector1,vector2):
    suma=[]
    for i in range(len(vector1)):
        resp=a.sumar(vector1[i],vector2[i])
        suma.append(resp)
    return suma
#suma_vectores([[8,3],[-1,-4],[0,-9]],[[8,-3],[2,5],[3,0]])
def inverso_aditivo(vector1):
    for i in range(len(vector1)):
        vector1[i]=a.conjugado(vector1[i])
        vector1[i][0]=vector1[i][0]*-1
    return vector1
#inverso_aditivo([[-5,2],[3,0],[0,-1]])
def escalar_por_vector(escalar,vector1):
    multiplicacion=[]
    for i in range (len(vector1)):
        resp=a.multiplicar(escalar,vector1[i])
        multiplicacion.append(resp)
    return multiplicacion

def suma_matrices(matriz1,matriz2):
     resp=[]
     for i in range(len(matriz1)):
         resp.append(suma_vectores(matriz1[i],matriz2[i]))
     return resp   
#adicion_matrices([[[-8,-3],[-6,-4],[0,-4]],[[-1,8],[6,-10],[8,-5]],[[4,0],[8,5],[-7,-9]]],[[[-7,-2],[-4,-2],[7,7]],[[5,9],[0,3],[6,-5]],[[1,5],[-6,-6],[5,8]]])
    
def inverso_matriz(matriz1):
    resp=[]
    for i in range(len(matriz1)):
        resp.append(inverso_aditivo(matriz1[i]))
    return resp
#inversa_matriz([[[7,3],[-1,7]],[[-9,-4],[-7,-9]]])    

def multiplicacion_escalar_matriz(escalar,matriz):
    resp=[]
    for i in range(len(matriz)):
        resp.append(escalar_por_vector(escalar,matriz[i]))
    return resp
#multiplicacion_escalar_matriz([-2,3],[[[3,-2],[8,-4]],[[4,-10],[-2,-8]]])

def transpuesta(matriz):
    resp=[]
    for i in range(len(matriz[0])):
        resp.append([])
        for j in range(len(matriz)):
            resp[i].append(matriz[j][i])
    return resp
#transpuesta([[[5,9],[-7,-5],[-1,-4]],[[8,2],[-3,-7],[7,-8]]])

def conjugada_matriz(matriz):
    resp=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            resp.append(a.conjugado(matriz[i][j]))
    return resp
#conjugada_matriz([[[-6,1],[3,8]],[[2,-6],[3,0]]])

def daga_matriz(matriz):
    resp=[]
    conj=conjugada_matriz(matriz)
    resp.append(conj)
    transp=transpuesta(resp)
    print(transp)
#daga_matriz([[[7,7],[3,8],[8,4]],[[5,0],[8,-6],[-10,-1]]])

def producto_matrices(matriz1,matriz2):
    resp=[]
    f1=len(matriz1)
    c1=len(matriz1[0])
    for i in range(f1):
        resp.append([[0,0]]*c1)
    print(resp)
    
    for i in range(f1):
        for j in range(c1):
            for k in range(f1):
                resp[i][j]+=matriz1[i][k]*matriz2[k][j]
    
            
    return resp
#producto_matrices([[[-6,2],[0,6],[7,2]],[[6,9],[7,7],[-6,-6]],[[5,8],[-6,8],[6,9]]],[[[9,-6],[-3,-4],[5,2]],[[3,6],[-1,-5],[0,-5]],[[9,9],[8,-4],[-8,-4]]])



























##def main():
##    tamaño=int(stdin.readline().strip())
##    lista1=[]
##    lista2=[]
##    for i in range(tamaño):
##        exp1=[int(x) for x in stdin.readline().split()]
##        lista1.append(exp1)
##    for i in range(tamaño):
##        exp2=[int(x) for x in stdin.readline().split()]
##        lista2.append(exp2)
##    print(sumaVectores(lista1,lista2))
##main()
