/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let current = init;
    return {
        increment: function() {
            // current++;
            // return current
            return ++current;
        }
        , reset: function() {
            // current = init
            // return current
            return (current = init)
        }
        , decrement: function() {
            // current--;
            // return current;
            return --current;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */

const counter = createCounter(5)
console.log(counter.increment()); // 6
console.log(counter.reset()); // 5
console.log(counter.decrement()); // 4