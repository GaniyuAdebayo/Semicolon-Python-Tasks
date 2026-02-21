import java.util.Scanner;
public class TaskThirteen{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a word: ");
		String word = input.nextLine();

		int val = 0;
		for (int count = 0; count < word.length(); count++){
			if (word.charAt(count) == 'e')
				val++;
		}

		System.out.printf("The number of e in %s is %d%n", word, val);
	}
}