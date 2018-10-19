/*
 *  implement LinkedList example in 'cracking the coding interview <2.2>'
 *
 *  <2.2>
 *  Implement an algorithm to find the nth to last element of a singly linked list.
 */
import java.util.*;

public class LinkedList_2_2 {
    public LinkedLists getNthToLast(LinkedLists list, int nth) {
        for (int i = 0; i < nth; i ++) {
            LinkedLists next = list.getNextNode();

            if (i == nth - 1) {
                list.setNextNode(false);
                list = next;
                list.print();
                return list;
            }

            list = next;
        }

        return list;
    }

    public static void main(String[] args) {
        LinkedList_2_2 nthToLast = new LinkedList_2_2();
        LinkedLists list = new LinkedLists(1);
        list.append(2);
        list.append(3);

        nthToLast.getNthToLast(list, 1);
    }
}

