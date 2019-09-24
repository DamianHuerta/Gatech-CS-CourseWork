/**
*@author Damian Huerta
*@version 9.6.19
*/
public class Counter {
	private static final int Max = 100; // class data statuc- applies to all instances of the class
	private int count; // instance data
    public static int numCounters = 0;

	/**
	*constructor for counter
	*/
	public Counter () {
	   count = 0; //count would already be 0 but this is good coding
	   numCounters++;
    }


    /**
    * @param count
    */
    public Counter (int count) {
        this.count = count; //count would already be 0 but this is good coding
    }

	/**
	* click which increments counter
	*/
	public void click () {
		count++;
		if (count >= Max) {
			count = 0;
		}
	}


	public void reset () {
		count = 0;
	}
	/**
	* get the counter
	* @param name user input of string name
	* @return the count of the counter
	*/
	public int getCount (String name) {
		return count;
	}
}