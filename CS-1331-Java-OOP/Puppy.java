//I worked on this assignment alone
import java.util.Random;
/**
* @author Damian Huerta-Ortega\
* @version 1.0
*/
public class Puppy {
    private String name;
    private int age;
    private int health;


    /**
    * Static random field
    * @param max the max value
    * @param min the min value
    * @return the random number
    */
    public static int randomNum(int min, int max) {
        Random r = new Random();
        return r.nextInt((max - min) + 1);
    }

    /**
    * Constructor with just the dog name
    *@param doggy the name of dog
    */
    public Puppy(String doggy) {
        this(doggy, randomNum(0, 15), randomNum(5, 35) + 5);
    }
    /**
    * @param doggy the name of the do
    * @param old the age of the dog
    * @param hearts the health of the dog
    */
    public Puppy(String doggy, int old, int hearts) {
        name = doggy;
        age = old;
        health = hearts;
    }

    /**
    * This is a setter for the name of the dog
    * @param rename new name for the dog
    */
    public void setName(String rename) {
        name = rename;
    }

    /**
    * This is a setter for the age of the dog
    * @param reage the new age of the dog
    */
    public void setAge(int reage) {
        age = reage;
    }

    /**
    * This is a setter for the health of the dog
    * @param rehealth the new health of the dog
    */
    public void setHealth(int rehealth) {
        health = rehealth;
    }

    /**
    * This is a getter for the name of the dogg
    * @return the name of the dog
    */
    public String getName() {
        return name;
    }

    /**
    * This is a getter for the health of the dog
    * @return the health of the dog
    */
    public int getHealth() {
        return health;
    }

    /**
    * This is a getter for the age of the dog
    * @return the age of the dog
    */
    public int getAge() {
        return age;
    }

    /**
    * This method makes a string describing the dog
    * @return a string describing the dog
    */
    public String toString() {
        return name + ": a puppy " + Integer.toString(age)
                + " years old with " + Integer.toString(health) + " health";
    }

    /**
    * Method that returns if the dog can be adopted
    * @return a boolean describing if the dog can be adopted
    */
    public boolean canAdopt() {
        return health >= 50;
    }

    /**
    * Method that plays fetch with the dog
    */
    public void fetch() {
        health++;
    }

    /**
    * This method plays fetcb with the dog
    * @param inside says if the dog is inside or not
    */
    public void fetch(boolean inside) {
        if (inside) {
            health += 5;
        } else {
            health += 10;
        }
    }

    /**
    * This method will play fetch with the dog
    * @param distance the distance the object is thrown
    */
    public void fetch(int distance) {
        health += (distance / 10);
    }
}