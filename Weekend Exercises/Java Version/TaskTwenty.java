public class TaskTwenty{

	public static void main (String [] args){

		int firstNumber = 0;
		int secondNumber = 1;

		System.out.printf("%d %d ", firstNumber, secondNumber);

		for (int counter = 1; counter <= 18; counter++){
			int number = firstNumber + secondNumber;
			firstNumber = secondNumber;
			secondNumber = number;
			
			System.out.printf("%d ", number);

		}
		System.out.println();
	}
}