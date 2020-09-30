/**
* Proyecto SIMULACIÓN DE PELEA clase CHARACTER
* Diego Emilio Barrera Hernández
* A01366802
* 12/06/2020
* Esta clase es la padre de los proximas clases heredadas
* contiene todos los metodos que tendrán igual cada personaje
* como es la vida, el ataque normal y el turno
* también un tiene un metodo abstracto virtual void ShowInfoGame()=0;
* para poder mostrar informacion del juego y de algo más dependiendo las clases hijas
**/

#ifndef CHARACTER_H
#define CHARACTER_H
#include<iostream> //para imprimir.
#include<cstdlib>//para Random
#include<ctime>//para afirmar el Random
using namespace std;

class CHARACTER{//CLASE PERSONAJE (PAPÁ)
    private://Atributos privados
        //Declaro variables de instancia
        int TiltAttack;
    protected://Atributos protegidos
        string Game;
        string info;
        int DamagePer;
        int Turn;
    public://Metodos
        CHARACTER(string, int, int, int);
        CHARACTER(string);
        CHARACTER(){}//Constructor para composición
        virtual void ShowInfoGame()=0;///metodo para polimorfismo y CLASE ABSTRACTA
        int DamageRecive(int DamageRecive);//Metodo donde recive DamageRecive para modificar el daño recivido
        int GetTiltAttack();
        int GetTurn();
        int GetDamagePer();
        void SetDamagePer(int DP);
};

//Constructor1
CHARACTER::CHARACTER(string game, int dam, int tilt, int turno){
    Game=game;
    DamagePer=dam;
    TiltAttack=tilt;
    Turn=turno;
}

//Constructor2
CHARACTER::CHARACTER(string Gam){
    Game=Gam;
}

//Obtener turno
int CHARACTER::GetTurn(){
    return Turn;
}

/*
* DamageRecive(DamageRecive) recibe el daño que se dió
* para que haga la suma del daño que tenía más el daño que se dió
*/
int CHARACTER::DamageRecive(int DamageRecive){
    DamagePer = DamagePer + DamageRecive;
    return DamagePer;
}

/*
* GetTiltAttack() le da la opción al usuarió de escoger que hacer para dar un ataque si el turno no es divisible entre 3
* tendrá una probabilidad de que acierte un ataque normal, un ataque critico o que falle
* regresando el daño del ataque que se haya dado
*/
int CHARACTER::GetTiltAttack(){
    if(Turn%3!=0){
        srand(time(0));//Número random
        int num;
        num=0;
        int cont;//Variable para la seleccion
        cout<<"Choose number 1 to attack!"<<endl;
        cout<<"1)YES"<<endl;
        cin>>cont;
        cout<<"\n";

        if(cont==1){//si la selección sí es 1
            num=rand()%11;//Variable para random
            if(num==0||num==1||num==2||num==3){//si el random es par entonces vale 25
                TiltAttack=25;
                cout<<"<Critic Tilt Attack of ";
                cout<<TiltAttack<<">\n";
                return TiltAttack;
            }
            else if(num==4||num==5||num==6||num==7){//Sino vale 15
                TiltAttack=15;
                cout<<"<Tilt Attack of ";
                cout<<TiltAttack<<">\n";
                return TiltAttack;
            }
            else{
                TiltAttack=0;
                cout<<"Failed attack!!\n";
                cout<<"<Tilt Attack of ";
                cout<<TiltAttack<<">\n";
                return TiltAttack;
            }
        }
        else{
            cout<<"You shouldnt have done that"<<endl;
            TiltAttack=0;
            cout<<"<Tilt Attack of ";
            cout<<TiltAttack<<">\n";
            return TiltAttack;

        }
    }
    return TiltAttack;
}

//obtener porcentaje de daño
int CHARACTER::GetDamagePer(){
    return DamagePer;
}

//Se utiliza para modificar, pues es el que se va a estar moviendo
void CHARACTER::SetDamagePer(int DP){
    DamagePer=DP;
}

#endif // CHARACTER_H
