/*
 *  (*) if statement brace careful (ex. if (a) return a;)
 */

import java.util.*;

public class LinkedList_2_4 {
    public LinkedList<Integer> getList(final LinkedList<Integer> list, final LinkedList<Integer> list2) {
        boolean isPlus = false;
        LinkedList<Integer> reList = new LinkedList<>();

        for (int i = 0; i < list.size(); i++) {
            int val = list.get(i) + list2.get(i);

            if (isPlus) {
                val += 1;
                isPlus = false;
            }

            if (val > 9) {
                isPlus = true;
                val -= 10;
            }

            reList.add(val);
        }

        if (isPlus) {
            reList.add(1);
        }

        System.out.println(reList);
        return reList;
    }

    public static void main(String[] args) {
        LinkedList_2_4 linkedlist = new LinkedList_2_4();
        LinkedList<Integer> list = new LinkedList<>();
        LinkedList<Integer> list2 = new LinkedList<>();
        list.add(8);
        list.add(0);
        list.add(8);

        list2.add(5);
        list2.add(9);
        list2.add(1);

        linkedlist.getList(list, list2);
    }
}
