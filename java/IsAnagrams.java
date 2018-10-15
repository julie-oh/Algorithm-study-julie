/*
 *  <1.4>
 *  Write a method to decide if two strings are anagrams or not
 *  apple
 *  pelaa
 *
 *  Time complexity: O(n)
 *  Space complexity: O(n)
 */

import java.util.*;
import java.io.*;

public class IsAnagrams {
    public static void main(String[] args) {
        IsAnagrams isAnag =  new IsAnagrams();
        char[] a = "listen".toCharArray();  // O(n)
        char[] b = "slient".toCharArray();
        System.out.println(isAnag.compareString2("listen", "slient"));  // true
        System.out.println(isAnag.compareString2("apple", "pelaa"));  // false
        System.out.println(isAnag.compareString2("tea", "te"));  // false
        System.out.println(isAnag.compareString2("ttea", "teaa"));  // false
    }

    public Boolean compareString(char[] a, char[] b) {
        if (a.length == 0 || b.length == 0) {
            return false;
        }

        if (a.length !=  b.length) {
            return false;
        }

        Arrays.sort(a);  // O(nlogn)
        Arrays.sort(b);

        // O(n)
        for (int i = 0; i < a.length; i++) {
            if (a[i] != b[i]) {
                return false;
            }
        }

        // O(n) + O(nlogn)  =  O(nlogn)
        return true;
    }

    public boolean compareString2(String a, String b) {
        if (a.length() != b.length()) return false;
        HashMap<Character, Integer> hashA = new HashMap<>();
        HashMap<Character, Integer> hashB =new HashMap<>();

        for (int i = 0; i < a.length(); i++) {
            char c = a.charAt(i);
            char d = b.charAt(i);

            if (hashA.containsKey(c)) {
                int intA = hashA.get(c);
                hashA.put(c, intA + 1);
            } else {
                hashA.put(a.charAt(i), 1);
            }

            if (hashB.containsKey(d)) {
                int intB = hashB.get(d);
                hashB.put(c, intB + 1);
            } else {
                hashB.put(b.charAt(i), 1);
            }
        }

        for (Map.Entry<Character, Integer> entry : hashA.entrySet()) {
            Character key = entry.getKey();
            Integer value = entry.getValue();

            if (hashB.containsKey(key)) {
                if (hashB.get(key) != value) {
                    return false;
                }
            } else {
                return false;
            }
        }
        return true;
    }
}