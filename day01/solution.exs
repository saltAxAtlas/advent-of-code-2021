lines = File.read!("./input.txt") |>
        String.replace("\r", "") |>
        String.split("\n") |>
        Enum.map(fn x -> String.to_integer("0" <> x) end)

# Part 1
IO.inspect(lines |>
        Enum.chunk_every(2, 1) |>
        Enum.filter(fn x -> List.first(x) < List.last(x) end) |>
        Enum.count())

# Part 2
IO.inspect(lines |>
        Enum.chunk_every(4, 1) |>
        Enum.filter(fn x -> List.first(x) < List.last(x) end) |>
        Enum.count())
