public class Message {
    public Commands type;
    public int targetChannel;
    public String data;

    public int messageType () {
        return type.ordinal();
    }
}