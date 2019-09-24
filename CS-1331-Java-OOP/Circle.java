//********************************************************************
//  Circle.java
//
//  Represents a circle.
//
//********************************************************************
import java.util.Random;

public class Circle
{
   private Random r = new Random();
   private int radius;
   //-----------------------------------------------------------------
   //  Sets up a circle with a random radius that is an integer between
   //  1 and 10
   //-----------------------------------------------------------------
   public Circle ()
   {
      //initialize a circle with random radium from 1 to 10
    this(1,10);

   }
   //-----------------------------------------------------------------
   //  Sets up a circle with a random radius that is an integer between
   //  start and stop inclusive
   //-----------------------------------------------------------------
   public Circle (int start, int stop)
   {
    radius = r.nextInt(stop - start + 1) + start;

   }
   //-----------------------------------------------------------------
   //  Return the area of the circle
   //-----------------------------------------------------------------
   public double getArea()
   {
    return Math.PI * Math.pow(radius,2);
   }
   //-----------------------------------------------------------------
   // Indicates the string to print when a Circle is printed out.
   //-----------------------------------------------------------------
   public String toString ()
   {
      // return a formatted string that has the radius and area rounded to 2 decimal place
      // reserve 6 spaces.
        return String.format("circle has the radius %d, with area of " + "%6.2f", radius, getArea());
   }
   public static void main(String[] args) {
    Circle c = new Circle();
    Circle c1 = new Circle(50,1000);
    System.out.println(c1);
    System.out.println(c);
   }
}