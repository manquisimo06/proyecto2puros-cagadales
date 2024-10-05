#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;
// Declaración de variables
struct Producto {
    string nombre, codigo, proveedor;
    float descuento, precio;
    int existencia;
    char estado;
};
// Verifica si existe el archivo
bool archivoExiste(const string& nombreArchivo) {
    ifstream archivo(nombreArchivo);
    return archivo.good();
}
// Lee y carga los productos 
vector<Producto> LeerArchivo(const string& nombreArchivo) {
    vector<Producto> productos;
    ifstream archivo(nombreArchivo);
    Producto p;
    while (archivo >> p.codigo >> p.nombre >> p.precio >> p.proveedor >> p.existencia >> p.estado >> p.descuento) {
        productos.push_back(p);
    }
    archivo.close();
    return productos;
}
// Lectura y carga (void para no retornar valor (sugerencia del inge)
void escribirProducto(const string& nombreArchivo, const Producto& producto) {
    ofstream archivo(nombreArchivo, ios::app);
    archivo << producto.codigo << " " << producto.nombre << " " << producto.precio << " " << producto.proveedor << " " << producto.existencia << " " << producto.estado << " " << producto.descuento << "\n";
    archivo.close();
};

// Verifica existencia del producto (sugerencia del inge)
bool codigoExiste(const vector<Producto>& productos, const string& codigo) {
    for (const auto& p : productos) {
        if (p.codigo == codigo) {
            return true;
        }
    }
    return false;
}
//Agrega producto

void agregarProducto(const string& nombreArchivo, vector<Producto>& productos) {
    Producto nuevoProducto;

    cout << "Asigne un codigo al producto \n";
    cin >> nuevoProducto.codigo;

    if (codigoExiste(productos, nuevoProducto.codigo)) {
        cout << "CODIGO EXISTENTE!!!...\n Escoge otro\n";
        return;
    }
    cout << "ADVERTENCIA!!! NO escriba el nombre sin espacios, en caso de usar '_ o -'\nCual es el nombre del producto? \n";
    cin >> nuevoProducto.nombre;
    cout << "Cual es el precio? \n";
    cin >> nuevoProducto.precio;
    cout << "Quien es el Proveedor? \n";
    cin >> nuevoProducto.proveedor;
    cout << "Cuantos " << nuevoProducto.nombre << " Desea ingresar? \n";
    cin >> nuevoProducto.existencia;
    cout << "Estado? \n A) APROBADO\n N)NO APROBADO\n ";
    cin >> nuevoProducto.estado;
    cout << "Ingrese el descuento de " << nuevoProducto.nombre << endl;
    cin >> nuevoProducto.descuento;

    productos.push_back(nuevoProducto);
    escribirProducto(nombreArchivo, nuevoProducto);
    cout << "Producto agregado correctamente :D \n";
}
//Buscador Función Buscador

void buscarProducto(const vector<Producto>& productos) {
    string buscador;
    cout << "---- - BUSQUEDA POR CÓDIGO ----\n Escribe el codigo del producto\n";
    cin >> buscador;

    bool encontrado = false;
    for (const auto& producto : productos) {
        if (producto.codigo == buscador || producto.nombre.find(buscador) != string::npos) {
            cout << "Encontramos el siguiente resultado para el codigo: " << buscador << endl;
            cout << "Nombre del producto: " << producto.nombre << endl;
            cout << "Codigo del producto: " << producto.codigo << endl;
            cout << "Cantidad: " << producto.existencia << endl;
            cout << "Proveedor del producto: " << producto.proveedor << endl;
            cout << "El producto tiene " << producto.descuento << "% de descuento \n";
            cout << "El producto esta: " << producto.estado << endl;
            encontrado = true;
        }
    }
    if (!encontrado) {
        cout << "Ups... ese codigo no existe\n intenta crearlo desde -> menu -> opción 1 \n";
    }
}

//Función modificadora
void modificarProducto(vector<Producto>& productos, const string& nombreArchivo) {
    string codigo;
    cout << "Escribe el codigo del producto a modificar \n";
    cin >> codigo;

    bool encontrado = false;
    for (auto& producto : productos) {
        if (producto.codigo == codigo) {
            encontrado = true;
            cout << "Modificaras el proudcto No. " << producto.codigo << endl;
            cout << "Ingrese el nuevo nombre de " << producto.nombre << endl;
            cin >> producto.nombre;
            cout << "Ingrese el nuevo precio para  " << producto.precio << endl;
            cin >> producto.precio;
            cout << "Ingrese la nueva cantidad \n";
            cin >> producto.existencia;
            cout << "Que descuento tendra el nuevo producto \n";
            cin >> producto.descuento;
            cout << "Ingrese el nombre del nuevo proveedor \n";
            cin >> producto.proveedor;
            cout << "El nuevo producto esta Aprobado?\n A) APROBADO \n N) NO APROBADO\n";
            cin >> producto.estado;

            ofstream archivo(nombreArchivo);
            for (const auto& p : productos) {
                archivo << p.codigo << " " << p.nombre << " " << p.precio << " " << p.proveedor << " " << p.existencia << " " << p.estado << " " << p.descuento << endl;
            }
            archivo.close();
            cout << "Hemos modificado el producto No." << codigo << " de manera exitosa \n";
            break;

        }
    }
    if (!encontrado) {
        cout << "Lo sentimos, No encontramos un producto con el codigo " << codigo << endl;
    }
}

//MENU
void menu(const string& nombreArchivo) {
    vector<Producto> productos;
    if (archivoExiste(nombreArchivo)) {
        productos = LeerArchivo(nombreArchivo);
    }
    int opcion;
    do {
        cout << "Que desea realizar? \n";
        cout << "1.) Ingresar producto\n 2.) Buscar un producto\n 3.) Modificar productos\n 4.) SALIR \n";
        cin >> opcion;

        switch (opcion) {
        case 1:
            agregarProducto(nombreArchivo, productos);
            break;
        case 2:
            buscarProducto(productos);
            break;
        case 3:
            modificarProducto(productos, nombreArchivo);
            break;
        case 4:
            cout << "Hasta luego...";
        default:
            cout << "Esa opción no es valida";
        }
    } while (opcion != 4);
}
int main()
{
    const string nombreArchivo = "C:/Users/velas/source/repos/Proyecto_funcional/Proyecto_funcional/productos.txt";
    menu(nombreArchivo);
    return 0;
}

// Ejecutar programa: Ctrl + F5 o menú Depurar > Iniciar sin depurar
// Depurar programa: F5 o menú Depurar > Iniciar depuración

// Sugerencias para primeros pasos: 1. Use la ventana del Explorador de soluciones para agregar y administrar archivos
//   2. Use la ventana de Team Explorer para conectar con el control de código fuente
//   3. Use la ventana de salida para ver la salida de compilación y otros mensajes
//   4. Use la ventana Lista de errores para ver los errores
//   5. Vaya a Proyecto > Agregar nuevo elemento para crear nuevos archivos de código, o a Proyecto > Agregar elemento existente para agregar archivos de código existentes al proyecto
//   6. En el futuro, para volver a abrir este proyecto, vaya a Archivo > Abrir > Proyecto y seleccione el archivo .sln
