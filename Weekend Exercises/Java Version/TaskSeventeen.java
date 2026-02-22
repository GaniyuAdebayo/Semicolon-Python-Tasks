public class TaskSeventeen{

	public static void main (String [] args){

		int noOfPrimeNumbers = 0;

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
				noOfPrimeNumbers++;
			}

		}

		System.out.printf("The number of prime numbers between 1 and 100 is %d%n", noOfPrimeNumbers);

	}
}