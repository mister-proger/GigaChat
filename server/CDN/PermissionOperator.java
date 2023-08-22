import java.sql.PreparedStatement;
import java.sql.SQLException;

public class PermissionOperator extends DBOperator {

    public static boolean validateToken (String _id, String token) {
        int id = Integer.parseInt(_id);
        return true;
    }
}
