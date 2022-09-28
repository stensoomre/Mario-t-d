import java.util.Scanner;

// Sten Soomre //
class KT5 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Vajuta Nr 1  ");
        String valik = scanner.next();
        String arv1;
        String arv2;
        String arv3;
        String arv4;
        String arv5;
        String arv6;

        double s;

        switch (Integer.parseInt(valik)) {
            case 1:
                System.out.print("Sisesta arv: ");
                arv1 = scanner.next();
                System.out.print("Sisesta arv: ");
                arv2 = scanner.next();
                System.out.print("Sisesta arv: ");
                arv3 = scanner.next();
                System.out.print("Sisesta arv: ");
                arv4 = scanner.next();
                System.out.print("Sisesta arv: ");
                arv5 = scanner.next();
                System.out.print("Sisesta arv: ");
                arv6 = scanner.next();
                s = KT5kooru.jes(arv1, arv2, arv3, arv4, arv5, arv6);
                System.out.print("Kogutakistus on " + s);
                break;
        }

    }
}