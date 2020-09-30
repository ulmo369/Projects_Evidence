/**
* Datos
* Proyecto SIMULACIÓN DE PELEA
* Diego Emilio Barrera Hernández
* A01366802
*
* Descripción:
* Esta es la ultima entrega de la clase Programación Orientado a Objetos.
* El programa nos muestra una simulación de un juego de pelea, dónde tu eres el que
* interactúa para que la batalla siga avanzando.
* Serás un héroe de cualquier juego y vencerás al Jefe Final de ese juego.
* Solo tienes un Tilt Attack y un Smash Attack
* El Tilt Attack puede fallar o puede ser un ataque crítico, pero solo es un 30% tener eso
* Y el Smash Attack se cargará cada tres turnos, el jefe tiene un 30% de pegar y el heroe un 70%.
* Smash Attack del jefe=100 y Smash Attack del héroe tu lo puedes escoger, tal vez de 50 o tal vez de 25
* Cuando tú y tu oponente alcanzan el %300 de su daño, el juego terminará
* El ganador será el jugador que tenga menos porcentaje de daño al final de la partida.
*/

//se llaman las clases creadas
#include"GAME.h"
#include"CHARACTER.h"
#include"TLOZELDA.h"
#include"GANONDORF.h"
#include"FINALFANTASY.h"
#include"SEPHIROTH.h"
#include<conio.h>//para el getch()
#include<iostream>//para imprimir

using namespace std; //para no utilizar nuevamete std

