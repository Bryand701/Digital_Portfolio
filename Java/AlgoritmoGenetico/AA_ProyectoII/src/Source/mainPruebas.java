package Source;

import Genetico.Datos;
import java.util.ArrayList;
import java.util.Arrays;

public class mainPruebas {

    public static void main(String[] args) {
        
        //1st arg: seria la silueta cuyo path obtenemos de la interfaz
        //2nd arg: seria la direccion donde se van ir salvando los fractales
        //double grade = Make_Evaluate.selection(".\\src\\Source\\images\\silueta.bmp", ".\\src\\Source\\images\\fractal.bmp",400, 650, -90, 4, 4, 25, 2, 0, false, 45, 0, -45);
        //System.out.println("The grade: "+grade);
       
        Datos d = new Datos();
        d.setPuntuacion(11);
       
        Datos d2 = new Datos();
        d2.setPuntuacion(33);
        
        Datos d3 = new Datos();
        d3.setPuntuacion(25);
        
        Datos[] p = new Datos[4];
        
        p[0] = d;
        p[1] = d2;
        p[2] = d3;
        p[3] = d3;
        
        for (int i = 0; i < p.length; i++) {
            Datos datos = p[i];
            System.out.println(datos.getPuntuacion());
        }
        
        Arrays.sort(p);
        ArrayList<Datos> dat = new ArrayList();
        int temp = p.length/2;
        while(temp >0){
            int id = p.length - temp + 1;
            System.out.println(temp + " " + id);
            temp -=1;
        }
        
        for (int i = 0; i < p.length; i++) {
            Datos datos = p[i];
            System.out.println(p.length);
        }
    }
    
}
