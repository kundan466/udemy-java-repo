package springBootcamp.quiz2;

public class Seven {
    public static void main(String[] args) {
        int x = 5;

        int y = 10;

        int z = (x++ > 5 && y-- < 10) ? x-- : y;
        System.out.println(x); // 6
        System.out.println(y); // 10
    }
}
