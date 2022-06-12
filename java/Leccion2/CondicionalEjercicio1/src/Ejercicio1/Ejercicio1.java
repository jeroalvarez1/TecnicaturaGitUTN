
package Ejercicio1;

import java.util.Scanner;


public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un mes del año: ");
        var mes = Integer.parseInt(entrada.nextLine());
        var estacion = "";
        
        if (1 <= mes && mes <= 3) {
            estacion = "Verano";
        } else if(4 <= mes && mes <= 6){
            estacion = "Otoño";
        } else if(7 <= mes && mes <= 9){
            estacion = "Invierno";
        } else if(10 <= mes && mes <= 12){
            estacion = "Primavera";
        } else{
            estacion = "El numero no corresponde a una estacion del año";
        }
        System.out.println("estacion = " + estacion);
    }
}
