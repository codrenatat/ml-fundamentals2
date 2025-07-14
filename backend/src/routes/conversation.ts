import { Elysia, t } from 'elysia';
import { db } from '../db';

// Define the route /chats
const chatRoutes = new Elysia({ prefix: '/chats' })

  // Get all conversations
  .get('/', async () => {
    return await db
      .selectFrom('conversation')
      .selectAll()
      .orderBy('updated_at', 'desc')
      .execute();
  })

  // Get a specific conversation and it's messages depending on its id
  .get('/:id', async ({ params, set }) => {
  const chat = await db
    .selectFrom('conversation')
    .selectAll()
    .where('id', '=', params.id)
    .executeTakeFirst();

  if (!chat) {
    set.status = 404;
    return { error: 'Chat not found' };
  }

  const messages = await db
    .selectFrom('message')
    .selectAll()
    .where('conversation_id', '=', params.id)
    .orderBy('created_at', 'asc')
    .execute();

  return {
    chat,
    messages,
  };
  })

  // Delete a chat and its messages
  .delete('/:id', async ({ params }) => {
  // Primero eliminamos los mensajes relacionados
    await db
      .deleteFrom('message')
      .where('conversation_id', '=', params.id)
      .execute();

    // Luego eliminamos la conversación
    await db
      .deleteFrom('conversation')
      .where('id', '=', params.id)
      .execute();

    return { success: true };
  })

  // Create a new conversation
  .post('/', async ({ body }) => {
    const now = new Date();
    const newChat = await db
      .insertInto('conversation')
      .values({
        id: crypto.randomUUID(),
        title: body.title ?? null,
        created_at: now,
        updated_at: now,
      })
      .returningAll()
      .executeTakeFirst();

    return newChat;
  }, {
    body: t.Object({
      title: t.Optional(t.String()),
    }),
  });

export default chatRoutes;


