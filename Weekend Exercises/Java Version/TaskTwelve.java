import java.util.Scanner;
public class TaskTwelve{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a number: ");
		int number = input.nextInt();

		System.out.println("Enter power: ");
		int power = input.nextInt();

		int result = 1;

		for (int count = 1; count <= power; count++){
			
			result *= number;

		}

		System.out.printf("%d to power of %d is %d%n", number, power, result);
	}
}