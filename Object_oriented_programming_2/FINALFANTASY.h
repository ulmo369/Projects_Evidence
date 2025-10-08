/**
* Proyecto SIMULACIÓN DE PELEA clase FINALFANTASY
* Diego Emilio Barrera Hernández
* A01366802
* 12/06/2020
* Esta clase es hija de CHARACTER y será el héro del juego Final Fantasy
* aquí tiene sus propios metodos y atributos como su ataque especial y su nombre
* cuenta con una sobrescritura ShowInfoGame()
* también cabe decir que su ataque especial modifica la vida directa de su enemigo SEPHIROTH
**/
#ifndef FINALFANTASY_H
#define FINALFANTASY_H
#include"SEPHIROTH.h"//llamada de clase SEPHIROTH
#include"CHARACTER.h"//Llamada de clase jugador
#include<iostream> //para imprimir.

using namespace std;

class FINALFANTASY:public CHARACTER{//CLASE FINALFANTASY (hija), con herencia a PERSONAJE
    private://Atributos
        //Declaro variables de instancia
        string NameF;
        bool LimitBreakF;
        int SmashF;
        string info;
        string infoPlayer;
    public://Metodos
        FINALFANTASY(): NameF(""), info(""), infoPlayer(""){};
        FINALFANTASY(string, int, int, int, string, bool, int);
        FINALFANTASY(string, int, int, int, string, bool, int, string);
        FINALFANTASY(string,string,string);
        void ShowInfoGame();//metodo polimorfismo y sobrescritura de clase abstracta
        string ShowNameF();
        int Mako(SEPHIROTH &s);//Metodo donde recive &s para que los cambio se preserven
        bool GetLimitBreakF();
};

//Constructor 1
FINALFANTASY::FINALFANTASY(string game, int dam, int tilt, int turno, string nameF, bool limitBreakF, int smashF):CHARACTER(game, dam, tilt, turno){
    NameF=nameF;
    LimitBreakF=limitBreakF;
    SmashF=smashF;
}

//Constructor 2
FINALFANTASY::FINALFANTASY(string game, int dam, int tilt, int turno, string nameF, bool limitBreakF, int _SmashF, string inf)
:CHARACTER(game, dam, tilt, turno){
    info=inf;
}

//Constructor 3
FINALFANTASY::FINALFANTASY(string game, string information, string infPlayer):CHARACTER(game){
    info=information;
    infoPlayer=infPlayer;
}

/*
* ShowInfoGame()(en esta clase) es para mostrar la información del juego del personaje y del personaje
* también es el metodo de polimorfismo y sobrescritura de clase ABSTRACTA CHARACTER
*/
void FINALFANTASY::ShowInfoGame(){
    cout<<"You chose ";
    cout<<Game;
    cout<<"\nExtra game info: ";
    cout<<info<<"\n";
    cout<<"\nYou will be Cloud and your enemy Sephiroth"<<endl;
    cout<<"Extra -Cloud- info: ";
    cout<<infoPlayer;
}

//Mostrar el nombre del personaje
string FINALFANTASY::ShowNameF(){
    cout<<NameF;
    return NameF;
}

/*
* Mako(SEPHIROTH &s) le da la opción al usuarió de escoger que hacer para dar un ataque especial
* tendrá una probabilidad de que acierte el ataque o falle, también que pasaría si decide no hacerlo
* haciendole daño directamente a su enemigo con s.DamageRecive(SmashF), ya que apunta directamente a SEPHIROTH &s
*/
//Obtener el ataque especial dependiendo del metodo (GetLimitBreakF)
int FINALFANTASY::Mako(SEPHIROTH &s){//apuntando directamente a la clase SEPHIROTH
    int numf;
    srand(time(0));//Número random
    if(LimitBreakF==true){//Si la barra de magia esta llena(TRUE)
        int SA;//variable para selección
        cout<<"Do yo want to do your Smash Attack?\n(1)YES\n(any other number)A Tilt Attack of 25"<<endl;
        cin>>SA;
        if (SA==1){//Si la selección es 1
            numf=rand()%9;//Variable para random
            if (numf==0||numf==2||numf==3||numf==4||numf==5||numf==6||numf==7){//Pega si tiene el 70%
                SmashF=50;
                s.DamageRecive(SmashF);
                cout<<"You used FAROREs WIND of "<<SmashF<<"!!!"<<endl;
            }
            else{//si cae en los numero random
                SmashF=0;
                s.DamageRecive(0);
                cout<<"You failed!!\n";
            }
        }
        else{//Si selecciona otro numero
            cout<<"You chose a Tilt Attack of 25"<<endl;
            SmashF=25;
            s.DamageRecive(SmashF);
        }
    }
    else{//SINO vale 0
        SmashF=0;
        s.DamageRecive(SmashF);
    }
    return SmashF;
}

/*
* GetLimitBreakF() sirve para regresar si su LimitBreakF es verdadero o falso
* en caso de que el turno sea divisible entre 3 entonces sera verdadero
*/
bool FINALFANTASY::GetLimitBreakF(){
    if(Turn%3==0){//Si el turno del jugador es div entre 3
        LimitBreakF=true;//la barra estará llena
    }
    else{
        LimitBreakF=false;//sino estará vacía
    }
    return LimitBreakF;
}

#endif // FINALFANTASY_H
