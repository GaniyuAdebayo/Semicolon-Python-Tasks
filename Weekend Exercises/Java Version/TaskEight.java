import java.util.Scanner;
public class TaskEight{

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

		System.out.printf("The divisors of %d is/are ", number);

		for (int count = 1; count <= halfOfNumber; count++){
			if (number % count == 0){
				System.out.printf("%d ", count);
			}
		}
		System.out.println();

	}
}