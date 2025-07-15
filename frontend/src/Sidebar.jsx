import React from 'react';
import axios from 'axios';

function Sidebar({ conversations, onSave, onNew, onLoad, onDelete }) {
  const handleDelete = (convId, index) => {
    if (confirm("Are you sure you want to delete this chat?")) {
      axios.delete(`http://localhost:3333/chats/${convId}`)
        .then(() => {
          onDelete(index);
        })
        .catch(err => {
          console.error("Error:", err);
          alert("Couldn[t delete convo");
        });
    }
  };

  return (
    <div className="sidebar">
      <button onClick={onNew} style={{ marginTop: "0.5rem" }}>New Chat</button>

      {conversations.map((c, i) => (
        <div key={i} className="conversation">
          <span onClick={() => onLoad(c)} style={{ flexGrow: 1, cursor: "pointer" }}>
            {c.title || "Unnamed"}
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

export default Sidebar; 

