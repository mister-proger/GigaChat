import com.jsoniter.output.JsonStream;
import org.java_websocket.WebSocket;

import java.util.ArrayList;

class Clients {
    private final ArrayList<Client> clients = new ArrayList<>();

    public void addClient (WebSocket sock, int id, String token, int channel) {

    }

    public void sendCommandToChannel (int channel, Message data) {
        String message = JsonStream.serialize(data);

        clients.parallelStream()
                .filter(c -> c.getChannel() == channel)
                .forEach(c -> c.send(message));
    }

    public void addClient (Client client) {

    }
}
