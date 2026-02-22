import java.util.Scanner;
public class TaskNine{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a number: ");
		int number = input.nextInt();

		int halfOfNumber = 0;

		if (number % 2 == 0){
			halfOfNumber = number/2;
		}

		else{
			halfOfNumber = (number/2) + 1;
		}

		int counter = 0;

		for (int count = 1; count <= halfOfNumber; count++){
			if (number % count == 0){
				counter++;
			}
		}
		System.out.printf("The number of divisors of %d is %d%n", number, counter);

	}
}