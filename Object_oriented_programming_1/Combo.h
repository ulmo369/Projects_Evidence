#ifndef COMBO_H
#define COMBO_H
#include<iostream> //para imprimir.
#include<cstdlib>
#include<ctime>
#include<stdlib.h>
#include"Comida.h"

using namespace std; //para no utilizar nuevamete std

class Combo: public Comida{ //Clase nueva con herencia hacia Comida
    private://Atributos
        int guarnicion;
    public://Metodos
        Combo(int, int, int, int);
        int getGuarnicion();
        void PGuarnicion();
};

Combo::Combo(int _entrada, int _bebida, int _postre, int _guarnicion):Comida(_entrada, _bebida, _postre){//Constructor
    guarnicion=_guarnicion;
}

int Combo::getGuarnicion(){ //Función para recivir la guarnición deseada
    getEntrada();
    getBebida();
    getPostre();
    switch(guarnicion){
        case 1:
            cout<<"De guarnicion: CARNE\n";
            break;
        case 2:
            cout<<"De guarnicion: ARROZ\n";
            break;
        case 3:
            cout<<"De guarnicion: FRIJOLES\n";
            break;
        case 4:
            cout<<"De guarnicion: PAPAS\n";
            break;
        case 5:
            cout<<"De guarnicion: QUESO\n";
            break;
        default:
            cout<<"De guarnicion: NADA\n";
}
    return guarnicion;
}

void Combo::PGuarnicion(){//Función para el pago extra por la guarnición
    int pagog;
    pagog=0;

        switch(guarnicion){
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
            pagog=pagog+20;
            break;
        default:
            pagog=pagog+0;
            break;
}
    cout<<"Se cargaran $"<<pagog<<" mas a tu tarjeta\n";
}

#endif
