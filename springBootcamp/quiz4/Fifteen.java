package springBootcamp.quiz4;

public class Fifteen {
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer("Java Code");

        System.out.println(sb.capacity()); // 25

        sb.trimToSize();

        System.out.println(sb.capacity()); // 9
    }
}
