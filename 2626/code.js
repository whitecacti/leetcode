/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let count = init;
    // for (i = 0; i < nums.length; i++) {
    //     count = fn(count, nums[i])  
    // }
    for (const num of nums) {
        count = fn(count, num)
    }
    return count
};

const arr = [1,2,8,3,10,23]
const fn = function sum(accum, curr) { return (curr + accum) % 2; }
const init = 25
console.log(reduce(arr,fn,init))