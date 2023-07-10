import numpy as np
import datetime
from os import system
system('cls')
fecha=datetime.date.today()
#ARRAY DEL ESCENARIO
escenario=np.empty((10,10),dtype=object)
fila=0
for f in range(10):
    for c in range(10):
        escenario[f,c]=fila+1
        fila=fila+1



ent_p=0
ent_g=0
ent_s=0

rut=[]

def menu():
    print('''
1. Comprar entradas
2. Mostrar ubicaciones disponiles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir
    ''')

def comprar():
    global ent_p, ent_g,ent_s
    while True:
        system('cls')
        try:
            op=int(input('Seleccione la cantidad de entradas (del 1 al 3)\n->'))
            if op!=1 and op!=2 and op!=3:
                continue
            for i in escenario:
                print('\t'.join(map(str,i)))
            print('Las entradas no disponibles se marcan con una X\n')
            print("""Platinum, $120.000. (Asientos del 1 al 20)
Gold, $80.000. (Asientos del 21 al 50)
Silver, $50.000. (Asientos del 51 al 100)\n""")
            for e in range(op):
                ubi=str(input(f'Seleccione la ubicacion de la entrada {e+1}\n->'))
                if ubi=='1' or ubi=='2' or ubi=='3' or ubi=='4' or ubi=='5' or ubi=='6' or ubi=='7' or ubi=='8' or ubi=='9' or ubi=='10':
                    if escenario[0,int(ubi[0])-1]=='X':
                        print('Asiento ocupado, Intente nuevamente')
                        continue
                    else:
                        escenario[0,int(ubi[0])-1]='X'
                        ent_p=ent_p+1
                elif ubi=='20' or ubi=='30' or ubi=='40' or ubi=='50' or ubi=='60' or ubi=='70' or ubi=='80' or ubi=='90':
                    if escenario[int(ubi[0])-1,9]=='X':
                        print('Asiento ocupado, Intente nuevamente')
                        continue
                    else:
                        escenario[int(ubi[0])-1,9]='X'
                        if ubi=='20':
                            ent_p=ent_p+1
                        elif ubi=='30' or ubi=='40' or ubi=='50':
                            ent_g=ent_g+1
                        else:
                            ent_s=ent_s+1
                elif ubi=='100':
                    if escenario[9,9]=='X':
                        print('Asiento ocupado, Intente nuevamente')
                        continue
                    else:
                        escenario[9,9]='X'
                        ent_s=ent_s+1
                elif len(ubi)==2:
                    if ubi[0]=='1' and ubi!='10':
                        if escenario[int(ubi[0]),int(ubi[1])-1]=='X':
                            print('Asiento ocupado, Intente nuevamente')
                            continue
                        else:
                            escenario[int(ubi[0]),int(ubi[1])-1]='X'
                            ent_p=ent_p+1
                    elif ubi[0]=='2' and ubi!='20':
                        if escenario[int(ubi[0]),int(ubi[1])-1]=='X':
                            print('Asiento ocupado, Intente nuevamente')
                            continue
                        else:
                            escenario[int(ubi[0]),int(ubi[1])-1]='X'
                            ent_g=ent_g+1
                    elif ubi[0]=='3' and ubi!='30':
                        if escenario[int(ubi[0]),int(ubi[1])-1]=='X':
                            print('Asiento ocupado, Intente nuevamente')
                            continue
                        else:
                            escenario[int(ubi[0]),int(ubi[1])-1]='X'
                            ent_g=ent_g+1
                    elif ubi[0]=='4' and ubi!='40':
                        if escenario[int(ubi[0]),int(ubi[1])-1]=='X':
                            print('Asiento ocupado, Intente nuevamente')
                            continue
                        else:
                            escenario[int(ubi[0]),int(ubi[1])-1]='X'
                            ent_g=ent_g+1
                    elif ubi[0]=='5' and ubi!='50':
                        if escenario[int(ubi[0]),int(ubi[1])-1]=='X':
                            print('Asiento ocupado, Intente nuevamente')
                            continue
                        else:
                            escenario[int(ubi[0]),int(ubi[1])-1]='X'
                            ent_s=ent_s+1
                    elif ubi[0]=='6' and ubi!='60':
                        if escenario[int(ubi[0]),int(ubi[1])-1]=='X':
                            print('Asiento ocupado, Intente nuevamente')
                            continue
                        else:
                            escenario[int(ubi[0]),int(ubi[1])-1]='X'
                            ent_g=ent_g+1
                    elif ubi[0]=='7' and ubi!='70':
                        if escenario[int(ubi[0]),int(ubi[1])-1]=='X':
                            print('Asiento ocupado, Intente nuevamente')
                            continue
                        else:
                            escenario[int(ubi[0]),int(ubi[1])-1]='X'
                            ent_g=ent_g+1
                    elif ubi[0]=='8' and ubi!='80':
                        if escenario[int(ubi[0]),int(ubi[1])-1]=='X':
                            print('Asiento ocupado, Intente nuevamente')
                            continue
                        else:
                            escenario[int(ubi[0]),int(ubi[1])-1]='X'
                            ent_g=ent_g+1
                    elif ubi[0]=='9' and ubi!='90':
                        if escenario[int(ubi[0]),int(ubi[1])-1]=='X':
                            print('Asiento ocupado, Intente nuevamente')
                            continue
                        else:
                            escenario[int(ubi[0]),int(ubi[1])-1]='X'
                            ent_g=ent_g+1
                run=int(input('Para continuar efectue su rut de la persona que ocupara el asiento.\ncomo se ve en el ejemplo\n(Ejemplo: 12.705.579-3, debe ser 12705579)\n->'))
            rut.append(run)
            print("\nLa operacion se ha realizado correctamente\n")
            break

        except :
            print('Error intente nuevamente')

def ganancia():
    print(f'''
| Tipo Entrada        | Cantidad | Total       |
+---------------------+----------+-------------+
| Platinum $120.000   | {ent_p:8d} | ${(ent_p*120000):10d} |
| Gold     $80.000    | {ent_g:8d} | ${(ent_g*80000):10d} |
| Silver   $50.000    | {ent_s:8d} | ${(ent_s*50000):10d} |
+---------------------+----------+-------------+
| Total               | {(ent_s+ent_g+ent_p):8d} | ${(ent_p*120000+ent_g*80000+ent_s*50000):10d}
    ''')



#sistema
while True:
    menu()
    op=str(input('->'))
    if op=='1':
        comprar()
    elif op=='2':
        for i in escenario:
            print('\t'.join(map(str,i)))
        print('Los asientos no disponibles se mostraran con una X')
    elif op=='3':
        rut.sort()
        for i in rut:
            print(i)
    elif op=='4':
        ganancia()
    elif op=='5':
        break
    else:
        continue

if op=='5':
    print(f'''
Allan Romero {fecha}
    ''')
