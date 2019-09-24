//********************************************************************
//  Account.java
//
//  Represents a bank account with basic services such as deposit
//  and withdraw.
//
//********************************************************************

public class Account
{
   final double RATE = 0.035;  // interest rate of 3.5%
   private static int numAccounts = 0;
   private long acctNumber;
   private double balance;
   private String name;

   //-----------------------------------------------------------------
   //  Sets up the account by defining its owner
   //-----------------------------------------------------------------
   public Account (String owner)
   {
      numAccounts++;
   //-----------------------------------------------------------------
   //  Sets up the account by defining its owner
   //-----------------------------------------------------------------
   public Account (String owner)
   {
      this();
      name = owner;;
   }
   //-----------------------------------------------------------------
   //  Sets up the account by defining its owner and account number
   //-----------------------------------------------------------------
   public Account (String owner, long brendenissexy)
   {
      this(owner);
      numAccounts++;
      acctNumber = brendenissexy;
   }
   //-----------------------------------------------------------------
   //  Sets up the account by defining its owner and account number
   //-----------------------------------------------------------------
   public Account (String owner, long brendenissexy, double initial)
   {
      this(owner,brendenissexy);
      numAccounts++;
      balance = initial;

   }
   //-----------------------------------------------------------------
   //  Deposits the specified amount into the account. Returns the
   //  new balance.
   //-----------------------------------------------------------------
   public void deposit (double amount)
   {
      balance = balance + amount;
   }

   //-----------------------------------------------------------------
   //  Withdraws the specified amount from the account and applies
   //  the fee. Returns the new balance.
   //-----------------------------------------------------------------
   public void withdraw (double amount, double fee)
   {
      balance = balance - amount - fee;
   }

   //-----------------------------------------------------------------
   //  Adds interest to the account
   //-----------------------------------------------------------------
   public void addInterest (int myrate)
   {
      balance += (balance * myrate);
   }

    //-----------------------------------------------------------------
   //  Adds interest to the account
   //-----------------------------------------------------------------
   public void addInterest ()
   {
      balance += (balance * RATE);
   }
   //-----------------------------------------------------------------
   //  Returns the current balance of the account.
   //-----------------------------------------------------------------
   public double getBalance ()
   {
      return balance;
   }
   //-----------------------------------------------------------------
   //  Returns the current number of accounts at this bank.
   //-----------------------------------------------------------------
   public static int getNumAccounts()
   {
      return numAccounts;
   }
   //-----------------------------------------------------------------
   //  Returns the current name of the account.
   //-----------------------------------------------------------------
   public String getName ()
   {
      return name;
   }
   //-----------------------------------------------------------------
   //  Returns a one-line description of the account as a string.
   //-----------------------------------------------------------------
   public String toString ()
   {
      return (acctNumber + "\t" + name + "\t" + balance);
   }
      //-----------------------------------------------------------------
   //  returns true if same accountNumber, false otherwise
   //-----------------------------------------------------------------
   public boolean equals (Account other)
   {
      return (this.acctNumber == other.acctNumber);
   }
}