/**
* Proyecto SIMULACI�N DE PELEA clase CHARACTER
* Diego Emilio Barrera Hern�ndez
* A01366802
* 12/06/2020
* Esta clase es la padre de los proximas clases heredadas
* contiene todos los metodos que tendr�n igual cada personaje
* como es la vida, el ataque normal y el turno
* tambi�n un tiene un metodo abstracto virtual void ShowInfoGame()=0;
* para poder mostrar informacion del juego y de algo m�s dependiendo las clases hijas
**/

#ifndef CHARACTER_H
#define CHARACTER_H
#include<iostream> //para imprimir.
#include<cstdlib>//para Random
#include<ctime>//para afirmar el Random
using namespace std;

class CHARACTER{//CLASE PERSONAJE (PAP�)
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
        CHARACTER(){}//Constructor para composici�n
        virtual void ShowInfoGame()=0;///metodo para polimorfismo y CLASE ABSTRACTA
        int DamageRecive(int DamageRecive);//Metodo donde recive DamageRecive para modificar el da�o recivido
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
* DamageRecive(DamageRecive) recibe el da�o que se di�
* para que haga la suma del da�o que ten�a m�s el da�o que se di�
*/
int CHARACTER::DamageRecive(int DamageRecive){
    DamagePer = DamagePer + DamageRecive;
    return DamagePer;
}

/*
* GetTiltAttack() le da la opci�n al usuari� de escoger que hacer para dar un ataque si el turno no es divisible entre 3
* tendr� una probabilidad de que acierte un ataque normal, un ataque critico o que falle
* regresando el da�o del ataque que se haya dado
*/
int CHARACTER::GetTiltAttack(){
    if(Turn%3!=0){
        srand(time(0));//N�mero random
        int num;
        num=0;
        int cont;//Variable para la seleccion
        cout<<"Choose number 1 to attack!"<<endl;
        cout<<"1)YES"<<endl;
        cin>>cont;
        cout<<"\n";

        if(cont==1){//si la selecci�n s� es 1
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

//obtener porcentaje de da�o
int CHARACTER::GetDamagePer(){
    return DamagePer;
}

//Se utiliza para modificar, pues es el que se va a estar moviendo
void CHARACTER::SetDamagePer(int DP){
    DamagePer=DP;
}

#endif // CHARACTER_H
