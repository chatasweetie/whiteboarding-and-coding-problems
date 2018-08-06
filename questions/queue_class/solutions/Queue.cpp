#include <memory>
#include <iostream>
#include <initializer_list>

using namespace std;

template<typename T>
class Queue{
    struct Node{
        T data;
        struct Node* next;
        struct Node* prev;
    };

    Node* front = nullptr;
    Node* back = nullptr;
    size_t size = 0;

    public:    
    Queue() = default;
    Queue(const Queue& q){
        Node* it = q.front;
        while(it){
            enqueue(it->data);
            it = it->prev;
        }
    };
    Queue(const initializer_list<T>& initial) {
        for(T x : initial)enqueue(x);
    }
    ~Queue(){
        Node* it = front;
        while(it){
            Node *rem = it;            
            it = it->prev;
            delete rem;
        }
    }
    Queue& operator=(const Queue& other){
        return *this(other);
    }

    T& first(){ return front->data; }
    T& last(){  return back->data;  }
    
    void enqueue(const T& item){
        Node* node = new Node{item, back, nullptr};
        if(back)back->prev = node;
        if(!front)front = node;
        back = node;  
        size++;              
    }
    
    bool isEmpty(){
        return size == 0;
    }

    T dequeue(){
        if(!front)throw "queue empty";
        T data = front->data;
        Node *last = front;        
        front = front->prev;        
        if(front)front->next = nullptr;        
        delete last;        
        size--;
        if(!size){
            front = nullptr;
            back = nullptr;
        }
        return data;
    }    
};



int main(){
    Queue<int> q1{1, 2, 3, 4};
    cout << "front: " << q1.first() << endl;
    q1.enqueue(10);
    q1.enqueue(11);
    q1.enqueue(12);
    while(!q1.isEmpty())cout << "dequeue: " << q1.dequeue() << endl;

    Queue<char> q2{'c', 'a', 't', 'z'};
    cout << "q2: " << q2.dequeue() << endl;
    q2.enqueue(' ');
    q2.enqueue('m');
    q2.enqueue('e');
    q2.enqueue('o');
    q2.enqueue('w');
  
    Queue<char> q3 = q2;
    while(!q2.isEmpty())cout << "dequeue: " << q2.dequeue() << endl;

    cout << "done" <<endl; 
    return 0;
}