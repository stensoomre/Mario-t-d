import java.util.Scanner;

// Sten Soomre //
class KT13 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Sisestage täisarv: ");
        int rows = scanner.nextInt();
        System.out.println("Kolmnurk: ");

        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        scanner.close();
    }
}