/*
 *   <1.5>
 *   Write a method to replace all space in a String with "%20"
 *
 *   time Complexity: o(n2)
 *   space Complexity: o(n2)
 */

import java.util.*;
import java.io.*;

public class InsertString {
    public static void main(String[] args) {
        InsertString test = new InsertString();
        System.out.println(test.getString("I am julie Oh"));
    }

    public String getString(String str) {
        StringBuffer sb = new StringBuffer();

        for (int i = 0; i < str.length(); i++) {
            char s = str.charAt(i);

            if (s == ' ') sb.append("%20");
            else sb.append(s);

        }

        return sb.toString();
    }
}
