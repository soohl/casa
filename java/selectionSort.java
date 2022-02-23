package algoData;

import java.lang.Math;
public class selectionSort{
    public static void main(String[] args){
        int[] list = new int[10];
        for (int i=0; i< list.length; i++){
            list[i] = (int)(Math.random()*10);
        }
        
        //selction sort ascending 
        for (int i = 0; i< list.length; i++){
            for (int k = i+1; k<list.length; k++){
                if (list[i] > list[k]){
                    int temp = list[i];
                    list[i] = list[k];
                    list[k] = temp;
                }
            }
        }
        for (int i = 0; i<list.length; i++){
            System.out.print(list[i]+",");
        }
    }
}