public class RC4 {
    String strPlainText;
    static char[] cipher;

    RC4(String strPlainText, int[] key) {
        this.strPlainText = strPlainText;
        cipher = new char[strPlainText.length()];
        int[] S = new int[256]; // changed from 255 to 256

        for (int i = 0; i < S.length; i++) {
            S[i] = i;
        }

        int i = 0;
        int j = 0;

        for (int k = 0; k < strPlainText.length(); k++) {
            int modk = k % key.length;
            int Kc = key[modk];

            j = (j + S[i] + Kc) % 256; // removed the +1

            int temp = S[i];
            S[i] = S[j];
            S[j] = temp; // swapped the values

            int Sc = (S[i] + S[j]) % 256;
            int Ck = S[Sc];

            cipher[k] = (char) (Ck ^ (int) strPlainText.charAt(k)); // changed from Aint to ^
        }
    }

    public static void main(String[] args) {
        int[] K = {1, 2, 3, 4, 5};
        String strOriginal = "Hello World";

        System.out.println("Original String ---> " + strOriginal);
        System.out.println("Encrypted String: ");
        new RC4(strOriginal, K);
        for (int i = 0; i < cipher.length; i++) {
                
                    System.out.print(" " + cipher[i]);
         
        }
        

    }
}