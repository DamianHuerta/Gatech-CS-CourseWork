// In order to help learn course concepts, I worked on this homework
// with Celina Huang and Dennis Crawford, discussed homework topics and
// issues with Celina Huang Dennis Crawford

/**
* @author Damian Huerta-Ortega
* @version 1.0
* a class that is for a chocolate bar
*/
public class Bar {
    private String chocolateType;
    private int barLength;
    private int barWidth;

    /**
    * This is the costructor method
    * @param chocolateType the type of chocolate
    * @param barLength the bar length
    * @param barWidth the bar width
    */
    public Bar(String chocolateType, int barLength, int barWidth) {
        this.chocolateType = chocolateType;
        this.barLength = barLength;
        this.barWidth = barWidth;
    }

    /**
    * This method returns the perimeter of the chocolate bar
    * @return the perimeter of the bar
    */
    public int getPerimeter() {
        return 2 * (barLength + barWidth);
    }

    /**
    * This method will return the area of the chocolate bar
    * @return the area of the bar
    */
    public int getArea() {
        return barLength * barWidth;
    }

    /**
    * This method will return a boolean based on if the bar is a square
    * @return a boolean based on if the bar is square
    */
    public boolean isSquare() {
        return barLength == barWidth;
    }
    /**
    * This method calculates the cost of the chocolate bar
    * @param chocolateCost how much chocolate costs
    * @param trimCost the cost of the trim
    * @return the cost of the chocolate
    */
    public double calculateCost(double chocolateCost, double trimCost) {
        return getArea() * chocolateCost + getPerimeter() * trimCost;
    }

    /**
    * This method will return information about the chocolate
    * @return a string of information about the chocolate
    */
    public String getDetails() {
        if (isSquare()) {
            return "Square " + getArea() + " piece bar of " + chocolateType + " chocolate";
        } else {
            return barLength + " by " + barWidth + " bar of " + chocolateType + " chocolate";
        }
    }

    /**
    * this method will draw the bar
    */
    public void drawBar() {
        String let = chocolateType.substring(0, 1).toUpperCase();
        String hi;
        for (int i = 0; i < barLength; i++) {
            hi = "";
            for (int b = 0; b < barWidth; b++) {
                hi += let;
            }
            System.out.println(hi);
        }

    }
}