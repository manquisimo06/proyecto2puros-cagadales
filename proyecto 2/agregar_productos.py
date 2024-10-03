def agregar():
    import random
    import re
    from pathlib import Path    
    archivo=Path('codigos.txt')
    if not archivo.exists():
        with open("codigos.txt","w") as f:
            f.write("Codigo Producto")
            f.write("   "+"Nombre")
            f.write("   "+"Precio")
            f.write("   "+"Proveedor")
            f.write("   "+"Existencia")
            f.write("   "+"Estado")
            f.write("   "+"Descuento")
            f.write("   "+"Total")
            f.write("   "+"Total del descuento")
            f.write("   "+"Total sin descuento")
            f.close()
    abecedario=('abcdefghijklmnopqrstuvwxyz')
    abcd=("")
    codigo=("")
    comprovante=0;
    while comprovante<1:
        i=1
        while i<5:
            numero=str(random.randint(0,9))
            letra=random.choice(abecedario)
            abcd=(abcd+numero)
            codigo=codigo+numero+letra
            i=i+1
        with open("codigos.txt","r") as f:
            lineas=f.readlines()
            buscador=re.escape(codigo)
            patas=re.compile(buscador)
            for linea in lineas:
                if patas.search(linea):
                    comprovante=0;
                else:
                    comprovante=5
            f.close()
    f=open('codigos.txt','a')
    nombre=str(input("Ingrese el nombre del producto""\n"))
    existencia=int(input("Ingrese la cantidad del producto""\n"))
    precio=float(input("Ingrese el precio Q.""\n"))
    proveedor=str(input("Nombre del proveedor""\n"))
    comprovacion=0;
    while comprovacion<1:
        estado=str(input("Estado donde A=aprobado y N=no aprobado""\n"))
        if estado=="A" or estado=="a":
            estado="Aprobado"
            comprovacion=6;
        elif estado=="N" or estado=="n":
            estado="No aprobado"
            comprovacion=6;
        else:
            print("ingrese un tipo valido")
    res=int(input("El producto tiene descuento?""\n""1. Si""\n""2. No"))
    precio_total=precio*existencia
    if res==1:
        descuento=int(input("Ingrese el numero de porcentaje de descueto N%""\n"))
        total_descuento=float(0.0);
        total_descuento=float(precio_total*descuento)/100
        total_sin_descuento=precio_total-total_descuento
    else:
        descuento=0;
        total_sin_descuento=precio_total
        total_descuento=0;
    total_sin_descuenton=str(total_sin_descuento)
    precios=str(precio)
    descuentonn=str(total_descuento)
    axistencias=str(existencia)
    precio_totales=str(precio_total)
    des=str(descuento)
    f.write("\n"+codigo)
    f.write("   "+nombre)
    f.write("   "+precios)
    f.write("   "+proveedor)
    f.write("   "+axistencias)
    f.write("   "+estado)
    f.write("   "+des,)
    f.write("%")
    f.write("   "+precio_totales)
    f.write("   "+descuentonn)
    f.write("   "+total_sin_descuenton)
    f.close()