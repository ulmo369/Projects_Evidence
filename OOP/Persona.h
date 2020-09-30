#ifndef PERSONA_H
#define PERSONA_H
#include"Comida.h"
#include<string>
#include<iostream> //para imprimir.
using namespace std;

class Persona{//Clase para composición
    private://Atributos
        string nombreP;
        Comida seleccion1;
    public://Metodos
        Persona(string x, int, int, int);
        void MostrInfo();
};

Persona::Persona(string x, int entrada, int bebida, int postre)//Constructor para definir la composición
{
    Comida ob(entrada,bebida,postre);
    nombreP=x;
    seleccion1=ob;

}

void Persona::MostrInfo(){//Función que te muestra la comida seleccionada por los otros objetos de la clase Comida
    cout<<"\nTu seleccion de comida "<<nombreP<<" es \n";
    seleccion1.getEntrada();
    seleccion1.getBebida();
    seleccion1.getPostre();

}

#endif
