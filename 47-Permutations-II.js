#!/usr/bin/env node

function permuteUnique(nums) {
    const visited = new Set()
    const perm = []    

    function nextNum() {
        if (nums.length === 0) {
            visited.add(JSON.stringify(perm))
            return
        }
        
        for (let i = 0; i < nums.length; i += 1) {
            const num = nums[i]
            if (visited.has(JSON.stringify([...perm, num]))) {
                continue
            }
            
            nums.splice(i, 1)
            perm.push(num)
            nextNum()
            perm.pop(num)
            nums.splice(i, 0, num)
        }
        visited.add(JSON.stringify(perm))
    }
    
    nextNum()
    return [...visited]
        .map(s => JSON.parse(s))
        .filter(arr => arr.length === nums.length)
}
