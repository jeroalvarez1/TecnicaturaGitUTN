/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package CalcularSalario;

import java.util.Scanner;

/**
 *
 * @author jeroa
 */
public class CalcularSalario {

    public CalcularSalario() {
        super();
    }
    
    
    
    private static Scanner scanner = new Scanner(System.in);
    private static Float horas = 0F;
    private static Float precioHora = 0F;
    
    public static void main(String[] args) {
        
        System.out.println("Ingrese la cantidad de horas que ha realizado esta semana: ");
        horas = Float.parseFloat(scanner.nextLine());
        
        System.out.println("Ingrese el valor de la hora");
        precioHora = Float.parseFloat(scanner.nextLine());
        
        System.out.println("El salario es de: $" + calcular(horas, precioHora));
    }
    
    public static Float calcular(Float horas, Float precioHora){
        return horas * precioHora;
    }
}
