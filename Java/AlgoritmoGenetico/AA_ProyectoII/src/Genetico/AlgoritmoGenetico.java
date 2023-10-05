/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Genetico;

import Source.Make_Evaluate;
import java.util.ArrayList;
import java.util.Arrays;

/**
 *
 * @author bryan
 */
public class AlgoritmoGenetico {
    
    Datos[] poblacion;
    ArrayList<Datos> poblacionDescartada;

    public AlgoritmoGenetico(int poblacionInicial) {
        poblacion = new Datos[poblacionInicial];
        poblacionDescartada = new ArrayList();
    }
    
    public void ejecutar(String modelPath, String fractalPath){
        int poblacionRemplazable = (poblacion.length/2);
        
        for (int i = 0; i < poblacion.length; i++) {
            poblacion[i] = new Datos();
        }
        
        while (true) {     
            
            for (int i = 0; i < poblacion.length; i++) {
                
                Datos datos = poblacion[i];
                double grade = Make_Evaluate.selection(modelPath, fractalPath,datos.getX(),datos.getY(),datos.getAngle(),datos.getDeep(),
                datos.getOriginalDepth(),datos.getBase_len(),datos.getLargeTrunk(),datos.getWidth(),datos.isTriple(),datos.getlGrade()
                ,datos.getrGrade(),datos.geteGrade());
                datos.setPuntuacion((int) grade);
            }
            
            Arrays.sort(poblacion);
            
            if (poblacion[0].getPuntuacion() >= 60) {
                break;                
            }
            
            int temp = poblacionRemplazable;
            while(temp>0){
                int id = poblacion.length - temp + 1;
                poblacion[id].setId(poblacionDescartada.size());
                poblacionDescartada.add(poblacion[id]);
                
                temp-=1;
            }
            
            int puntoMedio = poblacionRemplazable + 1;
            
            ArrayList<Datos> tempD = new ArrayList();
            
            for (int i = 0; i < puntoMedio; i++) {
                int d = (int) (Math.random()* poblacion.length);
                
                tempD.add(cruce(poblacion[i], poblacion[d]));
            }
            
            temp = poblacionRemplazable;
            int arrayI = 0;
            
            while(temp>0){
                int id = poblacion.length - temp + 1;
                poblacion[id] = tempD.get(arrayI);
                
                arrayI++;                
                temp-=1;
            }
        }
        
        
        
    }
    
    private Datos cruce (Datos d1, Datos d2){
        
        int datosCambiados = (int) (Math.random()* 13);
        int mutaciones = (int) (Math.random()* 10);
        int x = 0;
        int y = 0;
        double angle = 0;
        int deep = 0;
        int originalDepth = 0;
        double base_len = 0; 
        int largeTrunk = 0;
        int width = 0;
        boolean triple = false;
        double lGrade = 0;
        double rGrade = 0;
        double eGrade = 0;
        
        
        int i = 0;
        Datos temp = d1;
        while(i<13){            
            if(i>datosCambiados)
                temp= d2;
            int muta = (int) (Math.random()* 2);
            switch(i){
                case 1:
                    x = temp.getX();
                    break;
                case 2:
                    y = temp.getY();
                    break;
                case 3:
                    angle = temp.getAngle();
                    break;
                case 4:
                    deep = temp.getDeep();
                    if(mutaciones > 7 && muta == 1){
                        deep = (int) (Math.random()*9 + 3);
                        mutaciones--;
                    }
                    break;
                    
                case 5:
                    originalDepth = deep;
                    break;
                case 6:
                    base_len = temp.getBase_len();
                    if(mutaciones > 7 && muta == 1){
                        base_len = (int) (Math.random()*51 +100)/deep; 
                        mutaciones--;
                    }
                    break;
                case 7:
                    largeTrunk = temp.getLargeTrunk();
                    if(mutaciones > 7 && muta == 1){
                        largeTrunk = (int) (Math.random()*5 +1);
                        mutaciones--;
                    }
                    break;
                case 8:
                    width = temp.getWidth();
                    if(mutaciones > 7 && muta == 1){
                        width = (int) (Math.random()*2);
                        mutaciones--;
                    }
                    break;
                case 9:
                    triple = temp.isTriple();
                    if(mutaciones > 7 && muta == 1){
                        triple = !temp.isTriple();
                        mutaciones--;
                    }
                    break;
                case 10:
                    lGrade = temp.getlGrade();
                    if(mutaciones > 7 && muta == 1){
                        lGrade = (int) (Math.random()* 241 -120);
                        mutaciones--;
                    }
                    break;
                case 11:
                    rGrade = temp.getrGrade();
                    break;
                case 12:
                    eGrade = temp.geteGrade();
                    if(mutaciones > 7 && muta == 1){
                        eGrade = (lGrade + rGrade) / (int) (Math.random()*2 + 3);
                        mutaciones--;
                    }
                    break;

            }
            i++;
            
        }
            
        return new Datos(x, y, angle, deep, originalDepth, base_len, largeTrunk, width, triple, lGrade, rGrade, eGrade);
   
    }

    public Datos[] getPoblacion() {
        return poblacion;
    }

    public ArrayList<Datos> getPoblacionDescartada() {
        return poblacionDescartada;
    }
    
}
