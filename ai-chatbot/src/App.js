import React, { useState } from "react";
import { Container, TextField, Button, Typography, Box } from "@mui/material";
import axios from "axios";

const API_URL = "http://localhost:8000/api/chatbot"; // Backend API URL

function App() {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]);

  const handleSend = async () => {
    if (!query.trim()) return;
    
    const userMessage = { sender: "User", text: query };
    setMessages([...messages, userMessage]);

    try {
      const response = await axios.post(API_URL, { query });
      const botMessage = { sender: "Chatbot", text: response.data.answer };
      setMessages([...messages, userMessage, botMessage]);
    } catch (error) {
      console.error("Error fetching chatbot response:", error);
    }

    setQuery("");
  };

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" align="center" gutterBottom>
        AI Chatbot 🤖
      </Typography>
      <Box sx={{ height: 300, overflowY: "auto", border: "1px solid #ccc", p: 2, mb: 2 }}>
        {messages.map((msg, index) => (
          <Typography key={index} align={msg.sender === "User" ? "right" : "left"}>
            <strong>{msg.sender}:</strong> {msg.text}
          </Typography>
        ))}
      </Box>
      <TextField
        fullWidth
        label="Type your query..."
        variant="outlined"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyPress={(e) => e.key === "Enter" && handleSend()}
      />
      <Button variant="contained" color="primary" fullWidth onClick={handleSend} sx={{ mt: 2 }}>
        Send
      </Button>
    </Container>
  );
}

export default App;
