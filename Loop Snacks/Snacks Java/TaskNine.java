public class TaskNine{

	public static void main (String [] args){
		int product = 1;
		for (int count = 1; count <= 10; count++){
			product *= count;
		}
		System.out.printf("The product of the first 50 natural numbers is %d%n", product);
	}

}