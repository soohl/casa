import java.util.Scanner;
import java.lang.Math;

public class javaassign1{
    public void question1(){
        Scanner in = new Scanner(System.in); //a^2+bx+c
        System.out.print("Enter a: ");
        int a = in.nextInt();
        
        System.out.print("\nEnter b: ");
        int b = in.nextInt();
        
        System.out.print("\nEnter c: ");
        int c = in.nextInt();
        
        double disc = (b*b-4*a*c); //b^2-4ac
        int nature = -1; //0 = no root, 1 = one root; 2 = two roots
        System.out.print("\n");
        if (disc < 0){ //no root    
            nature = 0;
            System.out.println("no root " + nature);
        }
        else{
            if (disc > 0){ //two roots
                nature = 2;
                double root1 = (-b+Math.sqrt(disc)) / (2 * a);
                double root2 = (-b-Math.sqrt(disc)) / (2 * a);
                System.out.printf("%.3f, %.3f, %d",root1,root2,nature); //round up to 3 decimal places
            }
            else{ //one root
                nature = 1;
                double root = (-b) / (2 * a);
                System.out.printf("%.3f, %d",root,nature);
            }
        }
    }    
    
    public void question2(){ 

        String[] a = new String[10];
        Scanner in = new Scanner(System.in);
        for (int n = 0; n<10; n++){ //input name and append to array
            System.out.print("Input a name: ");
            a[n] = in.nextLine();
            System.out.print("\n");
        }
        
        int len = a.length;
        int shortest = 20;
        int count = 0;
        String temp;
        
        for (int z=0; z<len; z++){ //print sorted array;
            System.out.print(a[z]+" ");
        }
        System.out.print("\n");
        
        for (int t = 0; t<len; t++){ //find name with shortest length
            if (a[t].length() < shortest){
                shortest = a[t].length();
            }
        }
        
        for (int r = 1; r<len; r++){ // Repeat until all are sorted
            for (int i=0; i<len-1; i++){ //a[0] a[1] a[3] a[4] ...
                for (int x=0; x<shortest; x++){ // shawn -> s to h, h to a... 
                    String x1 = a[i];
                    String x2 = a[i+1];
                    int a1 = (int)(x1.charAt(x));
                    int a2 = (int)(x2.charAt(x));
                    if (a1 < a2)
                        break;
                        
                    if (a1 > a2){
                        temp = x1;
                        a[i] = x2;
                        a[i+1] = temp;
                        count++;
                        break;
                    }
                    
                }
            } 
            if (count == 0) //if nothing need to be sorted
                break;
            else
                count = 0;
        }
        for (int z=0; z<len; z++){ //print sorted array;
            System.out.print(a[z]+" ");
        }
    }
    
    public void question3(){
        System.out.print("Enter 5 digits number: ");
        Scanner in = new Scanner(System.in);
        String s = in.nextLine();
        int len = s.length(); //length of input number
        int num = Integer.parseInt(s); //input number in integer
        int even = 0;
        int digit = 0;
        for (int i = 0; i < len; i++){
            digit = (int)(num / Math.pow(10,i)) % 10; // (num / (10^i)) % 10;
            if (digit%2 == 0) //if digit is even
                even += digit; //sum all the even digits
            }      
        System.out.println(even);
    }
    
    public void question4(){
        boolean run = true;
        boolean go = true;
        Scanner in = new Scanner(System.in);
        while (go){
            while (run){
                System.out.println("\n=================");
                System.out.println("1.Factorial");
                System.out.println("2.Area of circle");
                System.out.println("3.Area of square");
                System.out.println("4.Pythagoras theorem calculator");
                System.out.println("5.EXIT");
      
                int a = in.nextInt();
                switch (a){
                    case 1: factorial();break;
                    case 2: area_circle();break;
                    case 3: area_square();break;
                    case 4: pythagoras();break;
                    case 5: System.out.println("BYEE");System.exit(0);
                    default: System.err.println("Invalid option selected"); run = false; 
                }
            } 
            System.out.println("Would you like to run again? Y/N");
            char runa = in.next().charAt(0);
            runa = Character.toUpperCase(runa);
            
            if (runa == 'Y')
                run = true;
            else if (runa == 'N'){
                System.out.println("Goodbye");
                System.exit(0);
                go = false;
            }
            else{
                System.out.println("Invalid entry. Try again");
            }
        }
    }
    public void factorial(){
        System.out.print("Enter a factorial number: ");
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        int total = 1;
        for (int i=1; i<=num; i++){
            total = total*i;
        }
        System.out.println(total);
    }
    
    public void area_circle(){
        System.out.print("Enter a radius: ");
        Scanner in = new Scanner(System.in);
        double r = in.nextInt();
        double area = Math.PI*r*r;
        System.out.printf("\n%.3f",area);
    }
    
    public void area_square(){
        System.out.print("Enter a side length: ");
        Scanner in = new Scanner(System.in);
        int s = in.nextInt();
        int area = s*s;
        System.out.println(area);
    }
    
    public void pythagoras(){
        Scanner in = new Scanner(System.in);
        System.out.print("Enter s1: ");
        int s1 = in.nextInt();
        System.out.print("\nEnter s2: ");
        int s2 = in.nextInt();
        double h = Math.sqrt(s1*s1+s2*s2);
        System.out.printf("\n%.3f", h);
    }
    public void question5(){
        System.out.print("Enter number from 000 ~ 999: ");
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        
        int c = num%10;
        int b = (int)(num/10)%10;
        int a = (int)(num/100);
        int cube = (int)Math.pow(a,3) + (int)Math.pow(b,3) + (int)Math.pow(c,3);
        if (cube == num)
            System.out.println(num+ " is Amstrong number");
         else
            System.out.println(num+ " is not Amstrong number");
    }

    public void question6(){
        int cube;
        for (int a = 0; a <= 9; a++){ //100th digit 
            for (int b = 0; b <= 9; b++){ //10th digit 
                for (int c = 0; c <= 9; c++){ //1th digit 
                    cube = (int)Math.pow(a,3) + (int)Math.pow(b,3) + (int)Math.pow(c,3); // a^3+b^3+c^3 = abc
                    int num = a * 100 + b * 10 + c;
                    if (cube == num)
                        System.out.print(num + " ");
                    }
                }
            }
        }
    }
 
    
