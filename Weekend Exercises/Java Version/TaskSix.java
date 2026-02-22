import java.util.Scanner;
public class TaskSix{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a word: ");
		String word = input.nextLine();

		System.out.printf("%8s%15s%n", "Letter", "ASCII Number");

		for (int index = 0; index < word.length(); index++){
			System.out.printf("%5s%13d%n", word.charAt(index), (int) word.charAt(index));
		}

		//System.out.printf("The number of lower case in %s is %d%n", word, count);
	}
}