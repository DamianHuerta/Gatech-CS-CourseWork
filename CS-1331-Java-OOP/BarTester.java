public class BarTester {
	public static void main (String[] args) {
		Bar b1,b2,b3;
		b1 = new Bar("toffee", 5, 7);
		b1.drawBar();
		System.out.println(b1.getDetails());
		b2 = new Bar("dick", 10, 10);
		System.out.println(b2.getPerimeter());
		b2.drawBar();
		System.out.println(b2.getArea());
		System.out.println(b2.isSquare());
		System.out.println(b2.calculateCost(2.0,2.0));
		System.out.println(b2.getDetails());
        b3 = new Bar("pizza",1,4);
        System.out.print(b3.getDetails());

	}
}