package algoData;

public class dynamicPg{
    public static void main(String[] args){
        dynamicPg object = new dynamicPg();
        System.out.println(object.Fibonacci(10));
    } 
    
    int Fibonacci(int n){
        //memoization use more memoery, take less time instead. 
        int[] dicFibonacci  = new int[n];
        dicFibonacci[0] = 0;
        dicFibonacci[1] = 1;
        for (int i = 2; i<n; i++){
            dicFibonacci[i] = dicFibonacci[i-1] + dicFibonacci[i-2];
        }
        
        for (int i = 0; i<n; i++){
            System.out.print(dicFibonacci[i]+",");
        }
        return dicFibonacci[n-1];
    }
}