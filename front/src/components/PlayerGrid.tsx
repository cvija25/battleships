"use client"

interface GridProps {
  rows: number;
  columns: number;
}

interface Cell {
  row: number;
  col: number;
}

const PlayerGrid: React.FC<GridProps> = ({ rows, columns }) => {
  return (
    <div className="flex flex-col space-y-2">
        {Array.from({ length: rows }).map((_, rowIndex) => (
            <div key={rowIndex} className="flex space-x-2">
            {Array.from({ length: columns }).map((_, colIndex) => (
                <div
                    key={colIndex}
                    className={`w-16 h-16 border border-gray-300 flex items-center justify-center text-sm`}
                    >
                    {`(${rowIndex}, ${colIndex})`}
                </div>
            ))}
            </div>
        ))}
    </div>
  );
};

export default PlayerGrid;
