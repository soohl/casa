import java.util.Scanner;
public class javaassign2{
    public static void leapyear_checker(){
        Scanner in = new Scanner(System.in);
        System.out.println("Enter a year: ");
        int year = in.nextInt();
        if (year % 4 == 0)
            System.out.println("Leap year!");
        else
            System.out.println("Not a leap year!");
    }
    
    public static void leapyear_finder(){
        int start_year = 1999;
        int end_year = 2016;
        int i, n = 0;
        
        for (i = start_year; i<=end_year; i++){
            if (i % 4 == 0){
                System.out.println(i);
                n++;
            }
        }
        System.out.println("Number of leap year between "+ String.valueOf(start_year)+"~"+String.valueOf(end_year)+" is "+ String.valueOf(n));
    }
    
    public static void reverse_num(){
        Scanner in = new Scanner(System.in);
        System.out.print("Enter number: ");
        int num = in.nextInt();
        int digit;
        int reversed = 0;
        boolean negative = false;
        if (num < 0){
            num *= -1;
            negative = true;
        }
        while (num!=0){
            digit = (int) num %10;
            reversed = reversed*10+digit;
            num /= 10;
        }
        if (negative == true){
            System.out.println("Reversed number is " +"-" + String.valueOf(reversed)); 
        }else{
            System.out.println("Reversed number is " + String.valueOf(reversed));
        }
    }
    
    public static void vc_counter(){
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a String: ");
        String s = in.nextLine();
        int l = s.length();
        char c;
        int v_num = 0, c_num = 0, i;
        for (i = 0; i< l; i++){
            c = s.charAt(i);
            if (vowel_checker(c)){
                v_num++;
            }else{
                c_num++;
            } 
        }
        System.out.println("Number of vowels is "+String.valueOf(v_num));
        System.out.println("Number of consonants is "+String.valueOf(c_num));
    }
    
    public static boolean vowel_checker(char c){
        switch (c){ // if any of the case is true, it goes to case 'u' and return true
           case 'a':
           case 'e':
           case 'i':
           case 'o':
           case 'u': return true; 
           default : return false; 
        }
    }
}
