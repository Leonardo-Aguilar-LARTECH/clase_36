from os import name, system as st

def f_clear_screen():
    if name == "nt":
        st("cls")
    else:
        st("clear")

def f_aprobar(nom, punt):
    f_clear_screen()
    if punt > 100 or punt < 0:
        print("el puntaje ingresado no es valido")
    elif punt >= 60:
        print(f"el candidato {nom} ha obtenido {punt}/100 puntos")
        print("el candidato ha sido aprobado")
    else:
        print(f"el candidato {nom} ha obtenido {punt}/100 puntos")
        print("el candidato no ha sido aprobado")

seguir = "s"

while seguir == "s":
    f_clear_screen()
    print("ingresa el nombre del candidato")
    v_nom_alum = input()
    print(f"ingresa el puntaje del candidato {v_nom_alum}")
    v_punt_alum = float(input())    
    f_aprobar(v_nom_alum,v_punt_alum)
    print("quiere evaluar otro candidato? (s/n)")
    seguir = input()
    seguir = seguir.lower()