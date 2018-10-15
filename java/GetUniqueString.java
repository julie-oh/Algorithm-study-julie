/*
    <1.3>
    Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer NOTE:
    One or two additional variables are fine An extra copy of the array is not
 */
import java.util.*;
import java.io.*;

public class GetUniqueString {
    public static void main(String[] args) {
        GetUniqueString str = new GetUniqueString();
        System.out.print(str.getString("Apple"));
    }

    public String getString(String str) {
        System.out.print(str);
        char[] cArr = new char[str.length()];
        str.getChars(0, str.length(), cArr, 0);
        for (int i = 0; i < cArr.length; i ++) {
            if (i != ' ') {
                for (int j = i + 1; j < cArr.length; j++) {
                    if (cArr[i] == cArr[j]) {
                        cArr[i] = ' ';
                    }
                }
            }
        }

        // second Way
        for (int i = 0; i < cArr.length; i++) {
            if (cArr[i] == ' ') {
                if (i == cArr.length - 1) {
                    // cArr.remove(i);
                    continue;
                }
                for (int j = i; i < cArr.length; j++) {
                    if (j == cArr.length - 1) {
                        // cArr.remove(j);
                        break;
                    }
                    cArr[j] = cArr[j+1];
                }
            }
        }

        return new String(cArr);

        //return str;
    }


}
