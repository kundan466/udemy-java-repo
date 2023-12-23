package springBootcamp.quiz3;

public class Five {
    public static void main(String[] args) {
        Message ob = new Message();

        ob.printMessage(5); // Message primitive: 5
    }
}

class Message {

    public void printMessage(int message) {

        System.out.println("Message primitive: " + message);

    }

    public void printMessage(Integer message) {

        System.out.println("Message object: " + message);

    }

}
