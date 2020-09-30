#ifndef COMIDA_H
#define COMIDA_H
#include<iostream> //para imprimir.
using namespace std; //para no utilizar nuevamete std

class Comida{ //Primera clase, la de la comida
    private://Atributos
        int entrada;
        int bebida;                                          //herencia
        int postre;
    public://Funciones de la clase
        Comida(int, int, int);//Constructor
        Comida(){}
        int getEntrada();
        int getBebida();
        int getPostre();
        void cost();
} ;

Comida::Comida(int _entrada, int _bebida, int _postre){//Constructor para los atributos
    entrada=_entrada;
    bebida=_bebida;
    postre=_postre;
}

int Comida::getEntrada(){
    switch(entrada){
        case 1:
            cout<<"De entrada: SOPA\n";
            break;
        case 2:
            cout<<"De entrada: MOLE\n";
            break;
        case 3:
            cout<<"De entrada: TACOS\n";
            break;
        case 4:
            cout<<"De entrada: CHILAQUILES\n";
            break;
        case 5:
            cout<<"De entrada: POLLO\n";
            break;
        default:
            cout<<"De entrada: NADA\n";
}
    return entrada;
}

int Comida::getBebida(){
    switch(bebida){
        case 1:
            cout<<"De bebida: NARANJADA\n";
            break;
        case 2:
            cout<<"De bebida: LIMONADA\n";
            break;
        case 3:
            cout<<"De bebida: COCA COLA\n";
            break;
        case 4:
            cout<<"De bebida: CERVEZA\n";
            break;
        case 5:
            cout<<"De bebida: CLAMATO\n";
            break;
        default:
            cout<<"De bebida: NADA\n";
}
    return bebida;
}

int Comida::getPostre(){
    switch(postre){
        case 1:
            cout<<"De postre: PASTEL\n";
            break;
        case 2:
            cout<<"De postre: NIEVE\n";
            break;
        case 3:
            cout<<"De postre: FLAN\n";
            break;
        case 4:
            cout<<"De postre: PIE\n";
            break;
        case 5:
            cout<<"De postre: BROWNIE\n";
            break;
        default:
            cout<<"De postre: NADA\n";
    }
    return postre;
}

void Comida::cost(){
int pago;
pago=0;
    switch(entrada){
        case 1:
            pago=pago+40;
            break;
        case 2:
            pago=pago+50;
            break;
        case 3:
            pago=pago+50;
            break;
        case 4:
            pago=pago+45;
            break;
        case 5:
            pago=pago+30;
            break;
        default:
            pago=pago+0;
            break;
    }

    switch(bebida){
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
            pago=pago+25;
            break;
        default:
            pago=pago+0;
            break;
    }

    switch(postre){
        case 1:
            pago=pago+20;
            break;
        case 2:
            pago=pago+10;
            break;
        case 3:
            pago=pago+30;
            break;
        case 4:
            pago=pago+20;
            break;
        case 5:
            pago=pago+15;
            break;
        default:
            pago=pago+0;
            break;
    }
    cout<<"Debes pagar: $"<<pago<<"\n";
    }

#endif
