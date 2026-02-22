import java.util.Scanner;
public class TaskOne{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a word: ");
		String word = input.nextLine();

		String newWord = "";

		for (int index = 0; index < word.length(); index++){

			newWord = word.charAt(index) + newWord;

		}

		System.out.printf("Reverse of the word is %s", newWord);
	}
}