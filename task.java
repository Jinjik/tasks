/*
Prorgamm convert litrs in gallons from 1 to 100
*/
class task {
	public static void main(String args[]) {
		double litrs, gallons;
		int counter;


		counter = 0;
		for (litrs = 1; litrs <= 100; litrs++) {
			gallons = litrs * 3.7854;
			counter = counter + 1;
			System.out.println(litrs + " litrs = " + gallons + " gallons");
			if (counter % 10 == 0) {
				System.out.println();
			}
		}
	}
}