/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Conversiones;

/**
 * Clase que permite convertir de un valoa a otro
 * por ejemplo de dolares a yenes
 * kilometros a millas etc
 * @author bryan
 * 
 */

public  class Conversion {
    
    private final String valorPrincipal;
    private final double valorDeConversion;
    private final String valorSecundario;

    /**
     * Constructor
     * @param valorPrincipal es cuantas veces ocupo el valor principal para obtener uno del secundario
     * para más claridad vease el toString
     * @param valorSecundario
     * @param valorDeConversion 
     */
    public Conversion(String valorPrincipal, String valorSecundario, double valorDeConversion) {
        this.valorPrincipal = valorPrincipal;
        this.valorSecundario = valorSecundario;
        this.valorDeConversion = valorDeConversion;
    }
    
    /**
     * convierte el calor principal a la Secundaria
     * @param valor es la cantidad que desea convertir
     * @return valor/valorDeConversion
     */
    public double convertirPrincipalASecundario(double valor){
        return valor/valorDeConversion;
    }
    
    /**
     * convierte el vañor secundaria a la principal
     * @param valor es la cantidad que desea convertir
     * @return valor*valorDeConversion
     */
    public double convertirSecundarioAPrincipal(double valor){
        return valor*valorDeConversion;
    }

    public String getValorPrincipal() {
        return valorPrincipal;
    }

    public double getValorDeConversion() {
        return valorDeConversion;
    }

    public String getValorSecundario() {
        return valorSecundario;
    }
    
    @Override
    public String toString() {
        return valorDeConversion +" "+ valorPrincipal+ " equivale a un " + valorSecundario;
    }

    
}
