
import java.util.Scanner;

public class vernam {

public static void main(String[] args) {
String text,key,output="",dec="";
char t,k;
int x;
Scanner s = new Scanner(System.in);
System.out.println("Enter text to Encrypt/Decrypt:");
text=s.nextLine();
System.out.println("Enter One Time Password: ");
key=s.nextLine();
for(int i=0;i<text.length();i++)
{
t=text.charAt(i);
k=key.charAt(i);
x=t^k;
output+=(char)x;//small 97 to 122
}
System.out.println("Encrypted Text is:"+output);
for(int i=0;i<output.length();i++)
{
t=output.charAt(i);
k=key.charAt(i);
x=t^k;
dec+=(char)x;
}
System.out.println("Decrypted Text is:"+dec);
}
}