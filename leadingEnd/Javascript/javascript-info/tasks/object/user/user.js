user = Object();

user.name = "John";

user.surname = "Smith";
user.name = "Pete";
delete user.name;

function isEmpty(obj){
    for(let key in obj){
        return false;
    }
    return true;
}