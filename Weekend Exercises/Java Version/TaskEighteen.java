import java.util.Scanner;
public class TaskEighteen{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a binary number (0s and 1s only): ");
		String number = input.nextLine();

		int binaryNumber = Integer.valueOf(number);

		int decimalNumber = 0;

		int power = 0;
		while (binaryNumber != 0){
			decimalNumber += ((binaryNumber % 10) * Math.pow(2, power));
			binaryNumber /= 10;
			power++;
		}

		System.out.printf("%s base 2 is %d in base 10%n", number, decimalNumber);
	}

}