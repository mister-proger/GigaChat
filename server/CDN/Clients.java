import org.java_websocket.WebSocket;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;

class Clients {
    private final ArrayList<Client> clients = new ArrayList<>();

    public void addClient (WebSocket sock, int id, String token, int channel) {

    }

    public void sendCommandToChannel (int channel, Message data) {
        clients.parallelStream()
                .filter(c -> c.getChannel() == channel)
                .forEach(c -> c.send(data));
    }

    public void addClient (Client client) {

    }
}
