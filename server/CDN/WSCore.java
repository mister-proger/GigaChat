import com.jsoniter.JsonIterator;
import com.jsoniter.output.JsonStream;
import org.java_websocket.WebSocket;
import org.java_websocket.handshake.ClientHandshake;
import org.java_websocket.server.WebSocketServer;

import java.net.InetSocketAddress;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;


class WSCore extends WebSocketServer {
    private final HistoryOperator historyOperator = new HistoryOperator();
    private final PermissionOperator permissionOperator = new PermissionOperator();
    private final Clients clients = new Clients();

    public WSCore (int port) {
        super(new InetSocketAddress(port));
    }

    @Override
    public void onOpen (WebSocket webSocket, ClientHandshake clientHandshake) {
        Helper.ConnectionPath connectParams = Helper.parse(clientHandshake.getResourceDescriptor());

        if (connectParams.params.get("id") != null && connectParams.params.get("token") != null) {
            if (!(PermissionOperator.validateToken(connectParams.params.get("id"), connectParams.params.get("token")))) {
                webSocket.close(401, "InvalidAuthorizationData");
            } else {
                clients.addClient(new Client(webSocket, Integer.parseInt(connectParams.params.get("id")), connectParams.params.get("token")));
            }
        } else {
            webSocket.close(406, "InsufficientData");
        }
        System.out.println(JsonStream.serialize(connectParams));
    }

    @Override
    public void onClose (WebSocket webSocket, int i, String reason, boolean b) {
        System.out.println("Client was disconnect!");
    }

    @Override
    public void onMessage (WebSocket webSocket, String s) {
        System.out.println(s);
        HashMap message = JsonIterator.deserialize(s, HashMap.class);
        System.out.println(message);
        System.out.println(PermissionOperator.validateToken(message.get("id").toString(), message.get("token").toString()));
    }

    @Override
    public void onError (WebSocket webSocket, Exception e) {
        
    }

    @Override
    public void onStart () {
        System.out.println("Server started on port 8080");
    }

    public static void main (String[] args) {
        int port = 8080;
        WSCore server = new WSCore(port);
        server.start();
    }
}