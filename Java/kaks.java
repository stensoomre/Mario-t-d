// Sten Soomre IT-21 //

class kaks {
	public static final double PI = 3.14;

	public static void main(String[] args) {

		tollidmeetriteks(2);
		ellipspindala(2, 8);
		minutidtundideks(100);
		sportkiirus(400, 5, 1152, 2);

	}

	static void tollidmeetriteks(int tollid) {
		double meetrid;
		meetrid = tollid * 0.0254;
		System.out.println("Sinu vastuseks on: " + meetrid + "m");
		System.out.println();
	}

	static void ellipspindala(int a, int b) {
		double pind = PI * a * b;
		double pindala = Math.round(pind * 100.00) / 100.00;
		System.out.println("Ellipsi pindala on: " + pindala + " ruutmeetrit");
	}

	static void minutidtundideks(int min) {
		int tund, kokku, minut;
		tund = min / 60;
		kokku = tund * 60;
		minut = min - kokku;
		System.out.println("Ajaks on: " + tund + " tund ja " + minut + " minutit.");
		System.out.println();
	}

	static void sportkiirus(int km, int h, int km1, int h1) {
		double kiir1 = km / h;
		double kiirus1 = Math.round(kiir1 * 100.00) / 100.00;

		double kiir2 = km1 / h1;
		double kiirus2 = Math.round(kiir2 * 100.00) / 100.00;

		double vahe = kiirus2 - kiirus1;

		System.out.println("Kahe sportlase kiiruse vahe on " + Math.abs(vahe));
	}

}
