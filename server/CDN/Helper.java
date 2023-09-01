import at.favre.lib.crypto.bcrypt.BCrypt;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Helper {
    protected static class ConnectionPath {
        String[] pathParts;
        Map<String, String> params;

        public ConnectionPath (String[] pathParts, Map<String, String> params) {
            this.pathParts = pathParts;
            this.params = params;
        }
    }
    public static ConnectionPath parseURI (String uri) {
        int index = uri.indexOf('?');
        String path = uri.substring(0, index);
        String query = uri.substring(index + 1);

        String[] pathParts = path.split("/");

        Map<String, String> params = new HashMap<>();
        for (String param : query.split("&")) {
            String[] entry = param.split("=");
            params.put(entry[0], entry[1]);
        }

        return new ConnectionPath(pathParts, params);
    }

    public static Boolean verifier (String data, byte[] hash_data) {
        return BCrypt.verifyer().verify(Arrays.copyOfRange(data.toCharArray(), 0, Math.min(data.toCharArray().length, 72)), hash_data).verified;
    }
}
