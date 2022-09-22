// Sten Soomre IT-21 //

import java.util.ArrayList;
import java.util.Scanner;
import java.util.stream.*;
import java.io.PrintWriter;
import java.io.*;

class kuus {

	public static void main(String[] args) {
		ArrayList<Integer> list = new ArrayList<Integer>();
		Scanner scanner = new Scanner(System.in);

		int kordus = 1;

		while (kordus == 1) {
			System.out.print("Sisesta arv: ");
			String arv = scanner.nextLine();

			if (arv == "") {
				break;
			}

			int number = Integer.parseInt(arv);
			list.add(number);
		}
		int kokku = list.size();
		int sum = list.stream().mapToInt(Integer::intValue).sum();
		int keskmine = sum / kokku;

		try {
			PrintWriter bw = new PrintWriter("numbrid.txt");
			bw.println("Kõik arvud: " + list);
			bw.println("Summa: " + sum);
			bw.println("Keskmine: " + keskmine);
			bw.close();
			System.out.println("Fail on loodud!");
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
