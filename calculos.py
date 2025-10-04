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
        if monto == 0:
            print("No se puede cobrar un monto de 0$")
            return
        porcentaje=(monto*10)/100
        total_pagar=print(f"el total del monto  ${monto} mas la propina ${porcentaje} es de ${monto+porcentaje}")

    elif opcion == 2:
        monto=float(input("Ingrese el monto total de la cuenta: "))
        if monto == 0:
            print("No se puede cobrar un monto de 0$")
            return
        porcentaje=(monto*15)/100
        total_pagar=print(f"el total del monto  ${monto} mas la propina ${porcentaje} es de ${monto+porcentaje}")


    elif opcion == 3:
        monto=float(input("Ingrese el monto total de la cuenta: "))
        if monto == 0:
            print("No se puede cobrar un monto de 0$")
            return
        porcentaje=(monto*20)/100
        total_pagar=print(f"el total del monto  ${monto} mas la propina ${porcentaje} es de ${monto+porcentaje}")


    elif opcion == 4:
        monto=float(input("Ingrese el monto total de la cuenta: "))
        if monto == 0:
            print("No se puede cobrar un monto de 0$")
            return
        porcentaje=float(input("Ingrese el porcentaje que quieres dar de propina: "))
        if porcentaje == 0:
            print("No se puede dar una propina de 0%")
            return
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
        if monto == 0:
            print("No se puede cobrar un monto de 0$")
            return
        personas=int(input("Ingrese cuantas personas van a pagar la propina: "))
        if personas == 0:
            print("no puede haber 0 personas pagando la propina")
            return
        porcentaje=(monto*10)/100
        total_pagar=print(f"el total del monto ${monto} mas la propina ${porcentaje} que tiene que pagar las {personas} personas es de {(monto+porcentaje)/personas} cada una.")

    elif opcion == 2:
        monto=float(input("Ingrese el monto total de la cuenta: "))
        if monto == 0:
            print("No se puede cobrar un monto de 0$")
            return
        personas=int(input("Ingrese cuantas personas van a pagar la propina: "))
        if personas == 0:
            print("no puede haber 0 personas pagando la propina")
            return
        porcentaje=(monto*15)/100
        total_pagar=print(f"el total del monto ${monto} mas la propina ${porcentaje} que tiene que pagar las {personas} personas es de {(monto+porcentaje)/personas} cada una.")


    elif opcion == 3:
        monto=float(input("Ingrese el monto total de la cuenta: "))
        if monto == 0:
            print("No se puede cobrar un monto de 0$")
            return
        personas=int(input("Ingrese cuantas personas van a pagar la propina: "))
        if personas == 0:
            print("no puede haber 0 personas pagando la propina")
            return
        porcentaje=(monto*20)/100
        total_pagar=print(f"el total del monto ${monto} mas la propina ${porcentaje} que tiene que pagar las {personas} personas es de {(monto+porcentaje)/personas} cada una.")


    elif opcion == 4:
        monto=float(input("Ingrese el monto total de la cuenta: "))
        if monto == 0:
            print("No se puede cobrar un monto de 0$")
            return
        personas=int(input("Ingrese cuantas personas van a pagar la propina: "))
        if personas == 0:
            print("no puede haber 0 personas pagando la propina")
            return
        porcentaje=float(input("Ingrese el porcentaje que quieres dar de propina: "))
        if porcentaje == 0:
            print("No se puede dar una propina de 0%")
            return
        resultado=(monto*porcentaje)/100
        total_pagar=print(f"el total del monto ${monto} mas la propina ${porcentaje} que tiene que pagar las {personas} personas es de {(monto+porcentaje)/personas} cada una.")

    else:
        print("Ingresaste la opcion incorrecta")





