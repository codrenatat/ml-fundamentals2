import { Elysia, t } from 'elysia';
import { db } from '../db';

const chatRoutes = new Elysia({ prefix: '/chats' })

  // Get all chats
  .get('/', async () => {
    return await db
      .selectFrom('conversation')
      .selectAll()
      .orderBy('updated_at', 'desc')
      .execute();
  })

  // Get a single chat and its messages
  .get('/:id', async ({ params }) => {
    const chat = await db
      .selectFrom('conversation')
      .selectAll()
      .where('id', '=', params.id)
      .executeTakeFirst();

    if (!chat) return { error: 'Chat not found' };

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

  // Create a new chat
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


