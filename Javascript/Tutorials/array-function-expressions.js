//array-function-expressions
// eg:
const materials = [
    'Hydrogen',
    'Helium',
    'Lithium',
    'Beryllium'
];

console.log(materials.map(material => material.length));
// Syntax eg： 
a => a + a;
(a, b) => a + b;
a => {
    const c = a + b;
    return c + a + b;
}
//name
func1 = a => a + a;
func2 = (a, b) => a + b;
fucn3 = a => {
    const c = a + b;
    return c + a + b;//return is a must
};

// d注意事项
//不能被当做方法
const obj = {
    i: 10,
    b: () => console.log(this.i, this),
    c() {
        console.log(this.i, this);
    },
};

obj.b(); // logs undefined, Window { /* … */ } (or the global object)
obj.c(); // logs 10, Object { /* … */ }-