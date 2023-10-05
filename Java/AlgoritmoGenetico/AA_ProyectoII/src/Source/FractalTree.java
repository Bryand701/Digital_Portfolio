
package Source;


import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Line2D;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;
import javax.swing.JFrame;
 
public class FractalTree extends JFrame {
     
    int x1;             //posicion de inicio del dibujo
    int y1;             //posicion de inicio del dibujo
    double angle;       //angulo general del arbol
    int depth;          //profundiad del arbol
    int originalDepth;  //profundiad total del arbol (copia del valor inicial)
    double base_len;    //proporcion del tamannio (largo) que tendran las ramas
    int largeTrunk;     //largo que tendra el tronco (multiplica el default)
    int width;          //duplica el ancho de las ramas
    boolean triple;     //Habilita una tercera rama
    double lGrade;         //grado de la rama izq(L)
    double rGrade;         //grado de la rama der(R)
    double eGrade;         //grado de tercera rama
    
    public FractalTree(int x1, int y1, double angle,
                       int depth, int originalDepth, double base_len,
                       int largeTrunk, int width, boolean triple,
                       double lGrade, double rGrade, double eGrade) {
        
        super("Fractal Tree");                              //aspectos de la ventana
        setBounds(0, 0, 800, 700);
        setResizable(false);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        
                                                           //asignando los valores a los atributos
        this.x1 = x1;
        this.y1 = y1;
        this.angle = angle;
        this.depth = depth;
        this.originalDepth = originalDepth;
        this.base_len = base_len;
        this.largeTrunk = largeTrunk;
        this.width = width;
        this.triple = triple;
        this.lGrade = lGrade;
        this.rGrade = rGrade;
        this.eGrade = eGrade;
                
        try                                                //escribe la imagen en un bmp 2 colores de 800x700
        {
            BufferedImage image = new BufferedImage(getWidth(), getHeight(), BufferedImage.TYPE_BYTE_BINARY);
            Graphics2D graphics2D = image.createGraphics();
            this.paint(graphics2D);
            ImageIO.write(image,"bmp", new File(".\\src\\Source\\images\\fractal.bmp"));            //path donde escribira la imagen
        }
        catch(Exception exception)
        {
            System.out.println("A unexpectable error ocurred!");
        }
        
    }
 
    /*
    g: Graphics, para pintar
    x1: posicion de inicio del dibujo
    y1: posicion de inicio del dibujo
    angle: angulo general del arbol
    depth: profundiad del arbol
    originalDepth: profundiad total del arbol (copia del 1er valor)
    base_len: proporcion del tamannio (largo) que tendran las ramas
    largeTrunk: largo que tendra el tronco (multiplica el default)
    width: duplica el ancho de las ramas
    triple: Habilita una tercera rama
    lGrade: grado de la rama izq(L)
    rGrade: grado de la rama der(R)
    eGrade: grado de tercera rama
    */
    
    private int getVar(){
        int var = (int) Math.floor(Math.random()*10);
        if (var%2!=0){
            var *= -1;
        }
        var = (int) Math.floor((double) var/2.0);
        System.out.println(var);
        return var;
    }
    
    private void drawTree(Graphics g, int x1, int y1, double angle,
                          int depth, int originalDepth, double base_len,
                          int largeTrunk, int width, boolean triple,
                          double lGrade, double rGrade, double eGrade) {
        
        int x2=0, y2=0;
        if (depth == 0) return;
        if (depth==originalDepth){                      //es el tronco
            x2 = x1 + (int) (Math.cos(Math.toRadians(angle)) * ((depth * base_len)*largeTrunk));
            y2 = y1 + (int) (Math.sin(Math.toRadians(angle)) * ((depth * base_len)*largeTrunk));
        }else{
            x2 = x1 + (int) (Math.cos(Math.toRadians(angle)) * depth * base_len);
            y2 = y1 + (int) (Math.sin(Math.toRadians(angle)) * depth * base_len);
        }
               
        
        Graphics2D g2 = (Graphics2D) g;
        int strk = depth*1;                             //en cuyo hace mas ancho el arbol
        if (width==1){
            strk = depth*2;
        }
        
        g2.setStroke(new BasicStroke(strk));            //setea el ancho de esta linea
        g2.draw(new Line2D.Float(x1, y1, x2, y2));      
        
        drawTree(g, x2, y2, angle + lGrade, depth - 1, originalDepth, base_len, largeTrunk, width, triple ,lGrade+getVar(), rGrade+getVar(), eGrade+getVar()); //angle - 8
        drawTree(g, x2, y2, angle + rGrade, depth - 1, originalDepth, base_len, largeTrunk, width, triple, lGrade+getVar(), rGrade+getVar(), eGrade+getVar()); //angle + 30 Hacen una clase de hoja
        if (triple){
            drawTree(g, x2, y2, angle + eGrade, depth - 1, originalDepth, base_len, largeTrunk, width, triple, lGrade+getVar(), rGrade+getVar(), eGrade+getVar());
        }        
    }   
 
    //Ver parametros arriba, utiliza los atributos
    @Override
    public void paint(Graphics g) {
        g.setColor(Color.ORANGE);
        drawTree(g, this.x1, this.y1, this.angle, this.depth, this.originalDepth, this.base_len,
                this.largeTrunk, this.width, this.triple, this.lGrade, 
                this.rGrade, this.eGrade);
        
    }
    
}
