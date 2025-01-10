"use client"
// components/Grid.tsx
import { useEffect, useState } from "react";

interface GridProps {
  rows: number;
  columns: number;
}

interface Cell {
  row: number;
  col: number;
}

const Grid: React.FC<GridProps> = ({ rows, columns }) => {
  const [clickedCells, setClickedCells] = useState<Cell[]>([]);
  const [messages, setMessages] = useState<string[]>([])
  const [socket, setSocket] = useState<WebSocket|null>(null);

  const handleCellClick = (row: number, col: number) => {
    const newClickedCells = [...clickedCells, { row, col }];
    setClickedCells(newClickedCells);
    socket?.send(`Cell clicked: Row ${row}, Col ${col}`);
  };

  useEffect(() => {
    const newSocket = new WebSocket('ws://localhost:8000/ws');


    newSocket.onopen = () => {
        console.log("connected");
        setSocket(newSocket);
    }

    newSocket.onmessage = (event) => {
        console.log("Message from server:", event.data);
        setMessages((prev) => [...prev, event.data]);
    }
    
    return () => {
        newSocket.close();
    } 
  } ,[]);

  return (
    <div className="flex flex-col space-y-2">
        <div className="mt-4 p-4 border border-gray-300">
            <h3 className="font-bold">Messages from Server:</h3>
            <ul>
            {messages.map((msg, idx) => (
                <li key={idx}>{msg}</li>
            ))}
            </ul>
        </div>
        <div>
            {Array.from({ length: rows }).map((_, rowIndex) => (
                <div key={rowIndex} className="flex space-x-2">
                {Array.from({ length: columns }).map((_, colIndex) => (
                    <div
                    key={colIndex}
                    className={`w-16 h-16 border border-gray-300 flex items-center justify-center text-sm cursor-pointer ${
                        clickedCells.some(
                        (cell) => cell.row === rowIndex && cell.col === colIndex
                        )
                        ? "bg-blue-300"
                        : "bg-white"
                    }`}
                    onClick={() => handleCellClick(rowIndex, colIndex)}
                    >
                    {`(${rowIndex}, ${colIndex})`}
                    </div>
                ))}
                </div>
            ))}
        </div>
    </div>
  );
};

export default Grid;
