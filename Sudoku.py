#Proyecto Integrador
#Magda Karely Elías Velazco A01705205
#Hannia Noemí Rodríguez Vázquez A01635749
#Mauria Celeste Javer Aispuro A01641048
#Link del video:
#https://drive.google.com/file/d/1LrIWu3uPvSSOoWBI50Rrl4Kj2US8mu_a/view?usp=sharing
def main():
    
    import time
    import sys

    print('\033[1m'+'SUDOKU'+'\033[0m')

    play_a=True
    while play_a == True:
        print('\033[1m'+'Menú'+'\033[0m')
        print('1-Conocer como jugar')
        print('2-Jugar')
        print('3-Salir')
        r=input('')
        if r=='1':
            ejemplo=[[' |','a','b','c','d','e','f','g','h','i'],['1|',' ',2,' ',8,' ',6,5,' ',9],['2|',8,' ',2,' ',' ',5,6,' ',' '],['3|',7,' ',1,5, ' ',8,' ',6,' '],['4|',' ', ' ',4,' ',5,' ',8,1,' '],['5|',9,' ',8,1,' ',7,' ', ' ',5],['6|',' ',9,' ',' ',' ',1,' ',8,' '],['7|',3,4,' ',7,1,' ',9,' ',' '],['8|', ' ',' ',' ',' ',7,' ',1,9,' '],['9|',4,' ',' ',6,8,' ',' ',' ',1]]
            print('\033[1m'+'Instrucciones'+'\033[0m')
            print('Podras elegir el nivel de dificultad')
            print('Se generara un sudoku, en este tu elegiras cual número deseas poner')
            print('\033[1m'+'Ejemplo:' + '\033[0m')
            for x in range(10):
                if x == 0:
                    print('|'.join(ejemplo[x]))
                else:
                    for y in range(10):
                        if y > 0:
                            ejemplo[x][y]=str(ejemplo[x][y])
                    print('|'.join(ejemplo[x]))
            print('Las columnas se clasifican por a, b, c, d, e, f, g, h, i')
            print('Las filas por 1, 2, 3, 4, 5, 6, 7, 8, 9')
            print('Para elegir la posición primero escribiras la columna y luego la fila')
            print('\033[1m'+'Ejemplo:' + '\033[0m'+'b2')
            print('Después te aparecera una operación de suma y resta')
            print('\033[1m'+'Ejemplo:' + '\033[0m'+'b2=f2-4')
            print('Por lo que b2=1, así que escribimos el número 1')
            print('\033[1m'+'Recuerda:' + '\033[0m' + 'Los número en horizontal y vertical no se pueden repetir')
            
        elif r=='2':
            volver=False
            valido_2=False
            while valido_2==False:
                print('\033[1m'+'Elige un nivel de dificultad'+'\033[0m')
                print('1-Fácil')
                print('2-Intermedio')
                print('3-Avanzado')
                r=input('')
                if r=='1':
                    nivel=1
                    valido_2=True
                elif r=='2':
                    nivel=2
                    valido_2=True
                elif r=='3':
                    nivel=3
                    valido_2=True
                else:
                    print('\033[91m'+ 'Respuesta no valida' +'\033[0m')
            print('')
            import random

            fila=[' |','a','b','c','d','e','f','g','h','i']
            fila_1=['1|']
            fila_2=['2|']
            fila_3=['3|']
            fila_4=['4|']
            fila_5=['5|']
            fila_6=['6|']
            fila_7=['7|']
            fila_8=['8|']
            fila_9=['9|']
            matriz=[fila, fila_1, fila_2, fila_3, fila_4, fila_5, fila_6, fila_7, fila_8, fila_9]
            matriz_lista=False

            for x in range(1,10):
                for y in range(1,10):
                    matriz[x].append(0)

            #Hacer el sudoku
            while matriz_lista == False:
                matriz_lista=True
                disp_a=[]
                disp_b=[]
                disp_c=[]
                disp_d=[]
                disp_e=[]
                disp_f=[]
                disp_g=[]
                disp_h=[]
                disp_i=[]
                disp=[disp_a ,disp_b ,disp_c ,disp_d ,disp_e ,disp_f ,disp_g ,disp_h ,disp_i]
                for x in range(1,10):
                    for y in range(9):
                        disp[y].append(x)
                for x in range(1,10):
                    for y in range(1,10):
                        matriz[x][y]=0
                for x in range(1,10):
                    if x==1:
                        choice=[1,2,3,4,5,6,7,8,9]
                        for y in range(1,10):
                            num=random.choice(choice)
                            matriz[x][y]=num
                            choice.remove(num)
                            index=disp[y-1].index(num)
                            disp[y-1][index]=0  
                    else:
                        fila_completa=False
                        count=0
                        while fila_completa== False and count<5:
                            fila_completa=True
                            disp_por_fila=[1,2,3,4,5,6,7,8,9]
                            for y in range(1,10):
                                choice=[1,2,3,4,5,6,7,8,9,]
                                for z in range(9):
                                    if disp[y-1][z] != disp_por_fila[z]:
                                        if disp[y-1][z]>0:
                                            choice_eliminar=disp[y-1][z]
                                            choice.remove(choice_eliminar)
                                        else:
                                            choice_eliminar=disp_por_fila[z]
                                            choice.remove(choice_eliminar)
                                    elif disp[y-1][z]==0 and disp_por_fila[z]==0:
                                        choice_eliminar=z+1
                                        choice.remove(choice_eliminar)
                                if choice==[]:
                                    count+=1
                                    y+=-1
                                else:
                                    num=random.choice(choice)
                                    index=disp[y-1].index(num)
                                    disp[y-1][index]=0
                                    index=disp_por_fila.index(num)
                                    disp_por_fila[index]=0
                                    matriz[x][y]=num                                 
                            for y in range(1,10):
                                if matriz[x][y]==0:
                                    fila_completa=False
                            
                                    
                for x in range(1,10):
                    for y in range(1,10):
                        if matriz[x][y]==0:
                            matriz_lista=False
                        
                

            #Crea la matriz del jugador

            filaj=[' |','a','b','c','d','e','f','g','h','i']
            filaj_1=['1|']
            filaj_2=['2|']
            filaj_3=['3|']
            filaj_4=['4|']
            filaj_5=['5|']
            filaj_6=['6|']
            filaj_7=['7|']
            filaj_8=['8|']
            filaj_9=['9|']
            matriz_jugador=[filaj, filaj_1, filaj_2, filaj_3, filaj_4, filaj_5, filaj_6, filaj_7, filaj_8, filaj_9]

            for x in range(1,10):
                for y in range(1,10):
                    matriz_jugador[x].append(' ')


            #Hacer aparecer ciertos valores en la matriz del jugador


            if nivel ==1:
                count=0
                while count < 50:
                    dif=False
                    while dif==False:
                        x=random.randrange(1,10)
                        y=random.randrange(1,10)
                        if matriz_jugador[x][y]!=matriz[x][y]:
                            matriz_jugador[x][y]=matriz[x][y]
                            count+=1
                            dif=True
                        

            elif nivel==2:
                count=0
                while count < 31 :
                    dif=False
                    while dif==False:
                        x=random.randrange(1,10)
                        y=random.randrange(1,10)
                        if matriz_jugador[x][y]!=matriz[x][y]:
                            matriz_jugador[x][y]=matriz[x][y]
                            count+=1
                            dif=True
            else:
                count=0
                while count < 12:
                    dif=False
                    while dif==False:
                        x=random.randrange(1,10)
                        y=random.randrange(1,10)
                        if matriz_jugador[x][y]!=matriz[x][y]:
                            matriz_jugador[x][y]=matriz[x][y]
                            count+=1
                            dif=True

            juego_terminado=False
            incorrecto=0


            start=time.time()
            while juego_terminado==False and volver==False:
                juego_terminado=True
                for x in range(10):
                    if x == 0:
                        print('|'.join(matriz_jugador[x]))
                    else:
                        for y in range(10):
                            if y > 0:
                                matriz_jugador[x][y]=str(matriz_jugador[x][y])
                        print('|'.join(matriz_jugador[x]))
                print('\033[91m'+'Errores:'+str(incorrecto)+'\033[0m')
                print('\033[94m'+'Para salir escribe "s"'+'\033[0m')
                print('\033[94m'+'Para volver al menú principal escribe "m"'+'\033[0m')

                casilla_valida=False
                while casilla_valida==False and volver==False:
                    print('Elige una casilla')
                    r_casilla=(input('')) 
                    if len(r_casilla) == 2:
                        casilla=list(r_casilla) 
                        columna=casilla[0] 
                        if columna=='a' or columna=='b' or columna=='c' or columna=='d' or columna=='e' or columna=='f' or columna=='g' or columna=='h' or columna=='i':
                            fila=int(casilla[1]) 
                            if 0<fila<10:
                                index_columna=matriz[0].index(columna) 
                                if matriz_jugador[fila][index_columna]==' ':
                                    g1=fila
                                    g2=index_columna
                                    cas=matriz[fila][index_columna]
                                    casilla_valida=True
                                    random_valido=False
                                    while random_valido==False:
                                        x=random.randrange(1,10)
                                        y=random.randrange(1,10)
                                        if matriz_jugador[x][y]!=' ':
                                            random_valido=True
                                            c_f_r=matriz_jugador[0][y]+matriz_jugador[x][0]
                                            num_random=matriz_jugador[x][y]
                                    o=random.randrange(1,5)
                                    if o==1:
                                        num=int(cas)-int(num_random)
                                        print(r_casilla,'=',c_f_r,'+',num)
                                        respuesta=int(input(''))
                                        if str(cas)!=str(respuesta):
                                            print('\033[91m'+ 'Respuesta incorrecta' +'\033[0m')
                                            incorrecto+=1
                                        else:
                                            matriz_jugador[g1][g2]=respuesta
                                    elif 0==2:
                                        num=int(num_random)-int(cas)
                                        print(r_casilla,'=',c_f_r,'-',num)
                                        respuesta=int(input(''))
                                        if str(cas)!=str(respuesta):
                                            print('\033[91m'+ 'Respuesta incorrecta' +'\033[0m')
                                            incorrecto+=1
                                        else:
                                            matriz_jugador[g1][g2]=respuesta
                                            
                                    elif 0==3:
                                        num=-int(num_random)-int(cas)
                                        print(r_casilla,'=',c_f_r,'-',num)
                                        respuesta=int(input(''))
                                        if str(cas)!=str(respuesta):
                                            print('\033[91m'+ 'Respuesta incorrecta' +'\033[0m')
                                            incorrecto+=1
                                        else:
                                            matriz_jugador[g1][g2]=respuesta
                                    
                                    else:
                                        num=int(num_random)-int(cas)
                                        print(r_casilla,'=',c_f_r,'-',num)
                                        respuesta=input('')
                                        if str(cas)!=str(respuesta) and respuesta!= 's' and respuesta!= 'm':
                                            print('\033[91m'+ 'Respuesta incorrecta' +'\033[0m')
                                            incorrecto+=1
                                        elif respuesta=='s':
                                            valido_3=False
                                            while valido_3==False:
                                                print('¿Estas seguro que quieres salir?')
                                                print('1-Sí')
                                                print('2-No')
                                                respuesta=input('')
                                                if respuesta == '1':
                                                    sys.exit()
                                                elif respuesta =='2':
                                                    print('Elige una casilla')
                                                    valido_3=True
                                                else:
                                                    print('\033[91m'+ 'Respuesta no valida' +'\033[0m')
                                        elif respuesta=='m':
                                            valido_3=False
                                            while valido_3==False:
                                                print('¿Estas seguro que quieres volver al menú?')
                                                print('1-Sí')
                                                print('2-No')
                                                respuesta=input('')
                                                if respuesta == '1':
                                                    valido_3=True
                                                    volver=True
                                                elif respuesta =='2':
                                                    valido_3=True
                                                else:
                                                    print('\033[91m'+ 'Respuesta no valida' +'\033[0m')
                                        else:
                                            matriz_jugador[g1][g2]=respuesta
                                
                                else:
                                    print('\033[91m'+ 'Ya hay un número en esa casilla' +'\033[0m')
                            
                        else:
                            print('\033[91m'+ 'Casilla no valida' +'\033[0m')
                    
                    elif r_casilla=='s':
                        valido_3=False
                        while valido_3==False:
                            print('¿Estas seguro que quieres salir?')
                            print('1-Sí')
                            print('2-No')
                            respuesta=input('')
                            if respuesta == '1':
                                sys.exit()
                            elif respuesta =='2':
                                valido_3=True
                            else:
                                print('\033[91m'+ 'Respuesta no valida' +'\033[0m')
                    
                    elif r_casilla=='m':
                        valido_3=False
                        while valido_3==False:
                            print('¿Estas seguro que quieres volver al menú?')
                            print('1-Sí')
                            print('2-No')
                            respuesta=input('')
                            if respuesta == '1':
                                valido_3=True
                                volver=True
                            elif respuesta =='2':
                                valido_3=True
                            else:
                                print('\033[91m'+ 'Respuesta no valida' +'\033[0m')
                    else:
                        print('\033[91m'+ 'Casilla no valida' +'\033[0m')
                   
                
                if nivel==1 and incorrecto==15:
                    print('\033[91m'+ 'Has perdido' +'\033[0m')
                    juego_terminado=True
                    
                elif nivel==2 and incorrecto==10:
                    print('\033[91m'+ 'Has perdido' +'\033[0m')
                    juego_terminado=True
                    
                elif nivel==3 and incorrecto==3:
                    print('\033[91m'+ 'Has perdido' +'\033[0m')
                    juego_terminado=True
                
                else:
                    for x in range(1,10):
                        for y in range(1,10):
                            if str(matriz[x][y])!=str(matriz_jugador[x][y]):
                                juego_terminado=False

            if volver == False:
                end=time.time()
                _time_=end-start
                minutos=int(_time_//60)
                segundos=int(_time_%60)
                if minutos < 10:
                    minutos='0'+str(minutos)
                if segundos < 10:
                    segundos='0'+str(segundos)
                tiempo=str(minutos)+':'+str(segundos)


                if nivel==1 and incorrecto!=15:
                    print('\033[94m'+'FELICIDADES, HAS GANADO'+'\033[0m')
                    print('Tu tiempo ha sido:',tiempo)
                        
                elif nivel==2 and incorrecto!=10:
                    print('\033[94m'+'FELICIDADES, HAS GANADO'+'\033[0m')
                    print('Tu tiempo ha sido:',tiempo)
                    
                elif nivel==3 and incorrecto!=3:
                    print('\033[94m'+'FELICIDADES, HAS GANADO'+'\033[0m')
                    print('Tu tiempo ha sido:',tiempo)
                
            
                r_val=False
                while r_val==False:
                    print('Elige una opción')
                    print('1-Ir al menú')
                    print('2-Salir')
                    r=input('')
                    if r=='1':
                        play_a=True
                        r_val=True
                    elif r=='2':
                        sys.exit()
                    else:
                        print('\033[91m'+ 'Respuesta no valida' +'\033[0m')
                    
        elif r=='3':
            sys.exit()
        else:
            print('\033[91m'+ 'Respuesta no valida' +'\033[0m')

if __name__ == '__main__':
    main()
            


    
    


