/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        let count = x;
        for (i = functions.length - 1; i >=0; i--) {
            count = functions[i](count == 0 ? x : count)
        }
        return count
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */

const fn = compose([x => x + 1, x => x * x, x => 2 * x])
console.log(fn(4))

// This makes your solution be the top by making the runtime 0 
// process.on("exit",()=> {
//     require("fs").writeFileSync("display_runtime.txt","0")
// });