//********************************************************************
//  RollingDice.java       Author: Lewis/Loftus
//
//  Demonstrates the creation and use of a user-defined class.
//********************************************************************

public class RollingDice {
    //-----------------------------------------------------------------
    //  Creates two Die objects and rolls them several times.
    //-----------------------------------------------------------------
    public static void main(String[] args) {
        Die die1, die2; //declaring the variables
        int sum;

        die1 = new Die(); //allocating the memory, new calls the constructor
        die2 = new Die();
        System.out.println(die1.getFaceValue()); //only works because face value is public



        die1.roll();
        die2.roll();
        System.out.println("After Constructor Die One: " + die1 + ", Die Two: " + die2);

        die1.roll();
        die2.setFaceValue(4);
        System.out.println("Die One: " + die1 + ", Die Two: " + die2);

        sum = die1.getFaceValue() + die2.getFaceValue();
        System.out.println("Sum: " + sum);

        sum = die1.roll() + die2.roll();
        System.out.println("Die One: " + die1 + ", Die Two: " + die2);
        System.out.println("New sum: " + sum);

        Die die3;
        die3 = new Die();
        die3.roll();
        sum += die3.getFaceValue();
        System.out.println(sum);
        System.out.println(die3.getFaceValue());
        System.out.println(die3.isEven());
    }
}
