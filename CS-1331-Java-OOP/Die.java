//********************************************************************
//  Die.java       Author: Lewis/Loftus
//
//  Represents one die (singular of dice) with faces showing values
//  between 1 and 6.
//********************************************************************

public class Die {
    private static final int MAX = 6;  // maximum face value

    private int faceValue;  // current value showing on the die
    						// this is the data for the die class
    						//also kown as an attribute of an instance of the die class
    						//

    //-----------------------------------------------------------------
    //  Constructor: Sets the initial face value.
    //-----------------------------------------------------------------
    public Die() {		//notice that the name is the same as the class
        faceValue = 1;
    }

    //-----------------------------------------------------------------
    //  Rolls the die and returns the result.
    //-----------------------------------------------------------------
    public int roll() {
        faceValue = (int) (Math.random() * MAX) + 1;
        return faceValue;
    }

    //-----------------------------------------------------------------
    //  Face value mutator.
    //-----------------------------------------------------------------
    public void setFaceValue(int value) {
        faceValue = value;
    }

    //-----------------------------------------------------------------
    //  Face value accessor.
    //-----------------------------------------------------------------
    public int getFaceValue() {
        return faceValue;
    }

    //-----------------------------------------------------------------
    //  Returns a string representation of this die.
    //-----------------------------------------------------------------
    public String toString() {
        return Integer.toString(faceValue);
    }
    //-----------------------------------------------------------------
    //	returns true if dice face valyue is even
    //-----------------------------------------------------------------
    public Boolean isEven() {
    	return faceValue % 2 == 0;
    }
}
