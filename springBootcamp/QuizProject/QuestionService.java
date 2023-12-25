package springBootcamp.QuizProject;

import java.util.*;

public class QuestionService {
    Question[] questions = new Question[5];
    String[] selection = new String[5];

    public QuestionService() {
        questions[0] = new Question(1, "What is size of int", "2", "4", "6", "8", "2");
        questions[1] = new Question(2, "Whatis size of double", "2", "4", "6", "8", "4");
        questions[2] = new Question(3, "What is size of char", "2", "4", "6", "8", "2");
        questions[3] = new Question(4, "What is size of float", "2", "4", "6", "8", "4");
        questions[4] = new Question(5, "What is size of boolean", "1", "4", "6", "8", "1");

    }

    public void playQuiz() {
        int i = 0;
        for (Question q : questions) {

            System.out.println("Question no." + q.getId());
            System.out.println(q.getQuestion());
            System.out.println(q.getOpt1());
            System.out.println(q.getOpt2());
            System.out.println(q.getOpt3());
            System.out.println(q.getOpt4());

            Scanner sc = new Scanner(System.in);
            selection[i++] = sc.nextLine();

        }
        for (String s : selection) {
            System.out.println(s);
        }
    }

    public void printScore() {
        int score = 0;

        for (int i = 0; i < questions.length; i++) {
            String Rightans = questions[i].getAnswer();

            String userAns = selection[i];
            if (Rightans.equals(userAns)) {
                score++;
            }
        }
        System.out.println("Total score is :" + score);
    }
}
