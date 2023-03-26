import java.net.*; // Сокеты для подключения
import java.util.*; // Многопоток для нескольких клиентов
import java.io.*; // IO Exception
import java.text.*; // Для получения текущего времени и даты
import org.json.*; // Для пересылки JSON объектов

public class Server {
   public static final String HOST = "65.108.21.143";
   public static final int PORT = 25872;
   public static HashMap<String,Socket> clients = new HashMap<String,Socket>();
   public static ServerSocket s;

   public static void main(String[] args) {
      try {
         s = new ServerSocket(PORT);
         System.out.println("Сервер запущен на адресе " + HOST + ":" + PORT);
         while (true) {
            Socket connection = s.accept(); // ждем подключения
            Thread client_thread = new Thread(new Runnable() {
               public void run() {
                  try {
                     handle_client(connection); // обработка подключения клиента
                  } catch (IOException e) {
                     e.printStackTrace();
                  }
               }
            });
            client_thread.start();
         }
      } catch (IOException e) {
         e.printStackTrace();
      }
   }

   public static void handle_client(Socket connection) throws IOException {
      String mask = (new BufferedReader(new InputStreamReader(connection.getInputStream()))).readLine().toString();
      if (clients.containsKey(mask) || mask.equals("server") || mask.contains(" ") || mask.equals("all")) {
         JSONObject error_obj = new JSONObject()
            .put("sender", "server")
            .put("text", "Данный никнейм занят или содержит запрещённые символы или слова")
            .put("recipient", "You");
         sendMessage(connection, error_obj.toString());
         return;
      }
      System.out.println("<" + (new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")).format(new Date()) + "> " + mask + " подключился");
      clients.put(mask, connection);
      JSONObject join_obj = new JSONObject()
         .put("sender", "server")
         .put("text", mask + " подключился")
         .put("recipient", "all");
      sendMessageToAll(join_obj.toString());
      while (clients.containsKey(mask)) {
         JSONObject message_obj = new JSONObject()
            .put("sender", mask)
            .put("text", (new BufferedReader(new InputStreamReader(connection.getInputStream()))).readLine().toString())
            .put("recipient", "all");
         if (message_obj.get("recipient").equals("all")) {
            System.out.println("<" + (new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")).format(new Date()) + "> " + message_obj.getString("sender") + ": " + message_obj.getString("text"));
            sendMessageToAll(message_obj.toString());
         } else {
            System.out.println("<" + (new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")).format(new Date()) + "> " + message_obj.getString("sender") + " -> " + message_obj.getString("recipient") + ": " + message_obj.getString("text"));
            sendMessage(clients.get(message_obj.getString("recipient")), message_obj.toString());
            JSONObject reply_obj = new JSONObject()
               .put("sender", "You")
               .put("recipient", message_obj.getString("recipient"))
               .put("text", message_obj.getString("text"));
            sendMessage(connection, reply_obj.toString());
         }
      }
      System.out.println("<" + (new SimpleDateFormat("HH:mm:ss")).format(new Date()) + "> " + mask + " отключился");
      clients.remove(mask);
      JSONObject leave_obj = new JSONObject()
         .put("sender", "server")
         .put("text", mask + " отключился")
         .put("recipient", "all");
      sendMessageToAll(leave_obj.toString());
   }

   public static void sendMessage(Socket connection, String message) {
      try {
         PrintWriter writer = new PrintWriter(connection.getOutputStream(), true);
         writer.println(message);
      } catch (IOException e) {
         e.printStackTrace();
      }
   }

   public static void sendMessageToAll(String message) {
      for (String key : clients.keySet()) {
         sendMessage(clients.get(key), message);
      }
   }
}