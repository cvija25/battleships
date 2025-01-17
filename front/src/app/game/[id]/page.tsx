import { FC } from "react";
import OpponentGrid from "@/components/OpponentGrid"
import PlayerGrid from "@/components/PlayerGrid";

// Define the expected `params` structure
interface GamePageProps {
  params: {
    id: string; // `id` will be a string
  };
}

const GamePage :FC<GamePageProps>= async( { params }) => {
  const { id } = await params; // No need to await params

  return (
    <div>
      <main className="p-4">
        <h1 className="text-2xl font-bold mb-6">Game {id}</h1>
        <OpponentGrid rows={5} columns={5} />
        <PlayerGrid rows={5} columns={5} />
      </main>
    </div>
  );
};

export default GamePage;
