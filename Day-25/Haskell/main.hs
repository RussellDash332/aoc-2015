import System.IO
import Data.List
import Data.Maybe

-- Converts string to integer
toInt:: String -> Int
toInt = read

-- String finder by index
findString :: (Eq a) => [a] -> [a] -> Int
findString search str = fromMaybe (-1) $ findIndex (isPrefixOf search) (tails str)

-- Substring
substr :: Int -> Int -> String -> String
substr m n str = take (n - m) (drop m str)

main = do
  contents <- readFile "../25.in"
  let r = toInt $ substr ((findString "row" contents) + 4) ((findString "column" contents) - 2) contents
  let c = toInt $ substr ((findString "column" contents) + 7) (length contents - 1) contents
  let pow = (r + c) * (r + c - 1) `div` 2 - r
  putStr "Part 1: "; print (20151125 * (252533 ^ pow) `mod` 33554393);
  putStrLn "Part 2: THE END!";