import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.security.MessageDigest;
import java.util.Scanner;

public class md5 {
public static void main(String[] args) {
String input;

byte buffer[]=new byte[1024];
System.out.println("Enter The Message To Be Send: ");
try
{
Scanner sc=new Scanner(System.in);
input=sc.nextLine();
FileOutputStream fos=new FileOutputStream("abc.txt");
ObjectOutputStream oos=new ObjectOutputStream(fos);
MessageDigest md=MessageDigest.getInstance("MD5");
buffer=input.getBytes();
md.update(buffer);
oos.writeObject(input);
oos.writeObject(md.digest());
System.out.println("Message Sent Successfully ");
}
catch(Exception e)
{
e.printStackTrace();}}}
