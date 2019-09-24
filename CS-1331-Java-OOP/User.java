//I worked on this homework alone
/**
* A class that tracks user data.
* @author Damian Huerta-Ortega
* @version 1.0.0
*/
public class User {
    private String username;
    private int password;
    private static int numUsers = 0;
    private static User newestUser;
    private static boolean displayNewest = true;

    /**
    * This is the constructor
    * @param name is the username
    * @param pass is the password
    */
    public User(String name, int pass) {
        username = name;
        password = pass;
        numUsers++;
        newestUser = this;
    }

    /**
    * Method to set display newest
    * @param dispnew what the variable will be set to
    */
    public static void setDisplayNewest(boolean dispnew) {
        displayNewest = dispnew;
    }

    /**
    * Method that returns the number of users
    * @return number of current users
    */
    public static int getNumUsers() {
        return numUsers;
    }

    /**
    * Method that displays the username
    * @return the username as a string
    */
    public String getUsername() {
        return username;
    }

    /**
    * This method returns a welcome message
    * @return a welcome message
    */
    public static String getWelcomeMessage() {

        if (numUsers > 0 && !displayNewest) {
            return "Welcome to our site! We have " + Integer.toString(numUsers)
                    + " user(s) and counting!";
        } else if (numUsers > 0 && displayNewest) {
            return newestUser.getUsername() + " just joined our site!"
                    + " Please give them a warm welcome!";
        } else  {
            return "This site doesn't have any users yet!";
        }
    }

    /**
    * password changer method
    * @param usernameInput the username of current user
    * @param passwordInput the password of current user
    * @param newPassword the new password
    */
    public void changePassword(String usernameInput, int passwordInput, int newPassword) {
        if (usernameInput == username && passwordInput == password) {
            password = newPassword;
        }
    }

    /**
    * Method that returns if the login is valid
    * @param usernameInput the password
    * @param passwordInput the username
    * @return the answer to if it is a successful login
    */
    public boolean validLogin(String usernameInput, int passwordInput) {
        return usernameInput == username && passwordInput == password;
    }
}