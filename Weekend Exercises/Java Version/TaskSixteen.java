public class TaskSixteen{

	public static void main (String [] args){

		for (int number = 1; number <= 100; number++){

			int halfOfNumber = 0;

			if (number % 2 == 0){
				halfOfNumber = number/2;
			}

			else{
				halfOfNumber = (number/2) + 1;
			}

			int counter = 0;

			for (int count = 1; count <= halfOfNumber; count++){
				if (number % count == 0){
					counter++;
				}
			}

			if (counter == 1 && number != 1){
				System.out.printf("%d ", number);
			}

		}

		System.out.println();

	}
}