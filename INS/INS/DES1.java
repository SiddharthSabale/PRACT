import java.util.Scanner;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class DES1 {
    private Cipher ecipher;
    private Cipher decipher;

    public static void main(String[] args) {
        System.out.println("Enter any String");
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        try {
            SecretKey key = KeyGenerator.getInstance("DES").generateKey();
            DES1 encrypter = new DES1(key);
            String encrypted = encrypter.encrypt1(input);
            String decrypted = encrypter.decrypt1(encrypted);
            System.out.println("Original String is: " + input);
            System.out.println("Encrypted String is: " + encrypted);
            System.out.println("Decrypted String is: " + decrypted);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public DES1(SecretKey key) throws Exception {
        ecipher = Cipher.getInstance("DES");
        ecipher.init(Cipher.ENCRYPT_MODE, key);
        decipher = Cipher.getInstance("DES");
        decipher.init(Cipher.DECRYPT_MODE, key);
    }

    public String encrypt1(String str) {
        try {
            byte[] utf8 = str.getBytes(StandardCharsets.UTF_8);
            byte[] enc = ecipher.doFinal(utf8);
            return Base64.getEncoder().encodeToString(enc);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
            return null;
        }
    }

    public String decrypt1(String str) {
        try {
            byte[] dec = Base64.getDecoder().decode(str);
            byte[] utf8 = decipher.doFinal(dec);
            return new String(utf8, StandardCharsets.UTF_8);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
            return null;
        }
    }
}