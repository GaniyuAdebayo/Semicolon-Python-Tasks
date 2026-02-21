public class TaskEight{

	public static void main (String [] args){
		int sum = 0;
		for (int count = 1; count <= 50; count++){
			sum += count;
		}

		System.out.printf("The sum of the first 50 natural numbers is %d%n", sum);
	}

}