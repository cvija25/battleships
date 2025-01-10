// pages/index.tsx
import Head from "next/head";
import Grid from "../components/Grid";

const Home: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
      <Head>
        <title>Grid Component</title>
        <meta name="description" content="Grid with clickable cells" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="p-4">
        <h1 className="text-2xl font-bold mb-6">Grid with Clickable Cells</h1>
        <Grid rows={5} columns={5} />
      </main>
    </div>
  );
};

export default Home;
