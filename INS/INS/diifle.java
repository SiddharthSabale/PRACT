import java.util.Scanner;

public class diifle {
public static void main(String[] args) {
    
Scanner sc = new Scanner(System.in);

System.out.print("Enter value of A & B: ");
int a = sc.nextInt();
int b = sc.nextInt();

System.out.print("Enter a Prime number P: ");
int p = sc.nextInt();

System.out.print("Enter Primitive root G (such that G < P): ");
int g = sc.nextInt();

int yA = (int) ((Math.pow(g, a)) % p);
int yB = (int) ((Math.pow(g, b)) % p);
int kA = (int) ((Math.pow(yB, a)) % p);
int kB = (int) ((Math.pow(yA, a)) % p);

if (kA == kB)
System.out.println("Keys matched!");
else
System.out.println("Keys didn't match!");}}
