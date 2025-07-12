import { Elysia, t } from "elysia";
import { db } from "../db"; // adjust path if needed
import { randomUUID } from "crypto";

const messageRoutes = new Elysia({ prefix: "/messages" })
  .post(
    "/:id",
    async ({ params, set, body }) => {
      const { id: conversationId } = params;
      const { question } = body;
      const now = new Date();

      try {
        // Store user message in DB
        await db
          .insertInto("message")
          .values({
            id: randomUUID(),
            conversation_id: conversationId,
            sent_by_user: true,
            content: question,
            created_at: now,
            updated_at: now,
          })
          .execute();

        // Call MCP service
        const response = await fetch("http://localhost:8000/financial/ask/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(body),
        });

        set.status = response.status;

        const res = await response.json();
        const isError = res.data.answer.isError;
        const resMsg = res.data.answer.content[0].text;

        // Store assistant message in DB
        await db
          .insertInto("message")
          .values({
            id: randomUUID(),
            conversation_id: conversationId,
            sent_by_user: false,
            content: resMsg,
            created_at: new Date(),
            updated_at: new Date(),
          })
          .execute();

        if (isError) {
          return {
            message: "There was an error processing your request.",
            details: resMsg,
          };
        }

        return { message: resMsg };
      } catch (error: any) {
        set.status = 503;
        return {
          message: "MCP service is unavailable.",
          details: error.message,
        };
      }
    },
    {
      body: t.Object({ question: t.String() }),
    }
  );

export default messageRoutes;
