/*
program to convert inches to meters
*/

class metr {
	public static void main(String args[]) {
		double inch, metr;
		int counter;

		counter = 0;
		for (inch = 1; inch <=144; inch++) {
			metr = inch / 39.97;
			counter++;
			System.out.println(inch + " inches = " + metr + " metrs");
			if (counter % 12 == 0) {
				System.out.println();
			}
		}
	}
}