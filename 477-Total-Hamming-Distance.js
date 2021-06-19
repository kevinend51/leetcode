#!/usr/bin/env node

function totalHammingDistance(nums) {
    const count = nums.reduce((acc, num) => {
        let i = 0
        while(num) {
            if (num % 2) {
                acc.set(i, (acc.get(i) ?? 0) + 1)
            }
            num >>= 1
            i += 1
        }
        return acc
    }, new Map())
    return [...count.values()]
        .reduce((acc, val) => acc + val * (nums.length - val), 0)
}
