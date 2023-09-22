// JavaScript objects are a bit different.You do not need to create classes in order to create objects.

let student = {
    name:"gled fish",
    age: 19,
    marks:{
        science:100,
        math:100,
    },

    great: function(name){
        console.log('hello! '+ name);
    }
};

student.great("gled fish");