---
title: 'Advent of Code 2022 Day 1'
date: 2022-12-01
permalink: /posts/2022/12/advent-of-code-day-1/
tags:
  - python
  - puzzles
  - fun
---

2022 is the first year I am participating in [Advent of Code](https://adventofcode.com/). I am using [this repository](https://github.com/nateraluis/advent-of-code) to store my solutions.

For solving the puzzles, I will be working with with [Python](https://www.python.org/) and trying to solve all the solutions using standard Python libraries. The code is stored in the `2022` directory and each solution is stored in `day{number}.py` files. For those of you that want to replicate them, you can create a new environment and use the dependencies that are stored in `requirements.txt` and can be installed using `pip install -r requirements.txt`.

For maintaining code quality I am using pre-commit hooks. The hooks are stored in `.pre-commit-config.yaml` and can be installed using `pre-commit install`.

Here is the first problem:

> This list represents the Calories of the food carried by five Elves
>
> In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).
>
> Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

## Solution

> **⚠️ Warning**
> 
> Do not keep reading if you are participating in Advent of Code and **do not** want to see the solution.

### Part 1

First, to get the data I used the `aocd` [library](https://github.com/wimglenn/advent-of-code-data) and stored the data for the first challenge in a variable:

```python
import aocd

data = aocd.get_data(day=1, year=2022)
```

The data was stored as a `string`, I parsed it by splitting the lines between data entries, and stored it in a list of lists, where I converted and stored each entire as an `integer`.

```python
elves_food = [[int(food) for food in elves.splitlines()] for elves in data.split("\n\n")]
```

Finally for getting the maximum number of calories I got the maximum of the sum of lists:

``` python
print("Max food calories: ", max(sum(elf) for elf in elves_food))
```

### Part 2

The second part of the challenge was to find the three Elves who have the most calories in their food, and sum the calories count to get the total of calories by the top three Elves. 

To solve this part one can sum all the calories by Elf and then sort the list by the sum, or one can use a [Heap queue](https://en.wikipedia.org/wiki/Heap_(data_structure)), that was the way I went for. It was a nice way to get to know about Heap queues. 

The solution is as follows:

```python
import heapq 

top_three = heapq.nlargest(3, elves_food, key=sum)

print("Total food calories: ", sum(sum(elf) for elf in top_three))
```
