import java.util.Scanner;
public class TaskSixteen{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a word: ");
		String word = input.nextLine().toLowerCase();
		int counter = 0;
		for (int count = 0; count < word.length(); count++){
			char letter = word.charAt(count);

			if (letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u'){
				counter++;
			}
		}
		System.out.printf("The number of vowels in %s is %d%n", word, counter);
	}
}