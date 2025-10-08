/**
* Proyecto SIMULACIÓN DE PELEA clase GANONDORF
* Diego Emilio Barrera Hernández
* A01366802
* 12/06/2020
* Esta clase es hija de CHARACTER y será el enemigo del juego The legend of Zelda
* aquí tiene sus propios metodos y atributos como su ataque especial y su nombre
* cuenta con una sobrescritura ShowInfoGame()
* también cabe decir que su ataque especial modifica la vida directa de su enemigo TLOZELDA
**/

#ifndef GANONDORF_H
#define GANONDORF_H
#include"TLOZELDA.h"//llamar clase TLOZELDA
#include"CHARACTER.h"//llamar clase jugador
#include<cstdlib>//para Random
#include<ctime>//para afirmar el Random
#include<iostream> //para imprimir.

using namespace std;

class GANONDORF:public CHARACTER{//CLASE GANONDORF (hija), con herencia a PERSONAJE
    private://Atributos
        //Declaro variables de instancia
        string info;
        string NameG;
        bool MagicG;
        int SmashG;
    public://Metodos
        GANONDORF(string, int, int, int, string, bool, int);
        GANONDORF(string, string);
        string ShowNameG();
        void ShowInfoGame();//metodo polimorfismo sobrescrito
        int Punch(CHARACTER &c);//Metodo donde recive &c para que los cambio se preserven
        bool GetMagicG();
};

//Constructor 1
GANONDORF::GANONDORF(string game, int dam, int tilt, int turno, string nameG, bool magicG, int smashG):CHARACTER(game, dam, tilt, turno){
    NameG=nameG;
    MagicG=magicG;
    SmashG=smashG;
}

//Constructor 2
GANONDORF::GANONDORF(string game, string information):CHARACTER(game){
    info=information;
}

/*
* ShowInfoGame()(en esta clase) es para mostrar la información del personaje GANONDORF
* también es el metodo de polimorfismo y sobrescritura de clase ABSTRACTA CHARACTER
*/
void GANONDORF::ShowInfoGame(){///metodo de polimorfismo para esta clase  y sobrescritura de clase ABSTRACTA
    cout<<"\nExtra -Ganondorf- info: ";
    cout<<info;
}

//Mostrar nombre del jugador
string GANONDORF::ShowNameG(){
    cout<<NameG;
    return NameG;
}

/*
* Punch(CHARACTER &c) dependiendo si MagicG es verdadero es para que el enemigo de TLOZELDA pueda hacer su ataque especial
* tendrá una probabilidad de que acierte el ataque o falle
* haciendole daño directamente a su enemigo con c.DamageRecive(SmashG), ya que apunta directamente a CHARACTER &c
*/
int GANONDORF::Punch(CHARACTER &c){//Apunta directamente a un objeto creado en CHARACTER
    int numm;
    srand(time(0));//Número random
    if(MagicG==true){//Si cuenta con magia(TRUE)
        numm=rand()%9;//Variable para random
        if(numm==9||numm==8||numm==7||numm==6){//pega si tiene el %40
            SmashG=100;
            c.DamageRecive(SmashG);//recive daño el objeto de CHARACTER
            cout<<"GANONDORF used DINs FIRE of "<<SmashG<<"!!!"<<endl;
        }
        else{//si es otro numero
            SmashG=0;
            c.DamageRecive(0);//recive daño el objeto de CHARACTER
            cout<<"GANONDORF Failed!!!"<<endl;
        }

    }
    else{//Si MagicG es falso
        SmashG=0;
        c.DamageRecive(SmashG);//No recive daño
    }
    return SmashG;
}

/*
* GetMagicG() sirve para regresar si su MagicG es verdadero o falso
* en caso de que el turno sea divisible entre 3 entonces sera verdadero
*/
bool GANONDORF::GetMagicG(){
    if(Turn%3==0){//Si el turno del jugador es div entre 3
        MagicG=true;//tendrá magia
    }
    else{
        MagicG=false;//sino no tendrá magia
    }
    return MagicG;
}

#endif // GANONDORF_H
