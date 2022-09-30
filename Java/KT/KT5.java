import java.util.Scanner;

// Sten Soomre //
class KT5 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Valige 1, et leida rööpselt ühendatud takiste kogutakistus - ");
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
                System.out.print("Takistuse oom: ");
                arv1 = scanner.next();
                System.out.print("Takistuse oom: ");
                arv2 = scanner.next();
                System.out.print("Takistuse oom: ");
                arv3 = scanner.next();
                System.out.print("Takistuse oom: ");
                arv4 = scanner.next();
                System.out.print("Takistuse oom: ");
                arv5 = scanner.next();
                System.out.print("Takistuse oom: ");
                arv6 = scanner.next();
                s = jes(arv1, arv2, arv3, arv4, arv5, arv6);
                System.out.print("Kogutakistus on " + s + " oomi");
                break;
        }

    }

    public static double jes(String a, String b, String c, String d, String e, String f) {
        float arv1 = Float.parseFloat(a);
        float arv2 = Float.parseFloat(b);
        float arv3 = Float.parseFloat(c);
        float arv4 = Float.parseFloat(d);
        float arv5 = Float.parseFloat(e);
        float arv6 = Float.parseFloat(f);
        double s = (arv1 + arv2 + arv3 + arv4) + (arv5 * arv6 / (arv5 + arv6));
        return s;
    }
}