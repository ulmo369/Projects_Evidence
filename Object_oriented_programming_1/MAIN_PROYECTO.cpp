/*
Datos
Proyecto Reservación de Restaurante en línea
Diego Emilio Barrera Hernández
A01366802
14/11/2019
*/

/*
Descripción: Esta es la primera entrega de la clase PensamienAto Computacional Orientado a Objetos
El programa trata de una reservación a un restaurante, donde simplemente escoges tu comida, bebida y postre
también especificas el pago y especificas la sucursal y la hora; la ventaja sería que ya estaría tu comida a
la hora y en el lugar que se decidió.
*/
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Bibliotecas
#include"App.h"
#include"Pago.h"
#include"Combo.h"
#include"Comida.h"
#include"Persona.h"
#include"Reservacion.h"
#include<iostream>//para imprimir.
#include<cstdlib>//para Random
#include<ctime>//para afirmar el Random

using namespace std; //para no utilizar nuevamete std

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
int main(){
    //Bienvenida y menu de comida, bebidas, postres
    int num;
    srand(time(0));//Numero random
    num=rand()%100;//Variable para numero random
    App R1("-THE SHIRE-");//Creación de objeto para bienvenida
    App R11(num);//Creación de un segundo objeto para mostrar numero
    R1.getNombre();//Llamada del GET para el nombre
    R11.NoReserv();//Llamada de función mostrar numero
    cout<<"Como te llamas?\n";
    string nombre;//Variable para nombre
    cin>>nombre;
    cout<<"\n";
    cout<<"\nPorfavor escoga unicamente el NUMERO\n"<<endl;
    cout<<"Estas son nuestras comidas:\n1.-Sopa.....$40\n2.-Mole.....$50\n3.-Tacos(5).....$50\n4.-Chilaquiles.....$45\n5.-Pollo.....$30\n6.-Nada"<<endl;
    cout<<"Cual deseas?"<<endl;
    int entrada;
    cin>>entrada;

    cout<<"\nEstas son nuestras bebidas, TODAS A $25:\n1.-Naranjada\n2.-Limonada\n3.-CocaCola\n4.-Cerveza\n5.-Clamato\n6.-Nada"<<endl;
    cout<<"Cual deseas?"<<endl;
    int bebida;
    cin>>bebida;

    cout<<"\nEstos son nuestros postres:\n1.-Pastel.....$20\n2.-Nieve.....$10\n3.-Flan.....$30\n4.-Pie.....$20\n5.-Brownie.....$15\n6.-Nada"<<endl;
    cout<<"Cual deseas?"<<endl;
    int postre;
    cin>>postre;
    cout<<"\n";

    Persona per(nombre, entrada, bebida, postre); //Creación de objeto uno y se utiliza las variables anteriores
    per.MostrInfo();

    ////////////////////////////////////////////////
    string hora;//Variable para la hora
    string sucursal;//Variable para la sucursal
    //Pregunas de hora y lugar donde se desea comer
    cout<<"\nAhora escoge la hora y el lugar\n";
    cout<<"\n¿A que hora deceas?\n";
    cin>>hora;
    cout<<"\nEstas son nuestras sucursales:\n-Centro\n-Tec\n-Quintana\n";
    cout<<"\n¿Donde le gustaría comer?\n";
    cin>>sucursal;

    Reservacion r1;//Creación de objeto
    r1.setReservar(sucursal, hora);//LLada del SET con las variables anteriores
    r1.ConfSucursal();//Llamada de los getters
    r1.ConfHora();
//////////////////////////////////////////////////////////////////
//Especificaciones del pago, numero de tarjeta y empresa de tarjeta
    cout<<"\nAhora tienes que pagar"<<endl;
    Comida uno (entrada, bebida, postre);
    uno.cost();
    int saldo;
    srand(time(0));
    saldo=rand()%10000;
    string tarjeta;//variable de tipo de tarjeta
    int clave;//variable de clave
    long long numero;//variable para numero grande de la tarjeta
    cout<<"\n¿Que tarjeta tiene?\n";
    cin>> tarjeta;
    cout<<"\n¿Que Numero de tarjeta tiene?\n";
    cin>> numero;
    cout<<"\n¿Cual es su Clave?\n";
    cin>> clave;
    cout<<"\n............\n";
    cout<<":AUTORIZADA:\n";
    cout<<"............\n"<<endl;

    Pago p1;//Creación de objeto con numero de tarjeta y tarjeta
    Pago p11(saldo);
    p1.setPago(numero,tarjeta);
    p1.getTarjeta();//Llamada de clase con objeto
    p1.getNumero();//Llamada de clase con objeto
    p11.MostrarSaldo();//Se muestra el saldo restante
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Se pregunta si se quiere un combo, en ese caso se llama la herencia creada
    int guarnicion;//Variables para respuestas
    string resp;
    cout<<"\nPor $20 mas quisieras completar un combo con guarnicion? SI/NO"<<endl;
    cin>>resp;
    if (resp=="SI"||resp=="si"||resp=="Si"||resp=="sI"){ //if para en caso de que quiera el combo o no
        cout<<"\nEstas son nuestras guarniciones extras(escoge el numero): \n1.-Carne\n2.-Arroz\n3.-Frijoles\n4.-Papas\n5.-Queso\n6.-Nada"<<endl;
        cin>>guarnicion;
        Combo C1(entrada, bebida, postre, guarnicion);
        C1.PGuarnicion();

        //Confirmación del Codigo con la composición
        cout<<"\n";
        cout<<"\nASI QUEDO SU PEDIDO Y RESERVACION";
        cout<<"\n........................................................\n";
        C1.getGuarnicion();//Get para la guarnición
        r1.ConfSucursal();
        r1.ConfHora();//Llamada de getters de la sucursal y hora
        cout<<"\n";
        p1.getTarjeta();//Llamada de getters de Tarjeta y Numero
        p1.getNumero();
        cout<<"........................................................."<<endl;
        return 0;
    }
    else {

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //Confirmación del código completo con composición
        cout<<"\n";
        cout<<"\nASI QUEDO SU PEDIDO Y RESERVACION";

        cout<<"\n........................................................\n";
        Persona per1(nombre, entrada, bebida, postre); //Objeto creado de la selección de entradas
        per1.MostrInfo();//Mostrar la información que se escogió
        r1.ConfSucursal();
        r1.ConfHora();//Llamada de getters de la sucursal y hora
        cout<<"\n";
        p1.getTarjeta();//Llamada de getters de Tarjeta y Numero
        p1.getNumero();
        cout<<"........................................................."<<endl;
        return 0;
    }
}
