package springBootcamp.quiz2;

public class Ten {
    public static void main(String[] args) {
        int i, j;

        i = 100;

        j = 300;

        while (++i < --j)
            ;

        System.out.println(i);
    }
}