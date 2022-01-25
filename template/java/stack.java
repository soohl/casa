package algoData;

public class stack{
    private Node top;
    private int size = 0;
    public Node pop(){
        Node todoReturned = top;
        Node nextNode = top.next;
        top = null;
        top = nextNode;
        nextNode = null;
        size--;
        return todoReturned;
    }
    public void push(Object input){
        Node newNode = new Node(input);
        if (top != null){
            newNode.next = top;
            top = newNode;
        }
        top = newNode;
        size++;
    }
    public class Node{
        private Object data;
        private Node next;
        public Node(Object input){
            this.data = input;
            this.next = null;
        }
        public String toString(){
            return String.valueOf(this.data);
        }
    }
}