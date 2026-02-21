public class TaskSeven{

	public static void main (String [] args){
		int counter = 0;
		for (int count = 1; count <= 100; count++){
			if(count % 7 == 0){
				counter++;
			}
		}
		System.out.printf("The number of multiples of 7 between 1 and 100 is %d%n", counter);
	}
}