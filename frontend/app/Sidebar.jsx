function Sidebar({ conversations, onSave, onNew, onLoad, onDelete }) {
  return (
    <div className="sidebar">
      <h2>Conversaciones</h2>
      <button onClick={onSave}>Guardar</button>
      <button onClick={onNew} style={{ marginTop: "0.5rem" }}>Nuevo Chat</button>
      {conversations.map((c, i) => (
        <div key={i} className="conversation">
          <span onClick={() => onLoad(c)} style={{ flexGrow: 1, cursor: "pointer" }}>
            {c.title}
          </span>
          <button
            onClick={() => onDelete(i)}
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
