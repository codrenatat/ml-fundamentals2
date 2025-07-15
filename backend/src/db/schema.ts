// Conversation table
export interface ConversationTable {
  id: string;
  title: string | null;
  created_at: Date;
  updated_at: Date;
}

// Message table
export interface MessageTable {
  id: string;
  conversation_id: string;
  sent_by_user: boolean;
  content: string;
  created_at: Date;
  updated_at: Date;
}

// Maps tables for interfaces
export interface DB {
  conversation: ConversationTable;
  message: MessageTable;
}
