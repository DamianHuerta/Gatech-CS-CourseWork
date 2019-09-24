/**
* A representation of a Dog
*
* @author
* @version 1.0
**/
public class Dog {

    /* Part 1: Fields

        -  Add instance variables for name and age, where age should be a
            whole number with appropriate visibility modifiers
        -  Add a variable called dogCount to keep track of how many
            Dogs have been instantiated that will be shared by all instances
            of the class
    */
    private int age;
    private String name;
    private static int dogCount = 0;

    /* Part 2: Constructor

        - Write a constructor to create a dog, given parameters: name, age
            (parameters must be in that order)
            Be sure to set the instance variables appropriately,
            and increment the dog count by 1
    */


    /**
    * Creates a Dog object
    *
    * @param name a string representing the name of the dog
    * @param age an int representing the age of the dog
    **/
    public Dog(String name, int age) {
        this.age = age;
        this.name = name;
        dogCount++;
    }

    /* Part 3: Visibility

        - Modify this method so that code in other classes cannot access it
    */

    /**
    * Forms and returns this Dog's secret
    *
    * @return a string holding the dog's secret
    **/
    private String dogSecret() {
        return "Dear diary, I love CS1331 - " + this.name;
    }

    /* Do not modify the main method. You can use the output to test if your
        code is working
    */
    /**
    * @param args the main method arguments
    **/
    public static void main(String[] args) {
        Dog pedro = new Dog("Pedro", 7);
        System.out.println(pedro.name + " is " + pedro.age + " years old");
        System.out.println(pedro.dogSecret());
        System.out.printf("There are %d dogs", dogCount);
    }

}
