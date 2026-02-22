public class TaskSeven{

	public static void main (String [] args){

		int total = 0;

		for (int count = 1; count <= 100; count++){
			total += count;
		}

		double average = (double) total/100;

		System.out.printf("The average is %.2f%n", average);
	}
}