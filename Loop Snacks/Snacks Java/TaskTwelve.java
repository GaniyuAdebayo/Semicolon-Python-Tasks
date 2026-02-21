import java.util.Scanner;
public class TaskTwelve{

	public static void main (String [] args){

		Scanner input = new Scanner (System.in);

		System.out.println("Enter a word: ");
		String word = input.nextLine();

		for (int count = 0; count < word.length(); count++){
			System.out.println(word.charAt(count));
		}
	}
}