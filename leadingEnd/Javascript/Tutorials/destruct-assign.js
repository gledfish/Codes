// eg：
const x = [1, 2, 3, 4, 5];
const [y, z] = x;//y = 1, z = 2

const foo1 = ['one', 'two', 'three'];

const [red, yellow, green] = foo;

const foo = ['one', 'two'];

//Basic variable assignment
const [red2, yellow2, green2, blue] = foo;
console.log(red); // "one"
console.log(yellow); // "two"
console.log(green); // undefined
console.log(blue);  //undefined

//Swapping variables
const arr = [1, 2, 3];
[arr[2], arr[1]] = [arr[1], arr[2]];
console.log(arr); // [1, 3, 2]

//Ignoring some returned values
function f() {
    return [1, 2, 3];
}

const [a1, , b1] = f();
console.log(a1); // 1
console.log(b1); // 3

const [c1] = f();
console.log(c1); // 1

// Using a binding pattern as the rest property
const [a, b, ...[c, d, ...[e, f]]] = [1, 2, 3, 4, 5, 6];
console.log(a, b, c, d, e, f); // 1 2 3 4 5 6