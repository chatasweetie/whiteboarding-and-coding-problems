function averageCandyJar([ size, ...info ]) {
  let candy = 0;

  for (const [start, end, count] of info) {
    candy += count * (end - (start - 1));
  }

  return candy / size;
}

console.log(averageCandyJar([5, [1, 2, 100], [2, 5, 100], [3, 4, 100]]) === 160);
