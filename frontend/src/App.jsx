import React from 'react';
import Sidebar from './Sidebar.jsx';
import Chat from './Chat.jsx';
import axios from 'axios';

export default function App() {
  const [input, setInput] = React.useState("");
  const [messages, setMessages] = React.useState([]);
  const [conversations, setConversations] = React.useState([]);
  const [selectedId, setSelectedId] = React.useState(null);

  React.useEffect(() => {
    axios.get("http://localhost:3333/chats")
      .then(res => {
        setConversations(res.data);
        if (res.data.length > 0) {
          const first = res.data[0];
          setSelectedId(first.id);
          axios.get(`http://localhost:3333/messages/${first.id}`)
            .then(r => setMessages(r.data.messages));
        }
      })
      .catch(err => {
        console.error("Error getting conversations", err);
      });
  }, []);

  const saveConversation = () => {
    const title = `Chat ${conversations.length + 1}`;
    const payload = { title, messages };

    axios.post("http://localhost:3333/chats", payload)
      .then(res => {
        setConversations(prev => [res.data, ...prev]);
        setSelectedId(res.data.id);
      })
      .catch(err => console.error("Error saving convo:", err));
  };

  const loadConversation = (conv) => {
    setSelectedId(conv.id);
    axios.get(`http://localhost:3333/chats/${conv.id}`)
      .then(res => {
        if (res.data && Array.isArray(res.data.messages)) {
          setMessages(res.data.messages);
        } else {
          setMessages([]);
        }
      })
      .catch(err => {
        console.error("Error", err.response?.data || err.message);
        setMessages([{ role: "system", content: "Error getting convo." }]);
      });
  };

  const startNewChat = () => {
    const title = prompt("New chat title:");
    if (!title || title.trim() === "") return;

    axios.post("http://localhost:3333/chats", { title })
      .then(res => {
        const newChat = res.data;
        setConversations(prev => [newChat, ...prev]);
        setSelectedId(newChat.id);
        setMessages([]);
      })
      .catch(err => {
        console.error("Error:", err);
        alert("Couldn't get convo");
      });
  };

  const deleteConversation = (indexToDelete) => {
    const conv = conversations[indexToDelete];
    axios.delete(`http://localhost:3333/chats/${conv.id}`)
      .then(() => {
        setConversations(prev =>
          prev.filter((_, index) => index !== indexToDelete)
        );
        if (selectedId === conv.id) {
          setMessages([]);
          setSelectedId(null);
        }
      })
      .catch(err => {
        const msg = err.response?.data?.error || err.message;
        console.error("Error msj:", msg);
        setMessages([{ role: "system", content: "Couldn't charge convo" }]);
      });
  };

  return (
    <>
      <Sidebar
        conversations={conversations}
        onSave={saveConversation}
        onNew={startNewChat}
        onLoad={loadConversation}
        onDelete={deleteConversation}
      />
      <Chat
        input={input}
        setInput={setInput}
        messages={messages}
        setMessages={setMessages}
        conversationId={selectedId}
      />
    </>
  );
}
