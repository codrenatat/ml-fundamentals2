function App() {
  const [input, setInput] = React.useState("");
  const [messages, setMessages] = React.useState([]);
  const [conversations, setConversations] = React.useState([]);
  const [selectedId, setSelectedId] = React.useState(null);

  // 🚀 Cargar conversaciones al montar
  React.useEffect(() => {
    axios.get("http://localhost:3333/chats")
      .then(res => {
        setConversations(res.data);
        if (res.data.length > 0) {
          const first = res.data[0];
          setSelectedId(first.id);
          axios.get(`http://localhost:3333/messages/${first.id}`)
            .then(r => setMessages(r.data));
        }
      })
      .catch(err => {
        console.error("Error cargando conversaciones:", err);
      });
  }, []);

  const saveConversation = () => {
    const title = `Chat ${conversations.length + 1}`;
    const payload = { title, messages };

    axios.post("http://localhost:3333/chats", payload)
      .then(res => {
        setConversations(prev => [res.data, ...prev]); // se añade al inicio
        setSelectedId(res.data.id);
      })
      .catch(err => console.error("Error guardando conversación:", err));
  };

  const loadConversation = (conv) => {
  console.log("📥 Cargando chat:", conv.id);
  setSelectedId(conv.id);

  axios.get(`http://localhost:3333/chats/${conv.id}`)
    .then(res => {
      if (res.data && Array.isArray(res.data.messages)) {
        console.log("✅ Mensajes del chat:", res.data.messages);
        setMessages(res.data.messages);
      } else {
        console.warn("⚠️ La respuesta no contiene mensajes.");
        setMessages([]);
      }
    })
    
    .catch(err => {
      console.error("❌ Error al cargar mensajes:", err.response?.data || err.message);
      setMessages([{ role: "system", content: "❌ No se pudo cargar esta conversación." }]);
    });
  };

  const startNewChat = () => {
  const title = prompt("Escribe el título del nuevo chat:");

  // Cancel or empty input? Do nothing
  if (!title || title.trim() === "") return;

  axios.post("http://localhost:3333/chats", { title })
    .then(res => {
      const newChat = res.data;
      setConversations(prev => [newChat, ...prev]);
      setSelectedId(newChat.id);
      setMessages([]);
    })
    .catch(err => {
      console.error("❌ Error creando nuevo chat:", err);
      alert("No se pudo crear una nueva conversación.");
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
        console.error("❌ Error cargando mensajes:", msg);
        setMessages([{ role: "system", content: "❌ No se pudo cargar esta conversación." }]);
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

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
