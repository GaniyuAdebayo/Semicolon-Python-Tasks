import java.util.Scanner;
public class TaskEleven{
	public static void main (String [] args){
		Scanner input = new Scanner(System.in);
		
		System.out.println("Enter a number: ");
		int number = input.nextInt();
		
		for (int count = 1; count <= 12; count++){
			System.out.printf("%d X %d = %d%n", number, count, number*count);
		}
	}

}