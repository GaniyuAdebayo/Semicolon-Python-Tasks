import java.util.Scanner;
public class TaskSeventeen{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a number: ");
		int numbers = input.nextInt();

		int number =  numbers;
		
		int counter = 0;

		while (number != 0){
			number /= 10;
			counter++;
		}
		
		System.out.printf("The number of digits in %d is %d%n", numbers, counter);
		
	}
}