import { Elysia, t } from 'elysia';
import { db } from '../db';

const messageRoutes = new Elysia({ prefix: '/messages' })

  .post('/:id', async ({ params, set, body }) => {
    const conversationId = params.id;
    const now = new Date();

    const userMessage = await db
      .insertInto('message')
      .values({
        id: crypto.randomUUID(),
        conversation_id: conversationId,
        sent_by_user: true,
        content: body.question,
        created_at: now,
        updated_at: now,
      })
      .returningAll()
      .executeTakeFirst();

    try {
      const response = await fetch('http://localhost:8000/financial/ask/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      });

      set.status = response.status;
      const res = await response.json();

      const isError = res.data.answer.isError;

      if (isError) {
        // Still store the failure as an assistant message if needed
        return { message: 'LLM failed to respond.' };
      }

      const resMsg = res.data.answer.content[0].text;

      // 3. Store assistant response
      const assistantMessage = await db
        .insertInto('message')
        .values({
          id: crypto.randomUUID(),
          conversation_id: conversationId,
          sent_by_user: false,
          content: resMsg,
          created_at: new Date(),
          updated_at: new Date(),
        })
        .returningAll()
        .executeTakeFirst();

      return { message: resMsg };

    } catch (error: any) {
      set.status = 503;
      return {
        message: 'MCP service is unavailable.',
        details: error.message,
      };
    }

  }, {
    body: t.Object({ question: t.String() }),
  });

export default messageRoutes;
