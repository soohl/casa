package algoData;

public class queue{
    private Node front;
    private Node rear;
    private int size = 0;
 
    public void enqueue(Object input){
        Node newNode = new Node(input);
        if (size != 0){
            newNode.next = front;
        }
        front = newNode;
        rear = newNode;
        size++;
    }
    public Node dequeue(){
        if (size == 0){
            return null;
        }else{
            
            return rear;
            
        }
    }
    public class Node{
        private Object data;
        private Node next;
        Node(Object input){
            this.data = input;
            this.next = null;
        }
    }
}