
import re
with open("codigos.txt","r") as f:
    palabra_clave=input("ingrese el dato a buscar""\n")
    lineas= f.readlines()
    buscador=re.escape(palabra_clave)
    patas=re.compile(r"\b"+buscador+r"\b")
    print("Resultado de la busqueda:""\n")
    for linea in lineas:
        if patas.search(linea):
            print(f"{linea.strip()}")
    eliminar = [linea for linea in lineas if not re.search(re.escape(palabra_clave), linea)]
    with open("codigos.txt","w") as f:
        f.writelines(eliminar)
    print("Se elimino la linea elegida")
