

package Ejercicio3;

import java.util.Scanner;


public class Ejercicio3 {
    
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese su calificacion: ");
        var nota = Integer.parseInt(entrada.nextLine());
        var  calificacion = "El numero no se encuentra en el rango aceptado como una calificacion";
        if (nota >= 0 && nota < 7) {
            calificacion = "D";
        } else if (nota >= 7 && nota < 8){
            calificacion = "C";
        } else if (nota >= 8 && nota < 9){
            calificacion = "B";
        } else if (nota >= 9 && nota <= 10){
            calificacion = "A";
        }
        System.out.println("calificacion = " + calificacion);
    }
    
}
