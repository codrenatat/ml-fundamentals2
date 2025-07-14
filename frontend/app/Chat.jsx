function Chat({ input, setInput, messages, setMessages, conversationId }) {
  const messagesEndRef = React.useRef(null);

  React.useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!input.trim()) return;
    if (!conversationId) {
      alert("Selecciona una conversación o guarda una nueva primero.");
      return;
    }

    const userMsg = { role: "user", content: input };
    setMessages(prev => [...prev, userMsg]);

    axios.post(`http://localhost:3333/messages/${conversationId}`, {
      question: input
    })
      .then(res => {
        const assistantMsg = {
          role: "assistant",
          content: res.data.message
        };
        setMessages(prev => [...prev, assistantMsg]);
      })
      .catch(err => {
        console.error("❌ Error al enviar mensaje:", err.response?.data || err.message);
        setMessages(prev => [...prev, {
          role: "system",
          content: "❌ Error al enviar mensaje: " + (err.response?.data?.message || err.message)
        }]);
      });

    setInput("");
  };

  return (
    <div className="chat-container">
      <div className="chat-header">AlphaVantage MCP Chat</div>

      <div className="chat-main">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={
              "message " +
              (msg.role === "user"
                ? "user"
                : msg.role === "assistant"
                ? "assistant"
                : "system")
            }
          >
            {msg.content}
          </div>
        ))}
        <div ref={messagesEndRef}></div>
      </div>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Escribe un mensaje..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button type="submit">Enviar</button>
      </form>
    </div>
  );
}
