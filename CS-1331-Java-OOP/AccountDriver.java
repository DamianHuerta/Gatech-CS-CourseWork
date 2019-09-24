//********************************************************************
//  AccountDriver.java
//
//  Demonstrates the creation and use of multiple Account objects.
//********************************************************************

public class AccountDriver
{
   //-----------------------------------------------------------------
   //  Creates some bank accounts and requests various services.
   //-----------------------------------------------------------------
   public static void main (String[] args)
   {
      Account acct1 = new Account ("Ted Murphy", 72354, 100.0);
      Account acct2 = new Account ("Jane Smith", 69713, 100.00);
      Account acct3 = new Account ("Edward Demsey", 93757, 759.32);
      Account acct4 = new Account ("Edward Demsey", 93757, 759.32);

      System.out.println(acct3 == acct4); // the exact same object
                                          // comparing the memory locations
      System.out.println(acct3.equals(acct4));

      System.out.println(acct3.getName().equals(acct4.getName()));

      acct1.addInterest();
      acct2.addInterest(2);
      System.out.println(acct1.toString());
      System.out.println(acct2.toString());
      //System.out.println(acct1.getBalance());
      //System.out.println(acct1.getName());

      //acct2.deposit(100.0);
      //acct2.withdraw(10.0, 1.75);

      System.out.println (acct1);
      System.out.println (acct2);
      System.out.println (acct3);
      System.out.println (acct4);

      System.out.println(Account.getNumAccounts());  // static method being called




   }
}