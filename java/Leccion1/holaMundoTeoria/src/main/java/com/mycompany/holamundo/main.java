/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.holamundo;

import java.util.Scanner;

/**
 *
 * @author jeroa
 */
public class main {

    public static void main(String[] args) {

        /*
        System.out.println("Hola Mundo Desde Java");
        
                int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
        
        
        var miVariableEnter = 10;
        var miVariableCadena = "Seguimos estudiando";
        System.out.println("miVariableEnter = " + miVariableEnter);
        System.out.println("miVariableCadena = " + miVariableCadena);*/
        //soutv + tab
        //Reglas para definir una variable en java
        //El primer caracter es con minuscula
        //No se pueden utilizar numeros como primer caracter de nuestra variable
        //las variables no pueden tener carecteres especiales
        //Si puede tener _ 
        //Se puede usar el signo del dolar
        //Se puede usar acento pero no es recomendable

        //Ejercicio de concatenacion
        /*var usuario = "Jero";
        var titular = "Tecnico";
        var union = titular + " " + usuario;
        System.out.println("union = " + union);

        var a = 8;
        var b = 4;
        var resultado = a + b;
        //con los paraentesis da prioridad de´realizacion
        System.out.println(usuario + " " + (a + b));

        //Ehercicio: Caracteres especiales Java
        var nombre = "Piter";
        System.out.println("Nueva linea: " + "\n" + nombre); //salto de linea
        System.out.println("Tabulador: \t" + nombre); //da una taburacion
        System.out.println("\t.:Menu:.");
        System.out.println("Retroceso: \b\b" + nombre); //caracter de retroceso(borra espacios hacia atras)
        System.out.println("Comillas simples: \'" + nombre + "\'"); //muestra comillas simple en cadena de texto
        System.out.println("Comillas dobles: \"" + nombre + "\""); //muestra comillas doble en cadena de texto
         */
        //clase Scaner 
        //sirve para pedirle al usaurio que ingrese un valor en una variable
        /*System.out.println("Ingres su nombre: ");
        Scanner entrada = new Scanner(System.in);
        var usuario2 = entrada.nextLine(); //next line detine la ejecucion del programa, y espera que el usuario presione enter, luego continua el programa.Lee una linea completa de la consola
        System.out.println("Usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Titulo = " + titulo2);
        System.out.println("resultado: " + titulo2 + " " + usuario2);*/
        /*
        byte numEnteroByte = (byte)1273;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte: " + Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte: " + Byte.MAX_VALUE);
        
        short numEnteroShort = 3276;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del Short: " + Short.MIN_VALUE);
        System.out.println("Valor maximo del Short: " + Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del Int: " + Integer.MIN_VALUE);
        System.out.println("Valor maximo del Int: " + Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del Long: " + Long.MIN_VALUE);
        System.out.println("Valor maximo del Long: " + Long.MAX_VALUE);
        */
        /*
        float numFloat = 3.4028235E38F; // or float numFloat = (float)3.4028235E38;
        System.out.println("numFloat = " + numFloat);
        System.out.println("Valor minimo del Float: " + Float.MIN_VALUE);
        System.out.println("Valor maximo del Float: " + Float.MAX_VALUE);
        
        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble = " + numDouble);
        System.out.println("Valor minimo del Double: " + Double.MIN_VALUE);
        System.out.println("Valor maximo del Double: " + Double.MAX_VALUE);
        
        //Inferencia de tipos var y tipos primitivos
        var numEntero = 20; //Las literales sin punto automaticamente son de tipo int
        
        System.out.println("numEntero = " + numEntero);
        
        var numFloat = 10.0F; //Automaticamente con el punto se trnasforma en tipo double
        
        System.out.println("numFloat = " + numFloat);
        
        var numDouble = 10.0;
        
        System.out.println("numDouble = " + numDouble);
         */
/*
        //Tipos primitivos char
        
        char mivarChar = 'a';
        System.out.println("miVariableChar = " + mivarChar);

        char varDeTIpoCaracter = '\u0024'; //Indicamos a Java la asignacion con el codigo unicode
        System.out.println("varCaracter = " + varDeTIpoCaracter);
        char varCaracterDecimal = 36; //Valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$'; //Un Caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);

        var varCaracter1 = '\u0024'; //Indicamos a Java la asignacion con el codigo unicode
        System.out.println("varCaracter1 = " + varCaracter1);
        var varCaracterDecimal1 = (char) 36; //Valor Entero y le asigna un tipo int
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$'; //Un Caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);

        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar);

        //Tipos primitivos tipos booleanos
        var varBool = false;
        System.out.println("varBool = " + varBool);

        if (varBool) {
            System.out.println("La bandera es verde");
        } else {
            System.out.println("La bandera es roja");
        }

        //Algoritmo: Mayor de edad
        var edad = 20;
        //var adulto = edad >= 18; 
        if (edad >= 18) {
            System.out.println("Eres mayor de edad");
        } else {
            System.out.println("Eres menor de edad");
        }

        //Conversion de  tipos primitivos
        var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI = " + valorPI);

        ////Pedir un valor
        var entrada = new Scanner(System.in);
        System.out.println("Digite su edad:");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("edad = " + edad);

        //Conversion de tipos primitivos en Java PArte 2
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);

        var fraseChar = "programadores".charAt(4);
        System.out.println("fraseChar = " + fraseChar);

        System.out.println("Digite un caracter: ");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = " + fraseChar);
        
        var nombre = "Ariel";
        System.out.println(nombre);
        nombre = "Pablo";
        System.out.println(nombre);
        String color;
        System.out.println(color);
        color = "azul";
        
        String TituloLibro = "A";
        String tituloLibro = "B";
        String titulolibro = "C";

        int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("solucion de la suma = " + solucion);

        solucion = num1 - num2;
        System.out.println("solucion de la resta = " + solucion);

        solucion = num1 * num2;
        System.out.println("solucion de la multiplicación = " + solucion);

        solucion = num1 / num2;
        System.out.println("solucion de la división = " + solucion);

        var solucion2 = 3.4 / num2;
        System.out.println("solucion2 resultado de la división = " + solucion2);

        solucion = num1 % num2; //Guarda el residuo entero de la division
        System.out.println("solucion = " + solucion); // 5/4

        if (num1 % 2 == 0) {
            System.out.println("Es un número Par");
        } else {
            System.out.println("Es un número Impar");
        }

        int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2; //Una operación
        System.out.println("varNum3 = " + varNum3);

        varNum1 += 1;
        System.out.println("varNum1 = " + varNum1);

        varNum2 -= 2;
        System.out.println("varNum2 = " + varNum2);
        varNum1 *= 5;
        System.out.println("varNum1 = " + varNum1);
        varNum3 /= 4;
        System.out.println("varNum3 = " + varNum3);
        varNum1 %= 6;
        System.out.println("varNum1 = " + varNum1);

        //Operadores UNarios: Cambio de Signo
        var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB); //El resultado será un número negativo

        //Operador de Negación
        var varC = true; //Esta literal por default en Java es de tipo boolean
        var varD = !varC; //Aqui esta invirtiendo el valor
        System.out.println("varD = " + varD);

        //Operadores Unarios de Incremento: Preincremento
        var varE = 9;
        var varF = ++varE;
        //Primero se incrementa la variable y despues se usa su valor
        System.out.println("varE = " + varE); 
        System.out.println("varF = " + varF); 

        //Postincremento (el simbolo va despues de la variable)
        var varG = 3;
        var varH = varG++; 
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);

        //Operadores Unarios de decremento: Predecremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI);
        System.out.println("varJ = " + varJ);

        //Postdecremento
        var varK = 8;
        var varL = varK--; 
        System.out.println("varK = " + varK);
        System.out.println("varL = " + varL);

        //Operadores de igualdad y Relacionales
        var aNum = 5;
        var bNum = 5;
        var cNum = (aNum == bNum);
        System.out.println("cNum = " + cNum);

        var dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);

        var cadenaA = "Hello";
        var cadenaB = "bye bye";
        var cVar = cadenaA == cadenaB;
        System.out.println("cVar = " + cVar);

        var fVar = cadenaA.equels(cadenaB);
        System.out.println("fVar = " + fVar);

        var gVar = aNum != bNum;
        System.out.println("gVar = " + gVar);

        if (aNum % 2 == 0) {
            System.out.println("El numero es Par");
        } else {
            System.out.println("El numero es Impar");
        }

        var edad = 15;
        var adulto = 18;
        if (edad >= adulto) {
            System.out.println("Es mayor de edad");
        } else {
            System.out.println("Es menor de edad");
        }
        var valorA = 11;
        var valorMinimo = 0; 
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <= 10;

        if (respuesta) {
            System.out.println("Esta dentro del rango establecido");
        } else {
            System.out.println("Esta fuera del rango establecido");
        }

        var vacaciones = false;
        var diaLibre = true;
        if (vacaciones || diaLibre) {
            System.out.println("Papá puede asistir al juego de su hijo");
        } else {
            System.out.println("Papá no puede asistir al juego de su hijo");
        }

        //Operador Ternario
        var resultadoT = (5 > 8) ? "verdadero" : "Falso";
        System.out.println("resultadoT = " + resultadoT);

        var numeroT = 4;
        resultadoT = (numeroT % 2 == 0) ? "Es par" : "Es Impar";
        System.out.println("resultadoT = " + resultadoT);

        var x = 5;
        var y = 10;
        var z = ++x + y;
        System.out.println("x = " + x); 
        System.out.println("y = " + y); 
        System.out.println("z = " + z); 

        var solucionA = 4 + 5 * 6 / 3; 
        System.out.println("solucionA = " + solucionA);

        solucionA = (4 + 5) * 6 / 3;  
        System.out.println("solucionA = " + solucionA);
*/

       
    }
}