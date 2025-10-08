/**
* Proyecto SIMULACI�N DE PELEA clase TLOZELDA
* Diego Emilio Barrera Hern�ndez
* A01366802
* 12/06/2020
* Esta clase es hija de CHARACTER y ser� el h�ro del juego The legend of Zelda
* aqu� tiene sus propios metodos y atributos como su ataque especial y su nombre
* cuenta con una sobrescritura ShowInfoGame()
* tambi�n cabe decir que su ataque especial modifica la vida directa de su enemigo GANONDORF
**/

#ifndef TLOZELDA_H
#define TLOZELDA_H
#include"GANONDORF.h"//llamada de clase ganondorf
#include"CHARACTER.h"//Llamada de clase jugador
#include<cstdlib>//para Random
#include<ctime>//para afirmar el Random
#include<iostream> //para imprimir.

using namespace std;

class TLOZELDA:public CHARACTER{//CLASE TLOZELDA (hija), con herencia a PERSONAJE
    private://Atributos
        //Declaro variables de instancia
        string NameZ;
        bool MagicBar;
        int SmashT;
        string info;
        string infoPlayer;
    public://Metodos
        TLOZELDA(): NameZ(""), info(""), infoPlayer(""){};
        TLOZELDA(string, int, int, int, string, bool, int);
        TLOZELDA(string, int, int, int, string, bool, int, string);//SOBRECARGA PARA UNA SOBREESCRITURA
        TLOZELDA(string,string,string);
        void ShowInfoGame();//metodo polimorfismo y sobrescritura de clase abstracta
        string ShowNameZ();
        int Triforce(GANONDORF &g);//Metodo donde recive &g para que los cambio se preserven
        bool GetMagicBar();
};

//Constructor 1
TLOZELDA::TLOZELDA(string game, int dam, int tilt, int turno, string nameZ, bool magicBar, int smashT):CHARACTER(game, dam, tilt, turno){
    NameZ=nameZ;
    MagicBar=magicBar;
    SmashT=smashT;
}

//Constructor 2
TLOZELDA::TLOZELDA(string game, int dam, int tilt, int turno, string nameZ, bool magicBar, int smashT, string inf)
:CHARACTER(game, dam, tilt, turno){
    info=inf;
}

//Constructor 3
TLOZELDA::TLOZELDA(string game, string information, string infPlayer):CHARACTER(game){
    info=information;
    infoPlayer=infPlayer;
}

/*
* ShowInfoGame()(en esta clase) es para mostrar la informaci�n del juego del personaje y del personaje
* tambi�n es el metodo de polimorfismo y sobrescritura de clase ABSTRACTA CHARACTER
*/
void TLOZELDA::ShowInfoGame(){
    cout<<"You chose ";
    cout<<Game;
    cout<<"\nExtra game info: ";
    cout<<info<<"\n";
    cout<<"\nYou will be Link and your enemy Ganondorf"<<endl;
    cout<<"Extra -Link- info: ";
    cout<<infoPlayer;
}

//Mostrar el nombre del personaje
string TLOZELDA::ShowNameZ(){
    cout<<NameZ;
    return NameZ;
}

/*
* Triforce(GANONDORF &g), en caso de que MagicBar sea verdadera le da la opci�n al usuari� de escoger que hacer para dar un ataque especial
* tendr� una probabilidad de que acierte el ataque o que falle, tambi�n que pasar�a si decide no hacerlo
* haciendole da�o directamente a su enemigo con g.DamageRecive(SmashT), ya que apunta directamente a GANONDORF &g
*/
int TLOZELDA::Triforce(GANONDORF &g){
    int numz;
    srand(time(0));//N�mero random
    if(MagicBar==true){//Si la barra de magia esta llena(TRUE)
        int SA;//variable para selecci�n
        cout<<"Do yo want to do your Smash Attack?\n(1)YES\n(any other number)A Tilt Attack of 25"<<endl;
        cin>>SA;
        if (SA==1){//Si la selecci�n es 1
            numz=rand()%9;//Variable para random
            if (numz==0||numz==2||numz==3||numz==4||numz==5||numz==6||numz==7){//pega si tiene el 70%
                SmashT=50;
                g.DamageRecive(SmashT);
                cout<<"You used FAROREs WIND of "<<SmashT<<"!!!"<<endl;
            }
            else{//Si no cae en los numeros random
                SmashT=0;
                g.DamageRecive(SmashT);
                cout<<"You failed!!\n";
            }
        }
        else{//Si decide hacer un tilt attack
            cout<<"You chose a Tilt Attack of 25"<<endl;
            SmashT=25;
            g.DamageRecive(SmashT);
        }
    }
    else{//SINO vale 0
        SmashT=0;
        g.DamageRecive(SmashT);
    }
    return SmashT;
}

/*
* GetMagicBar() sirve para regresar si su MagicBar es verdadero o falso
* en caso de que el turno sea divisible entre 3 entonces sera verdadero
*/
bool TLOZELDA::GetMagicBar(){
    if(Turn%3==0){//Si el turno del jugador es div entre 3
        MagicBar=true;//la barra estar� llena
    }
    else{
        MagicBar=false;//sino estar� vac�a
    }
    return MagicBar;
}

#endif // TLOZELDA_H
