import java.util.Scanner;
public class TaskThree{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a word: ");
		String word = input.nextLine();

		int count = 0;

		for (int index = 0; index < word.length(); index++){
			if (word.charAt(index) >= 'A' && word.charAt(index) <= 'Z'){
				count++;
			}
		}

		System.out.printf("The number of uppercase in %s is %d%n", word, count);
	}
}