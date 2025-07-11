import { Kysely, PostgresDialect } from 'kysely';
import { Pool } from 'pg';
import * as dotenv from 'dotenv';
import { DB } from './schema';

dotenv.config();

export const db = new Kysely<DB>({
  dialect: new PostgresDialect({
    pool: new Pool({
      connectionString: process.env.DATABASE_URL,
    }),
  }),
});