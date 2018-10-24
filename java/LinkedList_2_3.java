/*
 *  (!!!!!)don't modify index of list or array in for-loop
 *
 *   <2.4>
 *   You have two numbers represented by a linked list, where each node contains a single dligit.
 *   The digits are stored in reverse in reverse order, such that the 1's digit is at the head of the list.
 *   Write a function that adds the two numbers and returns the sum as a linked list.
 *
 */
import java.util.*;

public class LinkedList_2_3 {
    public LinkedList<Integer> getPartiton(LinkedList<Integer> list, int val) {
        System.out.println('a');
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) < val) {
                list.addFirst(list.get(i));
                list.remove(i + 1);
            }
        }

        System.out.println(list.toString());
        return list;
    }

    public static void main(String[] arg) {
        LinkedList<Integer> list = new LinkedList<Integer>();
        list.add(1);
        list.add(2);
        list.add(11);
        list.add(329);
        list.add(102);
        list.add(0);
        list.add(-3);
        list.add(0);
        list.add(12);
        list.add(5);
        list.add(9);

        LinkedList_2_3 partition = new LinkedList_2_3();
        partition.getPartiton(list, 11);
    }
}