int main(){
    //SE CREA EL OBJETO DE LA CLASE SMASH Y SE DA LA BIENVENIDA
    GAME smash("--PokeSmash--", "version:POO2");
    smash.welcome();
    cout<<smash.getname()<<"\n";
    cout<<smash.getversion()<<"\n"<<endl;
    cout<<" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __"<<endl;
    cout<<"|                                              -RULES-                                                 |"<<endl;
    cout<<"|You will be a hero of any game and you will need to defeat the Final Boss of that game                |"<<endl;
    cout<<"|You only have a Tilt Attack and Smash Attack                                                          |"<<endl;
    cout<<"|You can fail the Tilt Attack or it can be a Critic Attack, but you have only a 30% of having that     |"<<endl;
    cout<<"|And the Smash Attack will be charged every three turns, the boss have a 40% to hit and the hero a 70% |"<<endl;
    cout<<"|The Boss Smash Attack=100 and you can choose the Hero Smash Attack, maybe of 50 or maybe of 25        |"<<endl;
    cout<<"|When you and your opponent reach the %300 of damage the game will end                                 |"<<endl;
    cout<<"|The winner will be the player that has less damage percentage                                         |"<<endl;
    cout<<"|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __|"<<endl;
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    cout<<"\nWhich game do you want? (1)THE LEGEND OF ZELDA or (2)FINAL FANTASY"<<endl;
    int saga;
    cin>>saga;
    cout<<"\n";
    /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    if (saga==1){//Si se escoge THE LEGEND OF ZELDA

        cout<<"\n";
        cout<<"L E T - S T A R T!"<<endl;
        smash.agregarTLOZ();
        cout<<"\n";      ///METODOS QUE CONTIENEN EL POLIMORFISMO Y LA COMPOSICIÓN
        smash.mostrarTLOZ();
        cout<<"\n"<<endl;

        ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        cout<<"------------------------------------------------------------------------------------------------------------------------"<<endl;

        int GD=0;
        int LD=0;//variables para el ciclo y el ataque especial
        int turn=0;

        while(GD<300||LD<300){//CICLO PARA LA SOMULACIÓN DE PELEA
            turn++;
            //se crean los objetos para la pelea
            TLOZELDA link ("The Legend Of Zelda", LD, 15, turn, "LINK", false, 0);//se utilizó el primer constructor(SOBRECARGA)
            GANONDORF ganon ("The Legend Of Zelda", GD, 15, turn, "GANONDORF", false, 0);
            cout<<"--TURN:"<<link.GetTurn()<<"--"<<endl;//se muestra el turno
            cout<<"\n";
            cout<<"It is your turn"<<endl;
            link.GetMagicBar();//Llamada para el ataque especial
            link.Triforce(ganon);//Llamada para el ataque especial

            GD=ganon.DamageRecive(link.GetTiltAttack());//para mostrar y actualizar la vida

            cout<<"\n";
            cout<<"Now Ganondorfs Turn"<<endl;
            ganon.GetMagicG();//Llamada para el ataque especial
            ganon.Punch(link);//Llamada para el ataque especial

            LD=link.DamageRecive(ganon.GetTiltAttack());//para mostrar y actualizar la vida

            //para mostrarnos la vida de los personajes
            cout<<" _ _ _ _ _ _ _ _ _ _ _ _"<<endl;
            cout<<"|GANONDORFs DAMAGE %"<<ganon.GetDamagePer()<<"  |"<<endl;
            cout<<"|LINKs DAMAGE %"<<link.GetDamagePer()<<"       |"<<endl;
            cout<<"|_ _ _ _ _ _ _ _ _ _ _ _|";
            cout<<"\n";
            cout<<"------------------------------------------------------------------------------------------------------------------------";

            }

        if(GD<LD){//Si gana el jefe
            cout<<"GAME!\n";
            cout<<"You have met with a terrible fate!!\nHavent you?\nTHE DARK MASTER WINS!!"<<endl;
        }

        else if(LD<GD){//si gana el heroe
            cout<<"GAME!\n";
            cout<<"One more time you save Hyrule!! YOU WIN!!"<<endl;
        }
        else{//si quedan empate
            cout<<"\n";
            cout<<"OH MY GOSH!! IT WAS A TIE!\nMay be you can win in the next game"<<endl;
        }

}
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    else if(saga==2){//Si escoge final fantasy
        cout<<"\n";
        cout<<"L E T - S T A R T!"<<endl;
        smash.agregarFF();
        cout<<"\n";      ///METODOS QUE CONTIENEN EL POLIMORFISMO Y LA COMPOSICIÓN
        smash.mostrarFF();
        cout<<"\n"<<endl;
        /////////////////////////////////5//////////////////////////////////////////////////////////////////////////////////////

        cout<<"\n";
        cout<<"------------------------------------------------------------------------------------------------------------------------"<<endl;

        int GD=0;
        int LD=0;//variables para el ciclo y el ataque especial
        int turn=0;

        while(GD<300||LD<300){//CICLO PARA LA SOMULACIÓN DE PELEA
            turn++;
            //se crean los objetos para la pelea
            FINALFANTASY cloud ("Final Fantasy", LD, 15, turn, "CLOUD", false, 0);//se utilizó el primer constructor(SOBRECARGA)
            SEPHIROTH sephiroth ("Final Fantasy", GD, 15, turn, "SEPHIROTH", false, 0);
            cout<<"--TURN:"<<cloud.GetTurn()<<"--"<<endl;//se muestra la pelea
            cout<<"\n";
            cout<<"It is your turn"<<endl;
            cloud.GetLimitBreakF();//Llamada para el ataque especial
            cloud.Mako(sephiroth);//Llamada para el ataque especial

            GD=sephiroth.DamageRecive(cloud.GetTiltAttack());//para mostrar y actualizar la vida

            cout<<"\n";
            cout<<"Now Sephiroths Turn"<<endl;
            sephiroth.GetLimitBreakS();//Llamada para el ataque especial
            sephiroth.Masamune(cloud);//Llamada para el ataque especial

            LD=cloud.DamageRecive(sephiroth.GetTiltAttack());//para mostrar y actualizar la vida

            //para mostrarnos la vida de los personajes
            cout<<" _ _ _ _ _ _ _ _ _ _ _ _"<<endl;
            cout<<"|SEPHIROTHs DAMAGE %"<<sephiroth.GetDamagePer()<<"  |"<<endl;
            cout<<"|CLOUDs DAMAGE %"<<cloud.GetDamagePer()<<"       |"<<endl;
            cout<<"|_ _ _ _ _ _ _ _ _ _ _ _|";
            cout<<"\n";
            cout<<"------------------------------------------------------------------------------------------------------------------------";

            }

        if(GD<LD){//Si gana el jefe
            cout<<"GAME!\n";
            cout<<"Your brother in law won\nSEPHIROTH WON!!"<<endl;
        }

        else if(LD<GD){//si gana el heroe
            cout<<"GAME!\n";
            cout<<"Maybe now you can decide into Tiffany or Aerith\n CLOUD WON!!"<<endl;
        }
        else{//si quedan empate
            cout<<"\n";
            cout<<"OH MY GOSH!! IT WAS A TIE!\nMay be you can win in the next game"<<endl;
        }
    }
    /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    getch();
    return 0;
}
