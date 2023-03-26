// 待办列表
const todoList = document.getElementById('todo-list');
//添加待办事务
const newTodo = document.getElementById('new-todo');
const addTodoButton = document.getElementById('add-todo');

//删除待办事务
const deleteItem = document.getElementById('delete-item');
const deleteButton = document.getElementById('delete-item-button');

function addTodo() {
    const todoText = newTodo.value;
    if (todoText !== '') {
        const todoItem = document.createElement('li');
        todoItem.textContent = todoText;
        todoList.appendChild(todoItem);
        newTodo.value = '';
    } else {
        alert("请确认是否输入待办事项");
    }
}

//删除待办事项
function deleteTodo() {
    const deleteText = deleteItem.value;
    if(deleteText != '') {
        const todoItems = todoList.getElementsByTagName('li');
        let itemToDelete = null;
        for (let i = 0; i < todoItems.length; i++) {
            if (todoItems[i].textContent === deleteText) {
                itemToDelete = todoItems[i];
                break;
            }
        }
        if (itemToDelete !== null) {
            todoList.removeChild(itemToDelete);
            deleteItem.value = '';
        } else {
            alert('未找到对应的待办事项');
        }
    } else {
        alert("请确认是否成功输入要删除的事务");
    }
}

addTodoButton.addEventListener('click', addTodo);
deleteButton.addEventListener('click', deleteTodo);

