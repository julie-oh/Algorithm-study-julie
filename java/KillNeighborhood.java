/*
 *  <1.7>
 *  Write am algorithm such that if an element in an MxN matrix,
 *  its entire row and column is set to 0
 *
 *  time complexity:
 *  space complexity:
 *
 */
import java.util.*;

public class KillNeighborhood {
    public static void main(String[] args) {
        KillNeighborhood kn = new KillNeighborhood();
        int[][] arr = {{1,2,3}, {4,5,6}, {7,8,9}};

        System.out.println(kn.getTown(arr, 3, 3));
    }

    public String getTown(int[][] arr, int row, int col) {
        row -= 1;
        col -= 1;

        for (int i = 0; i < arr[row].length; i++) {
            arr[row][i] = 0;
        }

        for (int i = 0; i < arr.length; i++) {
            arr[i][col] = 0;
        }

        return Arrays.deepToString(arr);
    }
}
