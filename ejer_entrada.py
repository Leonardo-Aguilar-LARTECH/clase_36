from os import name, system as st

def f_clear_screen():
    if name == "nt":
        st("cls")
    else:
        st("clear")

continuar_fila = True

while continuar_fila == True:
    f_clear_screen()
    print("indique la edad de la persona que solicita ingreso")
    v_edad = int(input())
    if v_edad < 18:
        print("el menor de edad cuenta con el permiso parental? (s/n)")
        v_perm = input()
    elif v_edad > 18:
        print("Acceso Permitido, que disfrute el Evento")
    

    if v_edad < 18 and v_perm == "s":
        print("Acceso Permitido, que disfrute el Evento")
    elif v_edad < 18 and v_perm == "n":
        print("Lo sentimos, no podemos Permitir el ingreso")

    print("hay mas personas en la fila de ingreso (s/n)")
    fila = input()
    if fila.lower() == "n":
        continuar_fila = False
