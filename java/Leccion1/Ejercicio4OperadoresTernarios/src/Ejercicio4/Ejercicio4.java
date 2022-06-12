/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ejercicio4;

/**
 *
 * @author jeroa
 */
public class Ejercicio4 {
    //Operador ternario
    public static void main(String[] args) {
        
        var resultadoT = (5 > 8) ? "Verdadero" : "Falso";   
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 4;
        resultadoT = (numeroT % 2 == 0) ? "Par" : "Impar";
        System.out.println("resultadoT = " + resultadoT);
    }
}
