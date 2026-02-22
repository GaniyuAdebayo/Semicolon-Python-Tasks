import java.util.Scanner;
public class TaskNineteen{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a number: ");
		int number = input.nextInt();

		int decimalNumber = number;
		String binaryNumber = "";

		int power = 0;
		while (decimalNumber != 0){
			binaryNumber = String.valueOf(decimalNumber % 2) + binaryNumber;

			decimalNumber /= 2;
		}

		System.out.printf("%d base 10 is %s in base 2%n", number, binaryNumber);
	}

}