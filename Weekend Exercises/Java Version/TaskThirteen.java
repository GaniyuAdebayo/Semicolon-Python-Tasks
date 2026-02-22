import java.util.Scanner;
public class TaskThirteen{

	public static void main (String [] args){

		Scanner input = new Scanner(System.in);

		System.out.println("Enter a sentence: ");
		String sentence = input.nextLine().trim();

		int numberOfWords = 1;

		for (int index = 0; index < sentence.length(); index++){
			if(sentence.charAt(index) == ' '){
				numberOfWords++;
			}

			if(sentence.charAt(index) == ' ' && sentence.charAt(index+1) == ' '){
				numberOfWords--;
			}

		}

		System.out.printf("The number of words in %s is %d%n", sentence, numberOfWords);
	}

}