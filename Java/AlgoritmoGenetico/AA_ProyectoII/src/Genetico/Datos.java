/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Genetico;

import java.util.Collections;

/**
 *
 * @author bryan
 */
public class Datos implements Comparable<Datos>{
    int x;
    int y;
    double angle;
    int deep;
    int originalDepth;
    double base_len; 
    int largeTrunk;
    int width;
    boolean triple;
    double lGrade;
    double rGrade;
    double eGrade;
    double puntuacion;
    int id;

    public Datos() {
        x =  400;
        y = 600;
        angle = -90;
        deep = (int) (Math.random()*9 + 3);
        originalDepth = deep;
        base_len = (int) (Math.random()*51 +100)/deep; 
        largeTrunk = (int) (Math.random()*5 +1);
        width = (int) (Math.random()*2);
        if((int) (Math.random()*2) == 1)
            triple = true;
        else
            triple = false;
        lGrade = (int) (Math.random()* 241 -120);
        rGrade = lGrade*-1;
        eGrade = (lGrade + rGrade) / (int) (Math.random()*2 + 3);
        puntuacion = 0;
        id = 0;
    }

    public Datos(int x, int y, double angle, int deep, int originalDepth, double base_len, int largeTrunk, int width, boolean triple, double lGrade, double rGrade, double eGrade) {
        this.x = x;
        this.y = y;
        this.angle = angle;
        this.deep = deep;
        this.originalDepth = originalDepth;
        this.base_len = base_len;
        this.largeTrunk = largeTrunk;
        this.width = width;
        this.triple = triple;
        this.lGrade = lGrade;
        this.rGrade = lGrade*-1;
        this.eGrade = eGrade;
        puntuacion = 0;
        id = 0;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public double getAngle() {
        return angle;
    }

    public int getDeep() {
        return deep;
    }

    public int getOriginalDepth() {
        return originalDepth;
    }

    public double getBase_len() {
        return base_len;
    }

    public int getLargeTrunk() {
        return largeTrunk;
    }

    public int getWidth() {
        return width;
    }

    public boolean isTriple() {
        return triple;
    }

    public double getlGrade() {
        return lGrade;
    }

    public double getrGrade() {
        return rGrade;
    }

    public double geteGrade() {
        return eGrade;
    }

    public double getPuntuacion() {
        return puntuacion;
    }

    public void setPuntuacion(int puntuacion) {
        this.puntuacion = puntuacion;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    

    @Override
    public int compareTo(Datos datos){
        return (int) (datos.getPuntuacion() - this.puntuacion);
    }
    
}
