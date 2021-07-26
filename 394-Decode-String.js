#!/usr/bin/env node

const regexp = /^(((?<lb>\d+)\[)|(?<rb>\])|(?<str>[a-z]+))(?<rest>.*)$/

function pushStr(stack, str) {
    const i = stack.length - 1
    typeof stack[i] === 'string' ? stack[i] += str : stack.push(str)
}

function decodeString(s) {
    let stack = []
    while (s) {
        const { groups: { lb, rb, str, rest } } = regexp.exec(s)
        if (lb) {
            stack.push(Number(lb))
        } else if (rb) {
            const str = stack.pop()
            const num = stack.pop()
            pushStr(stack, str.repeat(num))
        } else {
            pushStr(stack, str)
        }
        s = rest
    }
    return stack[0]
}
