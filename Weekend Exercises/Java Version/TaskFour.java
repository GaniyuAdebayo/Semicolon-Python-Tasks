import java.util.Scanner;
public class TaskFour{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a word: ");
		String word = input.nextLine();

		int count = 0;

		for (int index = 0; index < word.length(); index++){
			if (word.charAt(index) >= 'a' && word.charAt(index) <= 'z'){
				count++;
			}
		}

		System.out.printf("The number of lower case in %s is %d%n", word, count);
	}
}