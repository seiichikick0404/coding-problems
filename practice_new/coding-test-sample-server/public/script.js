'use strict';

const todoList = document.getElementById('todoList');
const doneList = document.getElementById('doneList');

// チェックボックスを作成する関数
function createNewCheckBox(checked) {
  const newCheckBox = document.createElement("input");
  newCheckBox.type = "checkbox";
  newCheckBox.checked = checked;
  if (checked) {
    newCheckBox.addEventListener("click", clickDoneList);
  } else {
    newCheckBox.addEventListener("click", clickTodoList);
  }
  return newCheckBox;
}

// 登録ボタンが押されたときの処理
function submit() {
  const taskInput = document.getElementById("taskInput");
  if (taskInput.value.trim() === '') return; // テキストボックス内が空の場合はタスクを追加しない
  const newTask = document.createElement('li');
  newTask.appendChild(createNewCheckBox(false)); // チェックが入っていない状態
  const taskSpan = document.createElement('span');
  taskSpan.textContent = taskInput.value;
  newTask.appendChild(taskSpan);
  todoList.appendChild(newTask);
  taskInput.value = ''; // テキストボックスの内容を空にする
}

// TODOリストのチェックボックスがクリックされたときの処理
function clickTodoList(e) {
  const node = e.target.parentElement;
  const newTask = document.createElement('li');
  newTask.appendChild(createNewCheckBox(true)); // チェックが入った状態
  const taskSpan = document.createElement('span');
  taskSpan.textContent = node.querySelector('span').textContent;
  newTask.appendChild(taskSpan);
  doneList.appendChild(newTask);
  node.remove(); // TODOリストから削除
}

// DONEリストのチェックボックスがクリックされたときの処理
function clickDoneList(e) {
  const node = e.target.parentElement;
  const newTask = document.createElement('li');
  newTask.appendChild(createNewCheckBox(false)); // チェックが入っていない状態
  const taskSpan = document.createElement('span');
  taskSpan.textContent = node.querySelector('span').textContent;
  newTask.appendChild(taskSpan);
  todoList.appendChild(newTask);
  node.remove(); // DONEリストから削除
}
