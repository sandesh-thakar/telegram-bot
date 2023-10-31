import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

const MessageList = () => {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const fetchMessages = async () => {
      try {
        const response = await axios.get("http://localhost:8000/messages/");
        console.log(response.data);
        setMessages(response.data);
      } catch (error) {
        console.error("Error fetching messages:", error);
      }
    };

    // Fetch messages on component mount
    fetchMessages();

    // Poll for new messages every 5 seconds
    const pollInterval = setInterval(fetchMessages, 5000);

    // Clean up the interval on component unmount
    return () => clearInterval(pollInterval);
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
