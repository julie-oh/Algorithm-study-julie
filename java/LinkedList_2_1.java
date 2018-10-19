/*
 *  <2.1>
 *  Write code to remove duplicates from an unsorted linked list.
 *  FOLLOW UP
 *  How would you solve this problem if a temporary buffer is nor allowd?
 */
import java.util.*;

public class LinkedList_2_1 {
    public LinkedList<Integer> rmDuplication(LinkedList list) {
        HashMap<Integer, Integer> hash = new HashMap<>();

        for (int i = 0; i < list.size(); i++) {
            int key = (Integer)list.get(i);

            if (hash.containsKey(key)) {
                hash.put(key, hash.get(key) + 1);
            } else {
                hash.put(key, 1);
            }
        }

        for (int i = 0; i < list.size(); i++) {
            int key = (Integer)list.get(i);

            if (hash.get(key) > 1) {
                list.remove(i);
            }
        }

        System.out.println(list);
        return list;
    }

    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList();

        list.add(1);
        list.add(2);
        list.add(3);
        list.add(1);
        list.add(4);
        list.add(6);
        list.add(4);

        LinkedList_2_1 linkedlist = new LinkedList_2_1();
        linkedlist.rmDuplication(list);
    }
}
