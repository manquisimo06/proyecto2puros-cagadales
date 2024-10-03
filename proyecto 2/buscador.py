def buscar_texto(palabra_vusqueda):
    import re
    palabra_clave=input("ingrese el dato a buscar""\n")
    with open("codigos.txt","r") as f:
        lineas=f.readlines()
        buscador=re.escape(palabra_clave)
        patas=re.compile(buscador)
        print("Resultado de la busqueda:""\n")
        for linea in lineas:
            if patas.search(linea):
                print(f"{linea.strip()}")
            else:
                print("No se encontraron resultados para la busqueda""\n""Imtemte con otro dato")
                input("\n""ingrese cialquier numero para continuar""\n")