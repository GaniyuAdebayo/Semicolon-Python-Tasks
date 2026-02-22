import java.util.Scanner;
public class TaskFive{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a word: ");
		String words = input.nextLine();
		String word = words.toLowerCase();

		int index = 0;

		for (; index < word.length(); index++){

			char letter = word.charAt(index);
			if (letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u'){
				break;
			}
		}

		System.out.printf("The position of first vowel in %s is %d%n", word, index + 1);
	}
}