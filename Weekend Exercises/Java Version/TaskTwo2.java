import java.util.Scanner;
public class TaskTwo2{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a digit: ");
		int number = input.nextInt();

		int reversedNumber = 0;

		while (number != 0){

			reversedNumber = (number%10) + (reversedNumber * 10);

			number /= 10;
		}

		System.out.printf("The reverse is %d%n", reversedNumber);
	}

}