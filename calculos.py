def porcentaje_de_propina():
    global total_pagar
    
        
    print("-------Menu del cliente-------")
    print("Ingrese el porcentaje de propina que quieres agregar")
    print("""
1.10%
2.15%
3.20%
4.Ingresa el porcentaje que quieras entregar
0.Salir""")
        
    opcion=int(input("Ingresa la opcion que desea usar: "))

       

    if opcion == 1:
        monto=int(input("Ingrese el monto total de la cuenta: "))
        porcentaje=(monto*10)/100
        total_pagar=print(f"el total del monto  ${monto} mas la propina ${porcentaje} es de ${monto+porcentaje}")

    elif opcion == 2:
        monto=float(input("Ingrese el monto total de la cuenta: "))
        porcentaje=(monto*15)/100
        total_pagar=print(f"el total del monto  ${monto} mas la propina ${porcentaje} es de ${monto+porcentaje}")


    elif opcion == 3:
        monto=float(input("Ingrese el monto total de la cuenta: "))
        porcentaje=(monto*20)/100
        total_pagar=print(f"el total del monto  ${monto} mas la propina ${porcentaje} es de ${monto+porcentaje}")


    elif opcion == 4:
        monto=float(input("Ingrese el monto total de la cuenta: "))
        porcentaje=float(input("Ingrese el porcentaje que quieres dar de propina: "))
        resultado=(monto*porcentaje)/100
        total_pagar=print(f"el total del monto  ${monto} mas la propina ${resultado} es de ${monto+resultado}")

    else:
        print("Ingresaste la opcion incorrecta")


def porcentaje_de_propina_varias_personas():

    print("-------Menu del cliente-------")
    print("Ingrese el porcentaje de propina que quieres agregar")
    print("""
1.10%
2.15%
3.20%
4.Ingresa el porcentaje que quieras entregar
0.Salir""")

    opcion=int(input("Ingresa la opcion que desea usar: "))

       

    if opcion == 1:
        monto=int(input("Ingrese el monto total de la cuenta: "))
        personas=int(input("Ingrese cuantas personas van a pagar la propina: "))
        porcentaje=(monto*10)/100
        total_pagar=print(f"el total del monto ${monto} mas la propina ${porcentaje} que tiene que pagar las {personas} personas es de {(monto+porcentaje)/personas}")

    elif opcion == 2:
        monto=float(input("Ingrese el monto total de la cuenta: "))
        personas=int(input("Ingrese cuantas personas van a pagar la propina: "))
        porcentaje=(monto*15)/100
        total_pagar=print(f"el total del monto ${monto} mas la propina ${porcentaje} que tiene que pagar las {personas} personas es de {(monto+porcentaje)/personas}")


    elif opcion == 3:
        monto=float(input("Ingrese el monto total de la cuenta: "))
        personas=int(input("Ingrese cuantas personas van a pagar la propina: "))
        porcentaje=(monto*20)/100
        total_pagar=print(f"el total del monto ${monto} mas la propina ${porcentaje} que tiene que pagar las {personas} personas es de {(monto+porcentaje)/personas}")


    elif opcion == 4:
        monto=float(input("Ingrese el monto total de la cuenta: "))
        personas=int(input("Ingrese cuantas personas van a pagar la propina: "))
        porcentaje=float(input("Ingrese el porcentaje que quieres dar de propina: "))
        resultado=(monto*porcentaje)/100
        total_pagar=print(f"el total del monto ${monto} mas la propina ${porcentaje} que tiene que pagar las {personas} personas es de {(monto+porcentaje)/personas}")

    else:
        print("Ingresaste la opcion incorrecta")





