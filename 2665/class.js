class createCounter {
    constructor(init) {
        this.init = init;
        this.currentCount = init;
    }
    
    increment() {
        this.currentCount += 1;
        return this.currentCount
    }

    decrement() {
        this.currentCount -= 1;
        return this.currentCount
    }

    reset() {
        this.currentCount = this.init
        return this.currentCount
    }
}

const counter = new createCounter(5)
console.log(counter.increment()); // 6
console.log(counter.reset()); // 5
console.log(counter.decrement()); // 4