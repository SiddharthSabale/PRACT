import java.util.Scanner;

public class Trans {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a message: ");
        String text = sc.nextLine();
        int l = text.length();
        int row = (l + 3) / 4;
        char[][] a = new char[row][4];
        int k = 0;

        System.out.println("\nMatrix: ");
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < 4; j++) {
                if (k < l) {
                    a[i][j] = text.charAt(k++);
                    System.out.print(a[i][j] + " ");
                }
            }
            System.out.println();
        }

        System.out.println("Enter a key: ");
        int[] key = new int[4];
        for (int i = 0; i < 4; i++) {
            key[i] = sc.nextInt();
        }

        String s = "";
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < row; j++) {
                if (a[j][key[i]] != '\0') {
                    s += a[j][key[i]] + " ";
                }
            }
        }

        System.out.println("Cipher text: " + s);
    }
}