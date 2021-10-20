// regex_search example
#include <iostream>
#include <string>
#include <regex>
#include <conio.h>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

void resaltador (string file){
  /*- - - - - - - - -
  We read the file
  - - - - - - - - - -*/
  ifstream archivo;
  ofstream output;

  output.open("res.html", ios::out); //We open the output file
  archivo.open(file, ios::in); //We open the input file
  string line;

  if (archivo.fail()){ //This could be the fail of the input file
      cout<<"THE INPUT FILE COULD NOT BE OPEN\n\n";
      exit(1);
  }

  if (output.fail()){
    cout<<"THE OUTPUT FILE COULD NOT BE OPEN\n\n";
    exit(1);
  }
  

  output << "<!DOCTYPE html>\n";
  output << "<html lang=\"en\">\n";
  output << "<head>\n";
  output << "<meta charset=\"UTF-8\">\n";
  output << "<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n";
  output << "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n";
  output << "<link rel=\"stylesheet\" href=\"colors.css\">\n";
  output << "<title>RESULTADOS</title>\n";
  output << "</head>\n";
  output << "<body>\n";


  string caracter = "";
  string n = "";
  bool correct = false;

  while (!archivo.eof()){ //While we are reading the file

    getline(archivo, line);

    for(int i = 0; i < line.size(); i++){
      
      cout << "ANALIZANDO -> " << line[i] << "\n" << endl;

      if(line[i] == '(' || line[i] == ')' || line[i] == ' '){
        cout << caracter.size() << "\n";
        cout << caracter << "\n";
        cout << "\n" << endl;
        if(caracter.size() >= 1){
          output << "<span class=\"ident\" style=\"font-size: 150%; font-weight: bold;\">" << caracter << "</span>\n";
          cout << "Identificador\n";
          cout << "\n" << endl;
          caracter = "";
        }
      }
      caracter = caracter + line[i];

      if (regex_match (caracter, regex("\\(+") )){ 
        output << "<span class=\"OpenParentesis\" style=\"font-size: 150%; font-weight: bold;\">" << caracter << "</span>\n";
        cout << "Parentesis abierto\n";
        cout << "\n" << endl;
        caracter = "";
      }

      else if(regex_match (caracter, regex("\\)+") )){
        output << "<span class=\"CloseParentesis\" style=\"font-size: 150%; font-weight: bold;\">" << caracter << "</span>\n";
        cout << "Parentesis cerrado\n";
        cout << "\n" << endl;
        caracter = "";
      }

      else if(regex_match (caracter, regex("(\\+|-|\\*|\\/|<|<=|>|>=|=|<>|\\')+") )){
        output << "<span class=\"Char\" style=\"font-size: 150%; font-weight: bold;\">" << caracter << "</span>\n";
        cout << "Simbolo reservado\n";
        cout << "\n" << endl;
        caracter = "";
      }

      else if(regex_match (caracter, regex("(;)(.)*") )){
        cout << "AQUIIII ->  " << line << "\n" << endl;
        for (int j = 0; j < line.size(); j++){

          if ( line[j] == ';'){
            correct = true;
          }
          if (correct){
            if (line[j] == ' '){
              output << "<span class=\"Comments\" style=\"font-size: 150%; font-weight: bold;\"> &nbsp </span>\n";
            }
            else{
              output << "<span class=\"Comments\" style=\"font-size: 150%; font-weight: bold;\">" << line[j] << "</span>\n";
            }
            cout << "Comentario\n";
            cout << "\n" << endl;
          }
        }
        correct = false;
        caracter = "";
        break;
      }

      else if(regex_match (caracter, regex("(define|lambda|if|cond|else|true|false|nil|car|cdr|cons|list|apply|map|let|begin|null\\?|eq\\?|set!)") )){
        output << "<span class=\"ReservedWords\" style=\"font-size: 150%; font-weight: bold;\">" << caracter << "</span>\n";
        cout << "Plabra reservada\n";
        cout << "\n" << endl;
        caracter = "";
      }

      else if(regex_match (caracter, regex("E(\\+|\\-)(\\d{5}|\\d{4}|\\d{3}|\\d{2}|\\d{1})+") )){
        output << "<span class=\"poten\" style=\"font-size: 150%; font-weight: bold;\">" << caracter << "</span>\n";
        cout << "Potencia\n";
        cout << "\n" << endl;
        caracter = "";
      }

      else if(regex_match (caracter, regex("([0-9])") )){
        output << "<span class=\"Numbers\" style=\"font-size: 150%; font-weight: bold;\">" << caracter << "</span>\n";
        cout << "Numero\n";
        cout << "\n" << endl;
        caracter = "";
      }

      else if(regex_match (caracter, regex("(\\.)") )){
        output << "<span class=\"Dott\" style=\"font-size: 150%; font-weight: bold;\">" << caracter << "</span>\n";
        cout << "Punto\n";
        cout << "\n" << endl;
        caracter = "";
      }


      else if(regex_match (caracter, regex(" ") )){
        output << "<span class=\"space\" style=\"font-size: 150%; font-weight: bold;\"> &nbsp </span>\n";
        cout << "Espacio\n";
        cout << "\n" << endl;
        caracter = "";
      }

      else if(regex_match (caracter, regex("(#|!|\"|\\$|%|&|\\?|'|¡|¿|\\|¨|´|~|\\{|\'|\\}|\\[|\\]|\\^|`|_|:|,|;)") )){
        output << "<span class=\"else\" style=\"font-size: 150%; font-weight: bold;\">" << caracter << "</span>\n";
        cout << "Desconocido\n";
        cout << "\n" << endl;
        caracter = "";
      }

    }
    output << "<br>";
  }

  output << "</body>\n";
  output << "</html>";
  output.close();
}

int main ()
{

  resaltador ("input.txt");

  return 0;
}