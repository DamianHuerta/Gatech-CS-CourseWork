// I worked on this assignment alone
/**
* @author Dammian Huerta-Ortega
* @version 1.0
*/
public class WaterFountain {
    private String modelName;
    private boolean requiresMaintenance;
    private int cupsPoured;
    private static  int totalWaterFountains = 0;
    public static final String SOFTWARE_VERSION = "2.0.0";

    /**
    *This is the constructor
    * @param name name of the fountain
    * @param cup number of cups poured
    */
    public WaterFountain(String name, int cup) {
        modelName = name;
        cupsPoured = cup;
        requiresMaintenance = false;
        totalWaterFountains++;
    }

    /**
    * returns the model name
    * @return string of the model name
    */
    public String getModelName() {
        return modelName;
    }

    /**
    * @return boolean saying if this fountain needs maintenance
    */
    public boolean getRequiresMaintenance() {
        return requiresMaintenance;
    }

    /**
    * retunrs the number of cups this waterfountain has poured
    * @return number of cups this waterfountain has poured
    */
    public int getCupsPoured() {
        return cupsPoured;
    }

    /**
    * returns the number of total water fountains
    * @return interger of how many water fountains there is
    */
    public static int getTotalWaterFountains() {
        return totalWaterFountains;
    }

    /**
    * will change the modelname of the water fountain
    * @param newname the new model name
    */
    public void setModelName(String newname) {
        modelName = newname;
    }

    /**
    * sets if the fountain needs maintenance
    * @param broke if the foutain requires maintenance
    */
    public void setRequiresMaintenance(boolean broke) {
        requiresMaintenance = broke;
    }

    /**
    * will set the cups poured
    * @param thirst number of cups poured
    */
    public void setCupsPoured(int thirst) {
        cupsPoured = thirst;
    }

    /**
    * pours one cup and increments cups poured by 1
    */
    public void pourCup() {
        if (!requiresMaintenance) {
            cupsPoured++;
        }
    }

    /**
    * compares two water fountains
    * @param other the other water fountain it is being compared to
    * @return boolean if fountains are the same
    */
    //@Override
    public boolean equals(WaterFountain  other) {
        return (modelName == other.getModelName())
                && (cupsPoured == other.getCupsPoured())
                && (SOFTWARE_VERSION == SOFTWARE_VERSION);
    }
    /**
    * This is the hashcode
    * @return 0
    */
    public int hashCode() {
        return 0;
    }
    /**
    * @return a string describing the water fountain
    */
    public String toString() {
        if (requiresMaintenance) {
            return modelName + " has poured " + Integer.toString(cupsPoured)
                    + " cups, requires maintenance, and is running version: "
                    + SOFTWARE_VERSION;
        } else {
            return modelName + " has poured " + Integer.toString(cupsPoured)
                    + " cups, does not required maintenance, and is running version: "
                    + SOFTWARE_VERSION;
        }
    }
}