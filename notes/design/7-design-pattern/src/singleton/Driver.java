package edu.gatech.oad.patterns.singleton;

/**
 * Created by robertwaters on 3/16/17.
 */
public class Driver {
    public static void main(String args[]) {

        System.out.println("Monostate: ");
        Monostate mono1 = new Monostate();
        mono1.add("bob", "bob-data");
        mono1.add("sally", "sally-data");

        System.out.println(mono1.findKey("sally"));

        Monostate mono2 = new Monostate();
        mono2.add("fred", "fred-data");
        System.out.println(mono2.findKey("bob"));

        System.out.println(mono1.findKey("fred"));


        System.out.println("\n\nSingleton: ");
        EnumSingleton es1 = EnumSingleton.INSTANCE;
        es1.addData("bob", "bob-data");
        es1.addData("sally", "sally-data");
        System.out.println(es1.getData("bob"));

        EnumSingleton es2 = EnumSingleton.INSTANCE;
        es2.addData("fred", "fred-data");
        System.out.println(es2.getData("sally"));


        System.out.println(es1.getData("fred"));
    }
}
