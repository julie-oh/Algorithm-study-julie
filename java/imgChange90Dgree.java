import java.util.*;

/*
 *  <1.5>
 *
 * Given an image represented by an NxN matrix,
 * where each pixel in the image is 4 bytes,
 * write a method to rotate the image by 90 degrees.
 * Can you do this in place?
 *
 * time Complexity:
 * space Complexity:
 *
 */
//TODO 다차원 배열
public class imgChange90Dgree {
    public static void main(String[] args) {
        // list = new int[3][3];
        int[][] list = new int[][]{{1,2,3}, {4,5,6}, {7,8,9}};
        System.out.println("main:   "+Arrays.deepToString(list));

        imgChange90Dgree imgBox = new imgChange90Dgree();

        System.out.println(imgBox.getPlace(list));
    }

    public String getPlace(int[][] list) {
        int lLen = list.length;
        int[][] nList = new int[lLen][lLen];

        int index = 0;
        for (int i = list.length - 1; i >= 0; i--) {
            for (int j = 0; j < list[i].length; j++) {
                nList[j][index] = list[i][j];
            }

            index++;
        }
        return Arrays.deepToString(nList);
    }
}
