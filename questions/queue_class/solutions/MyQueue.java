// FIFO
// Operations o(1)
// space/search o(n)
class MyQueue{
    public static class QueueNode<t>{
        QueueNode<t> next;
        T data;

        public QueueNode(T data){
            this.data = data;
        }
    }

    // necesary to for operations on queue 
    private QueueNode<T> first;
    private QueueNode<T> last;

    // adds a node to the last node in the queue
    public void add(T data){
        QueueNode newNode = new QueueNode<>(data);

        // if queue is empty
        if (this.last != null){
            this.last.next = newNode;
        }
        
        last = newNode;

        // if queue is only one node
        if (this.first == null){
            this.first = this.last;
        }
    }

    // removes the first node of the queue
    // returns the data from the first node of the queue
    public T remove(){

        // if queue is empty
        if (this.first == null){
            System.out.println("Error. Cannot remove -- queue is empty.");
        }
        
        // save data to return + update first node to next
        T data = this.first.data;
        this.first = this.first.next;

        // if the queue is only one node
        if (this.first == null){
            this.first = this.last;
        }
        return data;
    }

    public T peek(){
        if (this.first == null){
            System.out.println("Error. Cannot peek -- queue is empty.");
        }
        return this.first.data;
    }

    public boolean isEmpty(){
        return this.first == null;
    }
}