/*
Help command java
*/

class Help {
	public static void main(String args[])
	throws java.io.IOException {
		char a;
		System.out.println("Help: ");
		System.out.println("1.if");
		System.out.println("2.switch");
		System.out.print(" your choose: ");
		a = (char) System.in.read();
		switch (a) {
			case '1': 
				System.out.println("if (condition) { ");
				System.out.println("operators");
				System.out.println("}");
				System.out.println("else {");
				System.out.println("operators");
				System.out.println("}");
				break;		
			case '2':
				System.out.println("switch (expression) {");
				System.out.println("\tcase const1:");
				System.out.println("\t\toperators");
				System.out.println("break;");
				System.out.println("...");
				System.out.println("default:");
				System.out.println("\toperators");
				System.out.println("}");
				break;
		}
	}
}