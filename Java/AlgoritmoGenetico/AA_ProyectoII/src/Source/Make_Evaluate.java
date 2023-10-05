
package Source;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;

public class Make_Evaluate {
    
    public static double selection(String modelPath, String fractalPath,
                                    int x1, int y1, double angle,
                                    int depth, int originalDepth, double base_len,
                                    int largeTrunk, int width, boolean triple,
                                    double lGrade, double rGrade, double eGrade){
        
        
        //Llama a Fractal Tree
        new FractalTree(x1, y1, angle, depth, originalDepth, base_len, largeTrunk, width, triple, lGrade, rGrade, eGrade).setVisible(true);
                
        //Llama a Fitness
        Fitness ins = new Fitness();
        int[] fitnessResult = {-1, -1, -1, -1, -1};
        
        /*
        File directory = new File("./");
        System.out.println(directory.getAbsolutePath());
        */
        
        try {
            fitnessResult = ins.FitnessFunction(modelPath, fractalPath, 800, 700);
        } catch (IOException ex) {
            System.out.println("Verifique la ruta y formato de los bmp!");
        }
        
        System.out.println(fitnessResult[0]+", "+fitnessResult[1]+", "+fitnessResult[2]);
        System.out.println(fitnessResult[3]+" "+fitnessResult[4]);
        
        //Calculando la nota:
        int paints = fitnessResult[0];
        int emptys = fitnessResult[1];
        int differs = fitnessResult[2];
        int cleanPoints = fitnessResult[3];
        int paintPoints = fitnessResult[4];
        
        double uPaints = (double) paints / (double) paintPoints;
        System.out.println(uPaints);
        double uClear = (double) emptys / (double) cleanPoints;
        System.out.println(uClear);
        double desv = (double) differs/560000.00;
        System.out.println(desv);
        
        double ecu = ((uPaints*100)+(uClear*100))/2.0;
        ecu -= (desv*100);
        
        System.out.println(ecu);
        
        return ecu;
        
    }
    
}
