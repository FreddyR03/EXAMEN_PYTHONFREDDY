from calculos import porcentaje_de_propina, porcentaje_de_propina_varias_personas

def menu_principal():

    while True:
        print("------RESTAURANTE DON FREDDY------")
        print("""
1.Va a pagar el total con la propina 1 sola persona
2.Va a pagar el total con la propina varias personas
0.salir""")
        
        opcion=int(input("Ingrese la opcion que desea: "))

        if opcion == 0:
            print("Saliendo del restaurante")
            break
        
        elif opcion == 1:
            porcentaje_de_propina()

        elif opcion == 2:
            porcentaje_de_propina_varias_personas()
        
        else :
            print("Ingresaste una opcion incorrecta, vuelva a intentar")
        
        
        
menu_principal()