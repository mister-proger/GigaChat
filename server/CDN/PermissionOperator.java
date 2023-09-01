import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class PermissionOperator extends DBOperator {

    public static boolean validateToken (int id, String user_token) {
        String sql = """
            SELECT token
            FROM tokens
            WHERE account_id = ?
        """;
        PreparedStatement stmt;

        try {
            stmt = conn.prepareStatement(sql);
            stmt.setInt(1, id);

            ResultSet rs = stmt.executeQuery();
            rs.next();

            String token = rs.getString(1);
            return Helper.verifier(user_token, token.getBytes());
        } catch (SQLException e) {
            return false;
        }
    }
}
