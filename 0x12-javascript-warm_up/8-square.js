#!/usr/bin/node

const args = process.argv.slice(2);
const size = parseInt(args[0], 10);

if (isNaN(size) || size <= 0) {
  console.log('Missing size');
} else {
  const line = 'X'.repeat(size);
  for (let i = 0; i < size; i++) {
    console.log(line);
  }
}
