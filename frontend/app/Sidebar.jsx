function Sidebar({ conversations, onSave, onNew, onLoad, onDelete }) {
  const handleDelete = (convId, index) => {
    if (confirm("¿Estás segura de que deseas eliminar esta conversación?")) {
      axios.delete(`http://localhost:3333/chats/${convId}`)
        .then(() => {
          onDelete(index);
        })
        .catch(err => {
          console.error("❌ Error al eliminar la conversación:", err);
          alert("No se pudo eliminar la conversación.");
        });
    }
  };

  return (
    <div className="sidebar">
      <h2>Conversaciones</h2>
      <button onClick={onNew} style={{ marginTop: "0.5rem" }}>New Chat</button>

      {conversations.map((c, i) => (
        <div key={i} className="conversation">
          <span onClick={() => onLoad(c)} style={{ flexGrow: 1, cursor: "pointer" }}>
            {c.title || "Sin título"}
          </span>
          <button
            onClick={() => handleDelete(c.id, i)}
            style={{
              background: "transparent",
              color: "#9ca3af",
              border: "none",
              cursor: "pointer",
              fontWeight: "bold",
              marginLeft: "0.5rem"
            }}
            title="Eliminar"
          >
            🗑️
          </button>
        </div>
      ))}
    </div>
  );
}
