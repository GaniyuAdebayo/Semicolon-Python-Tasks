import java.util.Scanner;
public class TaskNineteen{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a number: ");
		int numbers = input.nextInt();

		int number =  numbers;
		
		int largest = number%10;

		while (number != 0){
			if(number % 10 > largest){
				largest = number % 10;
			}
	
			number = number / 10;
		}
		
		System.out.printf("The largest digit of %d is %d%n", numbers, largest);
		
	}
}