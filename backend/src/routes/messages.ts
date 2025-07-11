import { Elysia, t } from "elysia";

const messageRoutes = new Elysia({ prefix: "/messages" })
    .post("/:id", async ({ params, set, body }) => {
        const { id } = params;  // Chat ID

        // TODO: Store message from client into this chat

        // Send a new message
        try {
            const response = await fetch('http://localhost:8000/financial/ask/', {
                method: 'POST',
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(body),
            });
            set.status = response.status;

            const res = await response.json();

            // TODO: Store response from mcp into this chat

            const isError = res.data.answer.isError;

            if (isError) {
                // TODO: something...
            }

            const resMsg = res.data.answer.content[0].text;

            return { message: resMsg };

        } catch (error: any) {
            set.status = 503;
            return { message: "MCP service is unavailable.", details: error.message };
        }

    }, {
        body: t.Object({ question: t.String() })
    });

export default messageRoutes;
