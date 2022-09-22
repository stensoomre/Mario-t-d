// Sten Soomre IT-21 //

import java.util.Scanner;

class viis {

	public static void main(String[] args) {
		jaga();
	}

	public static void jaga() {
		int kordus = 0;

		while (kordus < 3) {
			Scanner scanner = new Scanner(System.in);
			System.out.print("Sisesta 1. arv: ");
			int arv1 = scanner.nextInt();
			System.out.print("Sisesta 2. arv: ");
			int arv2 = scanner.nextInt();

			if (arv1 >= 0 && arv2 > 0) {
				double tehe = arv1 / arv2;
				System.out.println("Vaste: " + tehe);
				kordus++;
			} else {
				System.out.println("Midagi on valesti ):");
			}
		}

	}
}
