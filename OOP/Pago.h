#ifndef PAGO_H
#define PAGO_H
#include<iostream> //para imprimir.
using namespace std;

class Pago{//Segunda clase, la del pago
    private://Atributos, tipo de tarjeta y numero de tarjeta
        string tarjeta;
        long long numero;
        int saldo;
    public://Función pagar
        Pago();//Constructor
        Pago(int);//constructor2
        void setPago(long long, string); //Funcion SET del pago
        long long getNumero(); //Funciones GETTERS para número y tarjeta
        string getTarjeta();
        void MostrarSaldo();//Función para mostrar saldo
};

Pago::Pago(){//Constructor
}

Pago::Pago(int _saldo){ //Constructor 2
    saldo=_saldo;
}

void Pago::setPago(long long _numero,string _tarjeta){//Función SETTER para el numero y la tarjeta
    numero=_numero;
    tarjeta=_tarjeta;
}

long long Pago::getNumero(){ //Funcion GETTER para el numero y que te lo regrese
    cout<<" NUMERO: "<<numero<<endl;
    return numero;
}

string Pago::getTarjeta(){//Función GETTER para tipo de tarjeta y que te la regrese
    cout<<tarjeta;
    return tarjeta;
}

void Pago::MostrarSaldo(){ //Función para mostrar saldo
    cout<<"Tu saldo restante es de $"<<saldo<<"\n";

}
#endif
