/**
* Proyecto SIMULACIÓN DE PELEA clase GAME
* Diego Emilio Barrera Hernández
* A01366802
* 12/06/2020
* Esta clase contiene los objetos creados de los personajes heredados en la clase CHARACTER (composición)
* A parte de que tiene sus metodos propios de bienvenida y mostrar sus datos
**/

#ifndef GAME_H //se establece para la clase
#define GAME_H
#include "CHARACTER.h" //se establece para composición
#include "TLOZELDA.h" //se establece para composición
#include"FINALFANTASY.h" //se establece para composición
#include"SEPHIROTH.h" //se establece para composición
#include<iostream> //para imprimir.

using namespace std;

const int MAX = 1000;//Se crea una variable constante para utilizarla en el arreglo

class GAME{//CLASE JUEGO
    //Declaro variables de instancia
    private://atributos
        string nameG;
        string version;
        CHARACTER *character[MAX];//se define como apuntador para usar polimorfismo
    public://metodos
        GAME(string NameG, string ver);
        void agregarTLOZ();
        void mostrarTLOZ();
        void agregarFF();
        void mostrarFF();
        void welcome();
        string getname();
        string getversion();
};

//Constructor 1
GAME::GAME(string NameG, string ver){
    nameG=NameG;
    version=ver;
}

//obtener nombre
string GAME::getname(){
    return nameG;
}

//obtener version
string GAME::getversion(){
    return version;
}

//bienvenida al juego
void GAME::welcome(){
    cout<<"¡WELCOME! \nAND THIS IS!!"<<endl;
}

/*
* agregarTLOZ() crean objetos en CHARACTER[]
* Genera objetos de tipo GANONDORF y TLOZELDA y los
* guarda en la varibale de instancia en character[] (arreglo de CHARACTERS)
*/
void GAME::agregarTLOZ(){
    //new crea el objeto en tiempo de ejecución para usar polimorfismo
    int jugadores=0;
    character[jugadores] = new TLOZELDA ("THE LEGEND OF ZELDA", "Best Game in the world","The one without a fary");///POLIMORFISMO COMPOSICIÓN
    jugadores++;
    character[jugadores] = new GANONDORF ("THE LEGEND OF ZELDA", "Dark master and the one with millions sisters");
    jugadores++;
}

/*
* mostrarTLOZ()sirve para que al momento de llamarlo en el main
* el ciclo que recorra el arreglo e imprima cada objeto.
*/
void GAME::mostrarTLOZ(){
  //Ciclo que recorre el arreglo e imprime cada objeto.
	for(int i=0; i<2 ;i++){
        if (character[i]!=NULL){
            character[i]->ShowInfoGame();
        }
	}
}

/*
* agregarFF() crean objetos en CHARACTER[]
* Genera objetos de tipo FINALFANTASY y SEPHIROTH y los
* guarda en la varibale de instancia en character[] (arreglo de CHARACTERS)
*/
void GAME::agregarFF(){
    int jugadores=0;
    character[jugadores] = new FINALFANTASY ("FINAL FANTASY", "Best remake in the E3 of 2019","Soldier 1st class");///POLIMORFISMO COMPOSICIÓN
    jugadores++;
    character[jugadores] = new SEPHIROTH ("FINAL FANTASY", "In fact, he don't has limit break and he is Aeriths brother");
    jugadores++;

}

/*
* mostrarFF()sirve para que al momento de llamarlo en el main
* el ciclo que recorra el arreglo e imprima cada objeto.
*/
void GAME::mostrarFF(){
  //Ciclo que recorre el arreglo e imprime cada objeto.
	for(int i=0; i<2 ;i++){
        if (character[i]!=NULL){
            character[i]->ShowInfoGame();
        }
	}
}

#endif // GAME_H
