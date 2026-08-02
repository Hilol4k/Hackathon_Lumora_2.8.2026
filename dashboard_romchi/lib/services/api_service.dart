import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = "http://localhost:5000"; // Flask API Person 1

  static Future<void> sendMessage(String message) async {
    final response = await http.post(
      Uri.parse("$baseUrl/send_message"),
      body: {"text": message},
    );
    if (response.statusCode == 200) {
      print("Message sent successfully!");
    } else {
      print("Error sending message: ${response.statusCode}");
    }
  }
}
