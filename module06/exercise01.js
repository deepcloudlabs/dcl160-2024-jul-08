function* _3n_plus1(n) {
    console.log("_3n_plus1 just started...");
    yield n;
    while (n > 1) {
        if (n % 2 === 0) {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
        console.log(`yielding ${n}`);
        yield n;
    }
    console.log("_3n_plus1 about to return...");
}

for (const value of _3n_plus1(17)) {
    console.log(`for: ${value}`);
}