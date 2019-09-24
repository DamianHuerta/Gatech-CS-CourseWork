public class UserTest {
    public static void main (String[] args) {
        System.out.println(User.getWelcomeMessage());
        User user1 = new User("Bob", 122345);
        System.out.println(User.getWelcomeMessage());
        System.out.println(user1.getUsername());
        System.out.println(user1.validLogin("Bob",1273));
        User user2 = new User("Karen", 456);
        User.setDisplayNewest(false);
        System.out.println(User.getWelcomeMessage());

    }
}