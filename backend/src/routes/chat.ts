import { Elysia } from "elysia";

const chatRoutes = new Elysia({ prefix: "/chats" })
    .get("/", async () => {
        // TODO: Return the chats
    })

    .get("/:id", async () => {
        // TODO: Get a single chat...
        // Include conversations...
    })

    .post("/", async () => {
        // TODO: Create new chat
    });

export default chatRoutes;

