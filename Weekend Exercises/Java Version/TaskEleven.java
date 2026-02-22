import java.util.Scanner;
public class TaskEleven{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a word: ");
		String word = input.nextLine();

		String newWord = "";

		for (int index = 0; index < word.length(); index++){

			newWord = word.charAt(index) + newWord;

		}

		if (word == newWord){
			System.out.printf("%s is palindrome%n", word);
		}
		else{
			System.out.printf("%s is not palindrome%n", word);
		}
	}
}