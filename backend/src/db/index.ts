//Imports
import { Kysely, PostgresDialect } from 'kysely'; // Sets up a typed database connection
import { Pool } from 'pg';  // Imports PostgreSQL connection
import * as dotenv from 'dotenv'; // Loads the enbviroment variables for db connection
import { DB } from './schema';  // Imports the database schemas

dotenv.config();

// Init Kysely instance with PostgreSQL 
export const db = new Kysely<DB>({
  dialect: new PostgresDialect({
    pool: new Pool({
      connectionString: process.env.DATABASE_URL,
    }),
  }),
});