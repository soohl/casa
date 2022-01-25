import java.util.Scanner;

class StringMethods{

    public void trim(){
        String s;
        Scanner in  = new Scanner(System.in);
        System.out.print("Enter any String");
        s = in.next();
        System.out.println(s);
        System.out.println(s.trim());
    }
    
    public void with(){
        String s, s1, s2;
        Scanner in  = new Scanner(System.in);
        System.out.print("Enter any String");
        s = in.next();
        s1 = in.next();
        s2 = in.next();
        
        System.out.println(s.startsWith(s1));
        System.out.println(s.endsWith(s2));
    }
    
    public void charat(){
        String s;
        Scanner in  = new Scanner(System.in);
        System.out.print("Enter any String");
        s = in.next();
        System.out.println(s.charAt(0));
        System.out.println(s.charAt(3));
    }
    
    public void interns(){
        String s;
        Scanner in  = new Scanner(System.in);
        System.out.print("Enter any String");
        s = in.next();
        String s1 = new String(s);
        String s2 = s.intern();
        System.out.println(s2);
    }
    
    public void valueof(){
        int a = 10;
        String s = String.valueOf(a);
        System.out.println(s+10);
    }
    
    public void replaces(){
        String s;
        Scanner in  = new Scanner(System.in);
        System.out.print("Enter any String");
        s = in.next();
        String s1 = "Java is a programming language. Java is a platform. Java is an island";
        String replaceString = s1.replace("Java", "Kava");
        System.out.println(replaceString);
    }
    
    public void compare(){
        
        String s1 = "hello";
        String s2 = "hello";
        String s3 = "meklo";
        String s4 = "hemlo";
        System.out.println(s1.compareTo(s2));
        System.out.println(s1.compareTo(s3));
        System.out.println(s1.compareTo(s4));
    }
    
    public void concats(){
        String s;
        Scanner in  = new Scanner(System.in);
        System.out.print("Enter any String");
        s = in.next();
        String s1 = "java string";
        s1.concat("is immutable");
        System.out.println(s1);
        s1 = s1.concat(" is immutable so assign it explicitly");
        System.out.println(s1);
    }
    
    public void equal(){
        String s1 = "javatpoint";
        String s2 = "javatpoint";
        String s3 = "JAVATPOINT";
        String s4 = "python";
        System.out.println(s1.equals(s2));
        System.out.println(s1.equals(s3));
        System.out.println(s1.equals(s4));
    }
}
    
