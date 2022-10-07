import java.util.Scanner;

// Sten Soomre //
class KT5 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int i = 1;
        System.out.println("A  -  Jadamisi\nB  -  Rööbiti");
        String valik = scanner.nextLine();
        if("B".equals(valik)){
            System.out.print("Mitu takistit? ");
            Integer number = scanner.nextInt();
            int R1 = 0;
            for (;i <= number;){
                System.out.print("Mitu oomi? ");
                Integer Rn = scanner.nextInt();
                R1 = R1 + Rn;
                i++;
                }
            float R = 10000f/R1;
            System.out.println(R+" oomi");
        }
        if("A".equals(valik)){ 
            System.out.print("Mitu takistit? ");
            Integer number = scanner.nextInt();
            int R = 0;
            for (;i <= number;){
                System.out.print("Mitu oomi? ");
                Integer Rn = scanner.nextInt();
                R = R + Rn;
                i++;
            }
            System.out.println(R+" oomi");
        }
    }
}
