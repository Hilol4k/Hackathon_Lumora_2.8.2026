import 'package:flutter/material.dart';

class TicketList extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text('Escalated Tickets', style: TextStyle(fontSize: 20)),
        Expanded(
          child: ListView.builder(
            itemCount: 5, // пока mock‑данные
            itemBuilder: (context, index) {
              return ListTile(
                title: Text('Ticket #$index'),
                trailing: ElevatedButton(
                  onPressed: () {
                    // Claim Ticket логика
                  },
                  child: Text('Claim'),
                ),
              );
            },
          ),
        ),
      ],
    );
  }
}
