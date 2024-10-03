def buscarr():
    with open("codigos.txt","r") as f:
        import re
        palabra_clave=input("ingrese el dato a buscar""\n")
        lineas=f.readlines()
        buscador=re.escape(palabra_clave)
        patas=re.compile(buscador)
        print("Resultado de la busqueda:""\n")
        for linea in lineas:
            if patas.search(linea):
                print(f"{linea.strip()}")