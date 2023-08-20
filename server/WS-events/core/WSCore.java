import com.jsoniter.JsonIterator;
import com.jsoniter.any.Any;
import com.jsoniter.output.JsonStream;
import org.java_websocket.WebSocket;
import org.java_websocket.handshake.ClientHandshake;
import org.java_websocket.server.WebSocketServer;

import java.net.InetSocketAddress;
import java.util.HashMap;
import java.util.Map;


class WSCore extends WebSocketServer {
    private HashMap<String, DBOperator> operators;

    public WSCore (int port) {
        super(new InetSocketAddress(port));
    }

    @Override
    public void onOpen (WebSocket webSocket, ClientHandshake clientHandshake) {

    }

    @Override
    public void onClose (WebSocket webSocket, int i, String s, boolean b) {

    }

    @Override
    public void onMessage (WebSocket webSocket, String s) {

    }

    @Override
    public void onError (WebSocket webSocket, Exception e) {

    }

    @Override
    public void onStart () {
        operators = new HashMap<>();

        operators.put("History", new HistoryOperator());
    }

    public static void main (String[] args) {
        int port = 8080;
        WSCore server = new WSCore(port);
        server.start();
        System.out.println("Server started on port " + port);
    }
}