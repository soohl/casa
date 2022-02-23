package algoData;

public class Main{
    public static void main(String[] args){
        LinkedList numbers = new LinkedList();
        numbers.addLast(30);
        numbers.addLast(20);
        numbers.addLast(10);
        numbers.addLast(14);
        LinkedList.ListIterator i = numbers.listIterator();
        while (i.hasNext()){
            if ((int)i.next() == 10)
                i.add(20);
        }
        System.out.println(numbers);
    }
}