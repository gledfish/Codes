// 变量 和常量
// var --> let 
let count = 0;
//  变量的块作用域
{
    let count;//块外不可访问
}
// 常量
const BASE_URL = "http***";
// 不可修改


const str = 'str';
const str2 = "str2";
const str3 = `${str1}${str2}`;// 模板字符串

// 解构赋值操作
const arr = [1, 2, 3];
const v1 = arr[0] //传统且繁琐
const [a, b, c] = [1, 2, 3];
console.log(a, b, c) // 1, 2, 3

const {username, age:userAge, ...other} = {
    name:"",
    age: 44,
    gender: 'male'
}//指定名字，或指定别名
// 指定其他未被指定的元素
console.log(other)

// 扩展运算符
const arr1 = [1, 2 ,3];
const arr2 = [4, 5, 6];
const arr3 = [...arr1, ...arr2];//解构填充 1, 2, 3, 4, 5, 6

// 数组方法
Array.from();//将伪数组转换为真实数组
function fn(){
    Array.from(arguments).forEach(function(item){
        // console.log(item)
    })
}
// 对象的方法 Object.assign()
const objA = {
    name:"geld",
    age: 18
}
const objB = Object.assign({}, objA);// 对象浅拷贝
console.log(objA, objB);
 
// Class
class A{
    constructor (name, age) {
        this.name = name;
        this.age = age;
    }
}
const a1 = new A('gled', 18)
console.log(a1);

class B extends A {
    constructor(name, age, gender) {
        super(name, age);
        this.gender = gender;
    }
    sayHello(){
        console.log("你好");
    }
}

// 箭头函数
const getSum1 = n => n + 3;
const getSum2 = (n1, n2) => n1 + n2;
const getSum3 = (n1, n2, ...other) => n1 + n2 + other;

// 1. Promise
const p1 = new Promise((resolve, reject) =>{
    resolve("1成功");// p1 成功
    reject("1失败");//p1 失败
})
console.log(p1)

// p1成功
p1.then(data =>{
    console.log(data)

    return new Promise((resolve, reject) => {
        resolve("2成功");//p1 成功
        reject("2失败");// p1 失败
    })
})
.then(data => {
    console.log(data);//第二个任务
})
// p1失败
.catch(err => {
    console.log(err);
})

// Async await
function asyncTask(){
    return new Promise((resolve, reject) => {
        const isSuccess = true;
        if(isSuccess){
            resolve("成功");
        } else {
            reject("失败");
        }
    });
}
async function main() {
    console.log('任务1')
    const data = await asyncTask();//像同步任务一样的顺序
    console.log(data);
    console.log("任务3")

}
// 2.proxy
// 代理程序员跟踪程序的变化
const obj = {
    name:"gled",
    age: 18
}
const p2 = new Proxy(obj, {
    get(target, property){// 被访问触发
        return obj[property];
    },
    set(target, property, value){
        //被设置触发
        obj[property] = value;
    }
})

p2.age = 21; // 返回并更改obj.name = 21

console.log(p1.name);
// 3. Module
// ESM
// CommonJS(Node.js)
