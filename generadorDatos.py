"""Hay un total de 100.000 universidades dadas de alta. Hay 50 países
almacenados y uno de ellos debe ser “Spain”. Los países se asignan a la
Universidad de manera aleatoria entre los 50."""
NUM_UNIVERSIDADES = 10
PAISES = []

def generar_universidades(): #Lista con universidades
    #codigo_universidad,pais
    f = open('universidades.txt','w')
    f.write('CODIGO;PAIS\n')
    for i in range(NUM_UNIVERSIDADES):
        universidad = {}
        universidad['codigo'] = i+1
        universidad['pais'] = "prueba"
        f.write(f'{universidad["codigo"]};{universidad["pais"]}\n')
    f.close()

generar_universidades()



