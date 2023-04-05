let rolls = 0;
let die1 = 0;
let die2 = 0;

do {
  // Roll two D100's
  die1 = Math.floor(Math.random() * 100) + 1;
  die2 = Math.floor(Math.random() * 100) + 1;

  // Increment roll count
  rolls++;
} while (die1 !== die2);

console.log(`It took ${rolls} rolls to get the same number on both dice.`);
