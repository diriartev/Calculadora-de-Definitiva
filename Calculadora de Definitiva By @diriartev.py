'''
» Date: 16/05/2024
» Version: 1.0
» Author: @diriartev

'''

from colorama import init, Fore, Style
import os

init(autoreset=True)

def cantidad_parciales():
    while True:
        try:
            np = int(input(Fore.LIGHTBLUE_EX + ' → ' + Fore.WHITE + 'Por favor ingrese la cantidad de parciales que presentará éste semestre: ' + Fore.LIGHTBLUE_EX))
            if np > 0:
                break
            else: 
                os.system('cls')
                print('\n' + Fore.YELLOW + '   ⚠︎  | Error: ' + Style.DIM + Fore.BLACK + 'Por Favor ingrese un número mayor que cero.')
        except ValueError:
            os.system('cls')
            print('\n' + Fore.YELLOW + '   ⚠︎  | Error: ' + Style.DIM + Fore.BLACK + 'Por Favor ingrese un número entero mayor que cero, no letras ni palabras.')
    return np

def porcentajes_parciales(cantPar):
    while True:
        porcentajes = []
        for i in range(1 , cantPar + 1):
            while True:
                try:
                    porcentaje = float(input('\n' + Fore.LIGHTBLUE_EX + ' → ' + Fore.WHITE + f'Por favor ingrese el porcentaje del parcial ' + Fore.LIGHTBLUE_EX + f'#{i} ' + Style.DIM + Fore.WHITE + '(sin el signo %)' + Style.RESET_ALL + Fore.WHITE + ': ' + Fore.LIGHTBLUE_EX))   
                    if porcentaje <= 0:
                        print('\n' + Fore.YELLOW + '   ⚠︎  | Error: ' + Style.DIM + Fore.BLACK + 'Por Favor ingrese un número mayor que cero.')
                    else:
                        porcentajes.append(porcentaje)
                        break
                except ValueError:
                    print('\n' + Fore.YELLOW + '   ⚠︎  | Error: ' + Style.DIM + Fore.BLACK + 'Por Favor ingrese un número mayor que cero, no letras ni palabras.')
        if sum(porcentajes) == 100:
            break
        else:
            print('\n' + Fore.YELLOW + '   ⚠︎  | Error: ' + Style.DIM + Fore.BLACK + 'La suma de los porcentajes debe dar 100.')
    return porcentajes

def notas_parciales(cantPar):
    notas = []
    for i in range(1 , cantPar + 1):
        while True:
            try:
                nota = float(input('\n' + Fore.LIGHTBLUE_EX + ' → ' + Fore.WHITE + f'Por favor ingrese la nota del parcial ' + Fore.LIGHTBLUE_EX + f'#{i}' + Fore.WHITE + ': ' + Fore.LIGHTBLUE_EX))
                if nota < 0 or nota > 5:
                    print('\n' + Fore.YELLOW + '   ⚠︎  | Error: ' + Style.DIM + Fore.BLACK + 'Por Favor ingrese un número mayor que cero y menor que cinco.')
                else:
                    notas.append(nota)
                    break
            except ValueError:
                print('\n' + Fore.YELLOW + '   ⚠︎  | Error: ' + Style.DIM + Fore.BLACK + 'Por Favor ingrese un número mayor que cero y menor que cinco, no letras ni palabras.')
    return notas

def mostrar_parciales(cantPar , porcentajes , notas):
    for i in range(cantPar):
        print(Fore.LIGHTBLUE_EX + '    → ' + Fore.WHITE + 'El parcial ' + Fore.LIGHTBLUE_EX + f'#{i+1}' + Fore.WHITE + ' vale el ' + Fore.LIGHTBLUE_EX + f'{porcentajes[i]}%' + Fore.WHITE + ' y su nota es: ' + Fore.LIGHTBLUE_EX + f'{notas[i]}')

def calcular_promedio(cantPar , porcentajes , notas):
    promedio = 0
    for i in range(cantPar):
        promedio += (porcentajes[i] / 100) * notas[i]
    return promedio

def definitiva(promedio):
    if promedio >= 3:
        print(Fore.LIGHTBLUE_EX + '⫸' + Fore.WHITE + '  Su definitiva es ' + Fore.LIGHTBLUE_EX + f'{round(promedio , 2)}' + Fore.WHITE + ' y usted ha ' + Fore.LIGHTGREEN_EX + 'Aprobado' + Fore.WHITE + ' la materia, ¡Felicitaciones! 🥳')
    else:
        print(Fore.LIGHTBLUE_EX + '⫸' + Fore.WHITE + '  Su definitiva es ' + Fore.LIGHTBLUE_EX + f'{round(promedio , 2)}' + Fore.WHITE + ' y usted ha ' + Fore.LIGHTRED_EX + 'Reprobado' + Fore.WHITE + ' la materia, lo sentimos... 😔')

def main():
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + '\n—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————')
    print('\n' + Fore.LIGHTBLUE_EX + '📘 Calculadora de Definitiva' + Style.DIM + Fore.BLACK +' | ' + Style.RESET_ALL + Fore.WHITE + 'Versión 1 📘' + '\n')
    print(Fore.LIGHTBLUE_EX + '—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n')
    cantpar = cantidad_parciales()
    print(Fore.LIGHTBLUE_EX + '\n—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————')
    porcentajes = porcentajes_parciales(cantpar)
    print(Fore.LIGHTBLUE_EX + '\n—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————')
    notas = notas_parciales(cantpar)
    print(Fore.LIGHTBLUE_EX + '\n—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n')
    promedio = calcular_promedio(cantpar , porcentajes , notas)
    print(Fore.LIGHTBLUE_EX + '⫸' + Fore.WHITE + '  Resumen de la información de los parciales' + Fore.LIGHTBLUE_EX + ':' + '\n')
    mostrar_parciales(cantpar , porcentajes , notas)
    print(Fore.LIGHTBLUE_EX + '\n—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n')
    definitiva(promedio)
    print(Fore.LIGHTBLUE_EX + '\n—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n')

if __name__ == '__main__':
    main()
