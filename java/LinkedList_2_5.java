import java.util.HashMap;
import java.util.LinkedList;

public class LinkedList_2_5 {
    public char getBeginNode(LinkedList<Character> list) {
        char re = ' ';
        HashMap<Character, Boolean> hash = new HashMap();
        for (int i = 0; i < list.size(); i++) {
            if (hash.containsKey(list.get(i))) {
                re = list.get(i);
                break;
            } else {
                hash.put(list.get(i), false);
            }
        }

        System.out.println(re);
        return re;
    }
    public static void main(String[] args) {
        LinkedList<Character> list = new LinkedList<>();
        list.add('a');
        list.add('b');
        list.add('c');
        list.add('d');
        list.add('e');
        list.add('c');

        LinkedList_2_5 getNode = new LinkedList_2_5();
        getNode.getBeginNode(list);
    }
}