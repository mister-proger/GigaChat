import java.sql.Array;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.List;

public class HistoryOperator extends DBOperator {

    public static void writeMessage (int senderId, int channelId, String textData, byte[] binaryData, List<Integer> files) throws SQLException {
        PreparedStatement stmt = conn.prepareStatement("INSERT INTO messages (sender, channel, t_data, b_data, files) VALUES (?, ?, ?, ?, ?)");

        stmt.setInt(1, senderId);
        stmt.setInt(2, channelId);
        stmt.setString(3, textData);
        stmt.setBytes(4, binaryData);

        if (files != null && !files.isEmpty()) {
            Array array = conn.createArrayOf("integer", files.toArray());
            stmt.setArray(5, array);
        } else {
            stmt.setArray(5, null);
        }

        stmt.executeUpdate();
        stmt.close();
    }

    public static List<HashMap<String, String>> loadHistory (int channel) {
        return null;
    }
}
