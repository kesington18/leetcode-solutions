/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    var counter = init;
    return {
        increment: function () {
            counter = counter + 1;
            return counter;
        },
        reset: function () {
            return counter = init;
        },
        decrement: function () {
            counter = counter - 1;
            return counter;
        }
    };
};
const counter = createCounter(5);
/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */