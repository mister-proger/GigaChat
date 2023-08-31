import at.favre.lib.crypto.bcrypt.BCrypt;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Arrays;

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

            return Helper.verifier(user_token, rs.getString(1).getBytes());
        } catch (SQLException e) {
            System.out.println(e.getMessage());
            return false;
        }
    }
}
