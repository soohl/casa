import java.util.Scanner;
import java.io.*;
import java.lang.Math;

public class binaryDenaryConverter{  
    public void dtb(){
        System.out.print("Enter denary numer: ");
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        int remainder = 0;
        int a=0;
        int[] result = new int[8];
        
        do{
            remainder = num%2;
            result[a] = remainder;
            num = num/2;
            a++;
        }while(num != 0);
        
        int l=result.length;
        for (int i=l-1;i>=0;i--){ //print reversed order
            System.out.print(result[i]);
        }
    
    }
    
    public void btd(){
        System.out.print("Enter binary number: ");
        Scanner in = new Scanner(System.in);
        long num = in.nextLong();
        int l = (String.valueOf(num).length());
        int digit;
        int result = 0;
        for (int a = 1; a <= l; a++){
            digit = (int)(num / Math.pow(10,a))%10;
            System.out.println(digit);
            result += digit*Math.pow(2,a);
        }
        if ((String.valueOf(num).charAt(0) == 0)){
            result+=1;
        }
        System.out.println(result);
    }
}
