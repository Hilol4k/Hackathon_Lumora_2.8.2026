import 'package:flutter/material.dart';
import '../services/api_service.dart';

class ChatWindow extends StatefulWidget {
  @override
  _ChatWindowState createState() => _ChatWindowState();
}

class _ChatWindowState extends State<ChatWindow> {
  final TextEditingController _controller = TextEditingController();
  List<String> messages = ["User: Hello", "AI: Needs human support"];

  void _sendMessage() async {
    String text = _controller.text;
    if (text.isNotEmpty) {
      setState(() {
        messages.add("You: $text");
      });
      await ApiService.sendMessage(text); // отправка в Flask API
      _controller.clear();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Expanded(
          child: Container(
            color: Colors.grey[200],
            child: ListView.builder(
              itemCount: messages.length,
              itemBuilder: (context, index) {
                return ListTile(title: Text(messages[index]));
              },
            ),
          ),
        ),
        Row(
          children: [
            Expanded(child: TextField(controller: _controller)),
            ElevatedButton(
              onPressed: _sendMessage,
              child: Text('Send to Telegram'),
            ),
          ],
        ),
      ],
    );
  }
}
