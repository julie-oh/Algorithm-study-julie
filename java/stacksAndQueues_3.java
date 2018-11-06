import java.util.LinkedList;
import java.util.Random;

public class stacksAndQueues_3 {
    public int maxSize = 10;
    private LinkedList<LinkedList<Integer>> stackList;

    // constructor
    public stacksAndQueues_3() {
        stackList = new LinkedList<>();  // size 0 init
        stackList.add(new LinkedList<>());
    }

    public void push(int value) {
        LinkedList<Integer> lastStack = stackList.getLast();
        if (lastStack.size() >= maxSize) {  // full
            LinkedList<Integer> newStack = new LinkedList<Integer>();
            newStack.push(value);
            stackList.add(newStack);  // created new stack
        } else {
            lastStack.push(value);
        }
    }

    public static void main(String[] args) {
        LinkedList stack = new LinkedList();
        Random ran = new Random();

        for (int i = 0; i < 11; i++) {
            int num = ran.nextInt(20)+1;
            stack.push(num);
        }

        stack.push(200);
    }
}
