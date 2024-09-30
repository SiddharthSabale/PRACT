import java.util.Scanner;

public class ceasar63 {
    public static String encryptText(String inputStr, Integer key) {
        String encText = "";
        for (int i = 0; i < inputStr.length(); i++) {
            int c = inputStr.charAt(i);

            if (Character.isUpperCase(c)) {
                c = c + (key % 26);
                if (c > 'Z')
                    c = c - 26;
                    
            } else if (Character.isLowerCase(c)) {
                c = c + (key % 26);
                if (c > 'z')
                    c = c - 26;
            }
            encText += (char) c;
        }
        return encText;
    }

    public static String decryptText(String inputStr, Integer key) {
        String decText = "";
        for (int i = 0; i < inputStr.length(); i++) {
            int c = inputStr.charAt(i);
            if (Character.isUpperCase(c)) {
                c = c - (key % 26);
                if (c < 'A')
                    c = c + 26;
            } else if (Character.isLowerCase(c)) {
                c = c - (key % 26);
                if (c < 'a')
                    c = c + 26;
            }
            decText += (char) c;
        }return decText;}
        
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Input Text to encrypt: ");
        String inputStr = sc.nextLine();

        System.out.print("Input key length: ");
        Integer encKey = sc.nextInt();
        
        sc.nextLine(); // consume newline left-over
        
        String encryptedString = encryptText(inputStr, encKey);
        System.out.println("Encrypted Text is: " + encryptedString);
        
        String decryptedString = decryptText(encryptedString, encKey);
        System.out.println("Decrypted Text is: " + decryptedString);}}