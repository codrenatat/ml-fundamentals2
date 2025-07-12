function App() {
  const [input, setInput] = React.useState("");
  const [messages, setMessages] = React.useState([]);
  const [conversations, setConversations] = React.useState([]);
  const saveConversation = () => {
    const title = `Chat ${conversations.length + 1}`;
    setConversations(prev => [...prev, { title, messages }]);
  };

  const loadConversation = (conv) => {
    setMessages(conv.messages);
  };

  const startNewChat = () => {
    setMessages([]);
    };

  const deleteConversation = (indexToDelete) => {
    setConversations(prev =>
      prev.filter((_, index) => index !== indexToDelete)
    );
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
      />
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
