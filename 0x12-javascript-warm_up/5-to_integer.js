#!/usr/bin/env node

const args = process.argv.slice(2);
const num = parseInt(args[0], 10);

if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
