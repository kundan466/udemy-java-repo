package springBootcamp.quiz4;

public class Eleven {
    public static void main(String[] args) {
        char chars[] = { 'a', 'b', 'c', 'd', 'e', 'f' };

        String str = new String(chars, 1, 3);

        System.out.println(str); // bcd
    }
}
