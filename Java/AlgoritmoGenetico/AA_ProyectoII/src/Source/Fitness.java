package Source;

import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;


public class Fitness {
    
    public byte[][] silueta = null;
    public int cleanPoints = 0;
    public int paintPoints = 0;
    
    public BufferedImage redimensionar(BufferedImage bfrImg) throws IOException{

        // creando una imagen vacia del tamannio deseado
        BufferedImage outputImage = new BufferedImage(800, 700, bfrImg.getType());
 
        // reescala y la guarda en el bufferedImage outputImage
        Graphics2D g2d = outputImage.createGraphics();
        g2d.drawImage(bfrImg, 0, 0, 800, 700, null);
        g2d.dispose();
        
        return outputImage;
    }
    
    public byte[][] getSilueta(String pSilueta, int pWidth, int pHeight) throws IOException{
                      
        //Procede a hacer la lectura de la imagen silueta
        File image = new File(pSilueta);           //Lee la imagen
        BufferedImage imgBuffer = ImageIO.read(image);
        
        //Esto es en el caso de que se deba redimensionar el modelo (que ya fue leido)
        if ((imgBuffer.getWidth()!=pWidth)||(imgBuffer.getHeight()!=pHeight)){
            System.out.println("Se procede a redimensionar!");
            imgBuffer = redimensionar(imgBuffer);
        }
                                                                                //lista de los bits
        byte[] pixels = (byte[]) imgBuffer.getRaster().getDataElements(0, 0, imgBuffer.getWidth(), imgBuffer.getHeight(), null);
        
        int theWidth = imgBuffer.getWidth();
        int theHeight = imgBuffer.getHeight();
        
        byte[][] matrix = new byte[theHeight][theWidth];
        
        int generalCount = 0;
        for (int i=0; i < theHeight; i++) {   //itera filas
            for (int j = 0; j < theWidth; j++) { //itera cols
                matrix[i][j] = pixels[generalCount];
                generalCount++;
                if (matrix[i][j]==0){
                    cleanPoints++;              //Saca el total de puntos vacios
                }else{
                    paintPoints++;              //Saca el total de puntos pintados
                }
            }
        }
        
        /*
        //Imprime la matriz, en caso de ser necesario
        for (int i=0; i < theHeight; i++) {
            for (int j = 0; j < theWidth; j++) {
                System.out.print(matrix[i][j]);
            }
            System.out.println("");
        }
        */
        
        return matrix;
        
    }
    
    public int[] FitnessFunction(String pSilueta, String candidate, int pWidth, int pHeight) throws IOException {
                
        if (silueta==null){                                     //En caso que no se haya leido silueta
            silueta = getSilueta(pSilueta, pWidth, pHeight);
        }
        
        //--------------------------------------------
        
        //Se lee el fractal
        File image2 = new File(candidate);
        BufferedImage imgBuffer2 = ImageIO.read(image2);
               
        byte[] pixels2 = (byte[]) imgBuffer2.getRaster().getDataElements(0, 0, imgBuffer2.getWidth(), imgBuffer2.getHeight(), null);
                
        int theWidth2 = imgBuffer2.getWidth();
        int theHeight2 = imgBuffer2.getHeight();
        
        byte[][] matrix2 = new byte[theHeight2][theWidth2];
        
        int generalCount2 = 0;
        for (int i=0; i < theHeight2; i++) {   //itera filas
            for (int j = 0; j < theWidth2; j++) {
                matrix2[i][j] = pixels2[generalCount2];
                generalCount2++;
            }
        }
        
        /*
        //Imprime la matriz, en caso de ser necesario
        for (int i=0; i < theHeight2; i++) {
            for (int j = 0; j < theWidth2; j++) {
                System.out.print(matrix2[i][j]);
            }
            System.out.println("");
        }
        */
        
        // ******************************************************
        
        //Comparacion de ambas imagenes
        int emptys = 0;
        int paints = 0;
        int differs = 0;
                                
        //Para este punto ambos deben tener el mismo tamannio
        for (int i=0; i < theHeight2; i++) {   //itera filas
            for (int j = 0; j < theWidth2; j++) { //itera cols
                if (silueta[i][j]!=matrix2[i][j]){
                    differs++;
                }else{
                    if((silueta[i][j]==matrix2[i][j])&&(silueta[i][j]==0)){
                        emptys++;
                    }else{
                        if((silueta[i][j]==matrix2[i][j])&&(silueta[i][j]==1)){
                            paints++;
                        }
                    }  
                }
            }
        }
                
        int[] resultFitness = {paints, emptys, differs, cleanPoints, paintPoints};
        return resultFitness;
    }
    
    public Fitness() {
    }  
    
}
