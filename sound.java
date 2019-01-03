/*
program for calculating distance to a lightning strike
*/
class sound {
	public static void main(String args[]) {
		double distance_foot, distance_metr, time;
		int speed;
		speed = 1100; // ft/s
		time = 3.7; //s
		distance_foot = speed * time; //ft
		distance_metr = distance_foot / 3.281; // metr
		System.out.println("Distance to a lightning strike " + distance_metr + " metrs");
	}
}