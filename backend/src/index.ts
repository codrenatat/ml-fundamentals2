import cors from "@elysiajs/cors";
import swagger from "@elysiajs/swagger";
import { Elysia } from "elysia";
import chatRoutes from "./routes/conversation";
import messageRoutes from "./routes/messages";

// Create Elysia instance
const app = new Elysia()
    .use(swagger())
    .use(cors())
    .use(chatRoutes)
    .use(messageRoutes)
    .get("/", () => "Hello Elysia")
    .get("/health", () => "healthy")
    .listen(3333);

console.log(
    `🦊 Elysia is running at ${app.server?.hostname}:${app.server?.port}`
);
