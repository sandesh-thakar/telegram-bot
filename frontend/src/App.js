import React, { useState, useEffect } from "react";
import "./App.css";

const MessageList = () => {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8000/messages/");

    socket.onmessage = (event) => {
      const messages = JSON.parse(event.data);
      setMessages(messages);
    };

    socket.onclose = (event) => {
      console.error("WebSocket closed:", event);
    };

    return () => {
      socket.close();
    };
  }, []);

  return (
    <div className="message-list">
      <h2>Message List</h2>
      <table className="message-table">
        <thead>
          <tr>
            <th>Sender</th>
            <th>Message</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {messages.map((message) => (
            <tr key={message.id}>
              <td>{message.sender}</td>
              <td>{message.content}</td>
              <td>{message.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

function App() {
  return (
    <div className="App">
      <MessageList />
    </div>
  );
}

export default App;
