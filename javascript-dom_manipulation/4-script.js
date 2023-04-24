#!/usr/bin/node

const addItem = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');

addItem.addEventListener('click', function () {
  const liElement = document.createElement('li');

  liElement.innerText = 'Item';

  myList.appendChild(liElement);
});
