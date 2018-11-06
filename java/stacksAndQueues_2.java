import java.util.*;
import java.io.*;

/*
 *  How would you design a stack which, in addition to push, also has a function min which returns the minimum element?
 *  Push, and min should all operate in 0(1) time
 */
public class stacksAndQueues_2 {
    public int min(LinkedList<Integer> stack) {
        int min = stack.get(0);

        for (int i = 1; i < stack.size(); i++) {
            int val = stack.get(i);

            if (min > val) min = val;
        }

        System.out.println(min);
        return min;
    }

    public LinkedList<Integer> push(LinkedList<Integer> stack, int val) {
        stack.push(val);

        System.out.println(stack);
        return stack;
    }

    public void pop(LinkedList<Integer> stack) {
        int lastIdx = stack.size() - 1;
        int popValue = stack.get(lastIdx);
        stack.remove(lastIdx);

        System.out.println(popValue);
    }

    /*
    private HashMap<String, Integer> hash;
    private void getHashMap(LinkedList stack) {
        if (this.hash.size() == 0) {
            int min = 0;

            for (int i = 0; i < stack.size(); i++) {
                int val = (int)stack.get(i);
                if (min > val) {
                    min = val;
                }
            }

            this.hash.put("min", min);
        }
    }
    */

    public static void main(String[] args) {
        Random ran = new Random();
        LinkedList stack = new LinkedList();
        stacksAndQueues_2 implementStack = new stacksAndQueues_2();

        for (int i = 0; i < 20; i++) {
            int num = ran.nextInt(50)+1;
            stack.push(num);
        }
        System.out.println(stack);

//        implementStack.min(stack);

        implementStack.pop(stack);
        System.out.println(stack);
    }
}
