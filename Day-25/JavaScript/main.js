const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    console.log();
    let rc = line.match(/\d+/g);
    var r = parseInt(rc[0]);
    var c = parseInt(rc[1]);
    var ans = 20151125;
    for (let i = 0; i < (r + c) * (r + c - 1) / 2 - r; i++) {
        ans = 252533 * ans % 33554393;
    }
    console.log("Part 1: " + ans);
    console.log("Part 2: THE END!");
});