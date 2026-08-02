import 'package:flutter/material.dart';
import 'widgets/ticket_list.dart';
import 'widgets/chat_window.dart';

void main() {
  runApp(HackathonDashboard());
}

class HackathonDashboard extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Romchi AI Support Dashboard',
      home: Scaffold(
        appBar: AppBar(title: Text('Romchi AI Support Dashboard')),
        body: Row(
          children: [
            Expanded(flex: 2, child: TicketList()),
            Expanded(flex: 3, child: ChatWindow()),
          ],
        ),
      ),
    );
  }
}
