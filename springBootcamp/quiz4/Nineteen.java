package springBootcamp.quiz4;

interface MyCode {

    double myScore();

}

public class Nineteen {
    public static void main(String[] args) {
        MyCode myScore;

        myCode = () -> 87;

        System.out.println(MyCode.myScore()); // compile time error
    }
}
