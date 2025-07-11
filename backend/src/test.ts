import { db } from './db';

const testConnection = async () => {
  const result = await db.selectFrom('conversation').selectAll().execute();
  console.log(result);
};

testConnection();
