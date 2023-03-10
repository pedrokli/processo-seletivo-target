
public class exercicio2 {
	
	public static void main(String[] args) {
	
				int i = 20;
				System.out.println("fibonacci(" + i + ") = " + fibonacci(i) );
				
			
			
		
		
	}
	public static int fibonacci(int n) {
		return n < 2 ? n : (fibonacci(n - 1) + fibonacci (n - 2));
	}


}
