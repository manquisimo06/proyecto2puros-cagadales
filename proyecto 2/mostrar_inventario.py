def inventario():
      import re
      with open("codigos.txt","r") as f:
            lineas=f.readlines()
            print("Este es su inventario final:""\n")
            for linea in lineas:
                  print(f"{linea.strip()}")