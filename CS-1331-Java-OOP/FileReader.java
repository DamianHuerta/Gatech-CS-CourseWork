import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
// I worked on this assignment alone.
/**
*@author Damian Huerta-Ortega
*@version 1.0
This class reads a file of commands and executes them.
*/
public class FileReader {
    /**

    *This is the main method that will read a file and execute commands
    *by printing the results.
    *@param args file name
    */
    public static void main(String[] args) throws FileNotFoundException {
        File commandsFile = new File(args[0]);
        Scanner scanboi = new Scanner(commandsFile);
        while (scanboi.hasNext()) {
            String command = scanboi.nextLine();
            String[] words = command.split(" ");
            if (command.contains("allcaps")) {
                System.out.println(allCaps(words[1]));
            } else if (command.contains("power")) {
                int b = Integer.parseInt(words[1]);
                int p = Integer.parseInt(words[2]);
                System.out.println(power(b, p));
            } else if (command.contains("substring")) {
                int start = Integer.parseInt(words[2]);
                int end = Integer.parseInt(words[3]);
                System.out.println(makeSubstring(words[1], start, end));
            } else {
                System.out.println("Invalid command");
            }
        }
    }
    /**
    *This method will return the parameter string in all caps.
    *@param str input string to be capitalized
    *@return aString
    */
    public static String allCaps(String str) {
        return str.toUpperCase();
    }
    /**
    *@author Damian Huerta-Ortega
    *This method will return the first parameter to the power of the other parameter.
    *@param base the base
    *@param power the power
    *@return a double that is the base raised to the power
    */
    public static double power(int base, int power) {
        return Math.pow(base, power);
    }

    /**
    *This method will return a string from startIndex to endIndex of str
    *@param str str and start/end index
    *@param startIndex the start index
    *@param endIndex the end index
    *@return a substring
    */
    public static String makeSubstring(String str, int startIndex, int endIndex) {
        if ((str.length() < startIndex)
            || (endIndex  > (str.length()))
            || (startIndex < 0)
            || (endIndex < 0)) {
            return "Invalid command";
        } else {
            return str.substring(startIndex, endIndex);
        }

    }
}