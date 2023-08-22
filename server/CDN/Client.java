import com.jsoniter.output.JsonStream;
import org.java_websocket.WebSocket;

public class Client {
    private final WebSocket sock;
    private final int id;
    private final String token;
    private int channel;

    public Client (WebSocket sock, int id, String token) {
        this.sock = sock;
        this.id = id;
        this.token = token;
    }

    public void moveTo (int channel) {
        this.channel = channel;
    }

    public void send (Message data) {
        sock.send(JsonStream.serialize(data));
    }

    public void close (int code, String reason) {
        sock.close(code, reason);
    }

    public Integer getChannel () {
        return channel;
    }
}
