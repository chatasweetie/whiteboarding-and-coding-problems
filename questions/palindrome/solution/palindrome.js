function palindrome(str) {
  str = str.replace(/\s/g, '');

  const letters = {};

  for (const letter of str) {
    const count = letters[letter] || 0;
    letters[letter] = count + 1;
  }

  let oddLetter = '';
  let out = [];

  for (const letter in letters) {
    const count = letters[letter];
    const nextLetters = letter.repeat(Math.floor(count / 2));

    if (nextLetters) {
      out.push(...nextLetters);
    }

    if (count % 2 !== 0) {
      oddLetter = letter;
    }
  }

  return out.join('') + oddLetter + out.reverse().join('');
}

console.log(palindrome('add') === 'dad');
