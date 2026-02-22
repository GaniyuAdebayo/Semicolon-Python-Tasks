import java.util.Scanner;
public class TaskTen{

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

		if (reverseInteger == number){
			System.out.printf("%d is a palindrome%n", number);
		}
		else{
			System.out.printf("%d is not palindrome%n", number);
		}

	}
}