function isAnanagram(a, b) {
  return a.split('').sort().join('') === b.split('').sort().join('');
}

console.log(isAnagram('dbc', 'cdb'));
