import java.util.Scanner;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import java.util.Base64;
import java.nio.charset.StandardCharsets;

public class AES {
    private Cipher ecipher;
    private Cipher decipher;


    public static void main(String[] args) {
        System.out.print("Enter any string: ");
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        try {
            // Generate a secret key
            KeyGenerator keyGen = KeyGenerator.getInstance("AES");
            keyGen.init(128); // Initialize with a key size of 128 bits
            SecretKey key = keyGen.generateKey();

            // Create an AES encrypter
            AES encrypter = new AES(key);

            // Encrypt and decrypt the input string
            String encrypted = encrypter.encrypt(input);
            String decrypted = encrypter.decrypt(encrypted);

            // Print the results
            System.out.println("Original String: " + input);
            System.out.println("Encrypted String: " + encrypted);
            System.out.println("Decrypted String: " + decrypted);
        } catch (Exception e) {
     
        }
    }

    public AES(SecretKey key) {
        try {
            ecipher = Cipher.getInstance("AES");
            ecipher.init(Cipher.ENCRYPT_MODE, key);
            decipher = Cipher.getInstance("AES");
            decipher.init(Cipher.DECRYPT_MODE, key);
        } catch (Exception e) {
        }
    }

    public String encrypt(String str) {
        try {
            byte[] utf8 = str.getBytes(StandardCharsets.UTF_8);
            byte[] enc = ecipher.doFinal(utf8);
            return Base64.getEncoder().encodeToString(enc);
        } catch (Exception e) {
            System.out.println(e);
            return null;
        }
    }

    public String decrypt(String str) {
        try {
            byte[] dec = Base64.getDecoder().decode(str);
            byte[] utf8 = decipher.doFinal(dec);
            return new String(utf8,"UTF8");
        } catch (Exception e) {
            System.out.println(e);
            return null;
        }
    }

   
}