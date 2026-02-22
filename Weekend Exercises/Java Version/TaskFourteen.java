import java.util.Scanner;
public class TaskFourteen{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a number: ");
		int number = input.nextInt();

		int sum = 0;

		while (number != 0){
			if ((number % 10) % 2 == 0){
				sum += (number % 10);
			}
			number /= 10;
		}

		System.out.printf("The sum of even digits is %d%n", sum);
	}

}