package springBootcamp.quiz4;

import springBootcamp.QuizProject.Main;

public class Twenty {
    int a = 5;

    A obj = () -> {

        System.out.println(this.a);
    };

    public static void main(String[] args) {
        Twenty ob = new Twenty();

        ob.obj.run(); // 5
    }
}

interface A {

    public void run();

}
