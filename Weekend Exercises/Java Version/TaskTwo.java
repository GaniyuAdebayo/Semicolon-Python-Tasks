import java.util.Scanner;
public class TaskTwo{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a number: ");
		int number = input.nextInt();

		String numberToString = String.valueOf(number);

		String reverseString = "";

		for (int index = 0; index < numberToString.length(); index++){
			reverseString = numberToString.charAt(index) + reverseString;
		}

		int reverseInteger = Integer.valueOf(reverseString);

		System.out.printf("Reverse of the number is %d%n", reverseInteger);
	}
}