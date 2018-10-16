/*
 *  implement Array in java
 */
public class LinkedList {
    private int data;
    private LinkedList nextNode;

    // constructer
    public LinkedList(int data, LinkedList nextNode) {
        this.data = data;
        this.nextNode = nextNode;
    }

    public LinkedList(int data) {
        this(data, null);
    }

    public LinkedList getNextNode() {
        return nextNode;
    }

    public void setNextNode(LinkedList nextNode) {
        this.nextNode = nextNode;
    }

    public LinkedList getNode(int idx) {
        LinkedList currList = this;

        for (int i = 0; i < idx + 1; i++) {
            currList = currList.getNextNode();
        }

        return currList;
    }

    public int getData() {
        return this.data;
    }

    public void setData(int data) {
        this.data = data;
    }

    public void getIdx(int idx) {
        if (idx == 0) {
            System.out.println(this.data);
            return;
        }

        LinkedList currList = this;

        for (int i = 0; i < idx + 1; i++) {
            if (i == idx) {
                System.out.println(currList.getData());
                return;
            }
            currList = currList.getNextNode();
        }

        //TODO
        // System.out.println("(*)out of range");
    }

    public void append(int data) {
        LinkedList currNode = this;

        while (currNode.getNextNode() != null) {
            currNode = currNode.getNextNode();
        }

        currNode.setNextNode(new LinkedList(data));
    }

    public int getLength(LinkedList list) {
        int cnt = 0;

        while (list.getNextNode() != null) {
            cnt++;
            list = list.getNextNode();
        }

        cnt++;

        return cnt;
    }

    public void printLength(LinkedList list) {
        int cnt = 0;

        while (list.getNextNode() != null) {
            cnt++;
            list = list.getNextNode();
        }

        cnt++;

        System.out.println(cnt);
    }

    //TODO
    public LinkedList remove(int idx) {
        LinkedList currList = this;
        int length = getLength(currList);

        if (idx == 0) {
            currList = currList.getNextNode();
        } else if (idx == length - 1) {
            for (int i = 0; i < length - 2; i++) {
                if (i == length - 2) {
                    currList.nextNode = null;
                } else {
                    currList = currList.getNextNode();
                }
            }
        } else {
            LinkedList strList = this;
            LinkedList endList = this;
            for (int i = idx - 1; i < idx + 2; i++) {
               if (i == idx - 1) {
                   strList = currList;
               } else if (i == idx + 1) {
                   endList = currList;
               }

               currList = currList.getNextNode();
            }

            strList.nextNode = endList;
        }

        this.print();
        return currList;
    }

    public void print() {
        StringBuffer sb = new StringBuffer();

        sb.append(data);
        sb.append(",");

        LinkedList getList = this.getNextNode();

        while (getList.getNextNode() != null) {
            sb.append(getList.getData());
            sb.append(",");
            getList = getList.getNextNode();
        }

        sb.append(getList.data);

        System.out.println(sb.toString());
    }

    public static void main(String[] args) {
        LinkedList list = new LinkedList(1);
        list.append(2);
        list.append(3);

        list.print();
        // list.printLength(list);
        list.remove(1);
    }
}
