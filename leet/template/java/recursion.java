package algoData;

public class recursion{
    private int sum = 0;
    public static void main(String[] args){
        recursion number = new recursion();
        System.out.println(number.Fibonacci(10));
    }
    int factorial(int n){
        if (n == 1){
            return 1;
        }else{
            n = n*factorial(n-1);
        }      
        return n;
    }
    int Fibonacci(int n){
        if (n == 1){
            return 0;
        }else if(n == 2){
            return 1;
        }else{
            sum = Fibonacci(n-1) + Fibonacci(n-2);
        }
        return sum;
    }
}
