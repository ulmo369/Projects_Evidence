/**
* Proyecto SIMULACIÓN DE PELEA clase SEPHIROTH
* Diego Emilio Barrera Hernández
* A01366802
* 12/06/2020
* Esta clase es hija de CHARACTER y será el enemigo del juego Final Fantasy
* aquí tiene sus propios metodos y atributos como su ataque especial y su nombre
* cuenta con una sobrescritura ShowInfoGame()
* también cabe decir que su ataque especial modifica la vida directa de su enemigo FINALFANTASY
**/
#ifndef SEPHIROTH_H
#define SEPHIROTH_H
#include"FINALFANTASY.h"//llamar clase FINALFANTSY
#include"CHARACTER.h"//llamar clase jugador
#include<cstdlib>//para Random
#include<ctime>//para afirmar el Random
#include<iostream> //para imprimir.

using namespace std;

class SEPHIROTH:public CHARACTER{//CLASE SEPHIROTH (hija), con herencia a PERSONAJE
    private://Atributos
        //Declaro variables de instancia
        string info;
        string NameS;
        bool LimitBreakS;
        int SmashS;
    public://Metodos
        SEPHIROTH(string, int, int, int, string, bool, int);
        SEPHIROTH(string, string);
        string ShowNameS();
        void ShowInfoGame();//metodo polimorfismo y sobrescritura de clase abstracta
        int Masamune(CHARACTER &c);//Metodo donde recive &c para que los cambio se preserven
        bool GetLimitBreakS();
};

//Constructor 1
SEPHIROTH::SEPHIROTH(string game, int dam, int tilt, int turno, string nameS, bool limitBreakS, int smashS):CHARACTER(game, dam, tilt, turno){
    NameS=nameS;
    LimitBreakS=limitBreakS;
    SmashS=smashS;
}

//Constructor 2
SEPHIROTH::SEPHIROTH(string game, string information):CHARACTER(game){
    info=information;
}

/*
* ShowInfoGame()(en esta clase) es para mostrar la información del personaje
* también es el metodo de polimorfismo y sobrescritura de clase ABSTRACTA CHARACTER
*/
void SEPHIROTH::ShowInfoGame(){
    cout<<"\nExtra -SEPHIROTH- info: ";
    cout<<info;
}

//Mostrar nombre del personaje
string SEPHIROTH::ShowNameS(){
    cout<<NameS;
    return NameS;
}

/*
* Masamune(CHARACTER &c) dependiendo si LimitBreakS es verdadero es para que el enemigo de FINALFANTASY pueda hacer su ataque especial
* tendrá una probabilidad de que acierte el ataque o falle
* haciendole daño directamente a su enemigo con c.DamageRecive(SmashS), ya que recibe un objeto CHARACTER &c
*/
int SEPHIROTH::Masamune(CHARACTER &c){//Apunta directamente a un objeto creado en CHARACTER
    int numms;
    srand(time(0));//Número random
    if(LimitBreakS==true){//Si cuenta con magia(TRUE)
        numms=rand()%9;//Variable para random
        if(numms==9||numms==8||numms==7||numms==6){//Probabilidad del 40% para asertar
            SmashS=100;
            c.DamageRecive(SmashS);//recive daño el objeto de CHARACTER
            cout<<"SEPHIROTH used his MASAMUNE of "<<SmashS<<"!!"<<endl;
        }
        else{//si el random es diferente
            SmashS=0;
            c.DamageRecive(0);//recive daño el objeto de CHARACTER
            cout<<"SEPHIROTH Failed!!!"<<endl;
        }
    }
    else{//si el turno no es divisible entre 3 entonces vale 0
        SmashS=0;
        c.DamageRecive(SmashS);//No recive daño
    }
    return SmashS;
}

/*
* GetLimitBreakS() sirve para regresar si su LimitBreakF es verdadero o falso
* en caso de que el turno sea divisible entre 3 entonces sera verdadero
*/
bool SEPHIROTH::GetLimitBreakS(){
    if(Turn%3==0){//Si el turno del jugador es div entre 3
        LimitBreakS=true;//tendrá magia
    }
    else{
        LimitBreakS=false;//sino no tendrá magia
    }
    return LimitBreakS;
}

#endif // SEPHIROTH_H
