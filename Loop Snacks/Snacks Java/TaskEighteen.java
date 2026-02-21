import java.util.Scanner;
public class TaskEighteen{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a number: ");
		int numbers = input.nextInt();

		int number =  numbers;
		
		int sum = 0;

		while (number != 0){
			sum += number%10;
			number /= 10;
		}
		
		System.out.printf("The sum of digits in %d is %d%n", numbers, sum);
		
	}
}