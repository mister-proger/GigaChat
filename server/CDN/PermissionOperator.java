import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class PermissionOperator extends DBOperator {

    public static boolean validateToken (String _id, String token) {
        int id = Integer.parseInt(_id);

        String sql = "SELECT COUNT(*) FROM tokens WHERE id = ? AND token = ?";
        PreparedStatement stmt;
        try {
            stmt = conn.prepareStatement(sql);
            stmt.setInt(1, id);
            stmt.setString(2, Helper.hasher(token));
            System.out.println(Helper.hasher(token));
            ResultSet rs = stmt.executeQuery();
            rs.next();
            int count = rs.getInt(1);
            return count > 0;
        } catch (SQLException e) {
            return false;
        }
    }
}
