// pages/index.tsx
import Head from "next/head";
import OpponentGrid from "../components/OpponentGrid";
import PlayerGrid from "../components/PlayerGrid"

const Home: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
      <Head>
        <title>Grid Component</title>
        <meta name="description" content="Grid with clickable cells" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="p-4">
        <h1 className="text-2xl font-bold mb-6">Wellcome to Battleships online!!</h1>
      </main>
    </div>
  );
};

export default Home;
