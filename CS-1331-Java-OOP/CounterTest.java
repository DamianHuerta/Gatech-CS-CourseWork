public class CounterTest {
	public static void main (String[] args) {
		Counter c1 = new Counter();
		Counter c2 = new Counter();
		c1.click();
        System.out.print(Counter.numCounters);
	}
}