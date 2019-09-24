public class PuppyTest {
    public static void main(String[] args) {
        Puppy pup = new Puppy("pup");
        System.out.println("age: " + pup.getAge());
        System.out.println("health: " + pup.getHealth());

        pup. fetch(false);
        System.out.println("Play fetch outside");
        System.out.println("health: " + pup.getHealth());
    }
}