from DDBB import classes as m
import argparse

parse = argparse.ArgumentParser("My")
parse.add_argument("-U", "--UserName", type=str, nargs="*",help="Username and password for the login")
args = parse.parse_args()
log = m.ops.login(args.UserName[0], args.UserName[1])



if(log == True):
    print("""
        1.Add
        2.Search by ID
    """)
    option = input("Su opcion: ")
    if(option == "1"):
        print("-"*30 + " "*10 + "El ID es requerido para un mejor manejo de datos" + " "*10 + "-"*30 )
        Id = int(input("--ID del producto: "))
        print("-"*30 + " "*10 + "Nombre del producto" + " "*10 + "-"*30 )
        name = str(input("--Nombre: "))
        print("-"*30 + " "*10 + "Precio unitario o por pieza" + " "*10 + "-"*30 )
        price = int(input("--Precio: "))
        print("-"*30 + " "*10 + "Cantidad de piezas" + " "*10 + "-"*30 )
        cant = int(input("--Cantidad: "))
        m.ops.add(Id, name, price, cant)
    elif option == "2":
        print("-"*30 + " "*10 + "ID del producto" + " "*10 + "-"*30 )
        Id = int(input("--ID: "))
        m.ops.search(Id)
        
        
    else:
        print("Option no valida")

else:
    print("-"*30 + " "*10 + "Ejecute de nuevo con las credenciales correctas" + " "*10 + "-"*30 )

