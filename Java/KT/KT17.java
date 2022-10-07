// Sten Soomre //
class KT17 {
    public static void main(String[] args) {
        
        int numbers[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
        for(int number : numbers){
            int i = 2;
            if (number % 2 == 0){
                System.out.print("Paarisrvud: ");
                while (i <= number) {
                    System.out.print(i + " ");
                    i = i + 2;
                }
                System.out.println("");
            }
        }
    }
}
