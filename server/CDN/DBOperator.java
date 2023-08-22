import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public abstract class DBOperator {
    static String url = "jdbc:postgresql://localhost:5432/";
    static String user = "postgres";
    static String password = "pRN|$jZAKC@XefDBaTxdkQoOWi5VuvbFl~m*U1H0tRsa*oeUDypN@Z#4~xGg@O@F";

    static Connection conn;
    static {
        try {
            conn = DriverManager.getConnection(url, user, password);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}

