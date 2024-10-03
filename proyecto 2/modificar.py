def modificar():
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
        print("que modificasion desea realizar?")
        print("1. Nombre del producto\n2. Existencia\n3. Precio\n4. Proveedor\n5. Estado\n6. Descuento\n")
        print("Si desea modificar todos los datos ingre el No.7")
        no=int(input("ingrese el numero de la opcion""\n"))
        for i,linea in enumerate(lineas):
            if patas.search(linea):
                dividir=linea.strip().split()
                if no==1:
                    print(dividir[1])
                    nombre=input("ingrese un nuevo nombre para el producto""\n")
                    dividir[1]=nombre
                elif no==2:
                    print(dividir[4])
                    existencia=input("Ingrese la nueva existencia del del producto""\n")
                    dividir[4]=existencia
                elif no==3:
                    print(dividir[2])
                    precio=input("Ingrese el nuevo precio del producto Q.")
                    dividir[2]=precio
                elif no==4:
                    print(dividir[3])
                    proveedor=input("Ingrese el nombre del nuevo proveedor""\n")
                    dividir[3]=proveedor
                elif no==5:
                    print(dividir[5])
                    estado=input("Ingrese el estado del producto A o B""\n")
                    dividir [5]=estado
                elif no==6:
                    print(dividir[6])
                    descuento=input("Ingrese el nuevo descuento n%""\n")
                    print("Estos datos tambien se modificaran""\n")
                    print(dividir[2])
                    print(dividir[4])
                    precios=float(dividir[2])
                    existencias=int(dividir[4])
                    des=float(descuento)
                    precio_total=precios*existencias
                    total_descuento=(precio_total*des)/100
                    total_sin_descuento=precio_total-total_descuento
                    total_descuentos=str(total_descuento)
                    precio_totals=(precio_total)
                    total_sin_descuentos=str(total_sin_descuento)
                    dividir[6]=descuento+"\n"
                    if precio_totals:
                        dividir[7]=precio_totals
                    linea[i]="   ".join(dividir)+"\n"
                    if total_descuentos:
                        dividir[8]=total_descuentos
                    linea[i]="   ".join(dividir)+"\n"
                    if total_sin_descuentos:
                        dividir[9]=total_sin_descuentos
                    linea[i]="   ".join(dividir)+"\n"
                elif no==7:
                    dividir=linea.strip().split()
                    nombre=input("ingrese un nuevo nombre para el producto""\n")
                    existencia=input("Ingrese la nueva existencia del del producto""\n")                    
                    precio=input("Ingrese el nuevo precio del producto Q.")                    
                    proveedor=input("Ingrese el nombre del nuevo proveedor""\n")                    
                    estado=input("Ingrese el estado del producto A o B""\n")                    
                    descuento=input("Ingrese el nuevo descuento n%""\n")
                    dividir[2]=(precio)
                    dividir[4]=(existencia)
                    precios=float(precio)
                    existencias=int(existencia)
                    des=float(descuento)
                    precio_total=precios*existencias
                    total_descuento=(precio_total*des)/100
                    total_sin_descuento=precio_total-total_descuento
                    if precio_total:
                        dividir[7]=precio_total
                    linea[i]="   ".join(dividir)
                    if total_descuento:
                        dividir[8]=total_descuento
                    linea[i]="   ".join(dividir)
                    if total_sin_descuento:
                        dividir[9]=total_sin_descuento
                    linea[i]="   ".join(dividir)
                    if nombre:
                        print(dividir[1])
                        dividir[1]=nombre
                    lineas[i]= ' '.join(dividir)+'\n'
                    if existencia:
                        print(dividir[4])
                        dividir[4]=existencia
                    lineas[i]= ' '.join(dividir)+'\n'
                    if proveedor:
                        print(dividir[3])
                        dividir[3]=proveedor
                    lineas[i]= ' '.join(dividir)+'\n'
                    if precio:
                        print(dividir[2])
                        dividir[2]=precio
                    lineas[i]= ' '.join(dividir)+'\n'
                    if estado:
                        print(dividir[5])
                        dividir[5]=estado
                    lineas[i]= ' '.join(dividir)+'\n'
                    if descuento:
                        print(dividir[6])
                        dividir[6]=descuento
                    lineas[i]= ' '.join(dividir)+'\n'
                linea[i]="   ".join(dividir)
            else:
                if no>=8:
                    print("Ingrese una opcion valida >:C""\n")
    f.close()
    with open("codigos.txt","w") as f:
        f.writelines(lineas)
        f.close()