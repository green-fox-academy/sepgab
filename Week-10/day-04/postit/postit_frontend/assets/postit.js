'use strict';

const root = 'http://localhost:3000';
const newTask = document.querySelector('.text');
const submitTask = document.querySelector('.submitTodo');

const ajax = new Object();

ajax.get = function(url, callback) {
	let xhr = new XMLHttpRequest(),
  method = "GET";

	xhr.open(method, root+url, true);

	xhr.onreadystatechange = function () {
		if(xhr.readyState === XMLHttpRequest.DONE) {
			if(xhr.status === 200) {
				var rsp = JSON.parse( xhr.response );
				callback(rsp);
			} else {
				new Error('API error!');
				console.log(xhr.status);
			}
		}
	};
	xhr.send();
}

ajax.post = function(url, message, callback) {
	let xhr = new XMLHttpRequest(),
  method = "POST";

	xhr.open(method, root+url, true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.setRequestHeader('Accept', 'application/json');

	console.log( 'message sent: ' + JSON.stringify(message) );
	xhr.send(JSON.stringify(message));

	xhr.onreadystatechange = function () {
		if(xhr.readyState === XMLHttpRequest.DONE) {
			if(xhr.status === 200) {
				var rsp = JSON.parse( xhr.response );
				callback(rsp);
			} else {
				new Error('API error!');
				console.log(xhr.status);
			}
		}
	};
}

ajax.put = function(url, message, callback) {
	let xhr = new XMLHttpRequest(),
  method = "PUT";

	xhr.open(method, root+url, true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.setRequestHeader('Accept', 'application/json');

	console.log( 'message sent: ' + JSON.stringify(message) + 'on the folowing url: ' + root + url);
	xhr.send(JSON.stringify(message));

	xhr.onreadystatechange = function () {
		if(xhr.readyState === XMLHttpRequest.DONE) {
			if(xhr.status === 200) {
				var rsp = JSON.parse( xhr.response );
				callback(rsp);
			} else {
				new Error('API error!');
				console.log(xhr.status);
			}
		}
	};
}

ajax.delete = function(url, message, callback) {
	let xhr = new XMLHttpRequest(),
  method = "DELETE";

	xhr.open(method, root+url, true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.setRequestHeader('Accept', 'application/json');

	console.log( 'message sent: ' + JSON.stringify(message) );
	xhr.send(JSON.stringify(message));

	xhr.onreadystatechange = function () {
		if(xhr.readyState === XMLHttpRequest.DONE) {
			if(xhr.status === 200) {
				var rsp = JSON.parse( xhr.response );
				callback(rsp);
			} else {
				new Error('API error!');
				console.log(xhr.status);
			}
		}
	};
}


const controller = new Object();



controller.render = function(tasks) {
	let listOfTasks = document.querySelector('.todos')
	listOfTasks.innerHTML = '';
  for (let i = 0; i < tasks.length; i++) {
    let taskToAdd = document.createElement('p');
    taskToAdd.innerText = tasks[i].title;

		let deleteButtonToAdd = document.createElement('img');
		deleteButtonToAdd.setAttribute('src', 'assets/delete.svg');
		deleteButtonToAdd.addEventListener('click', function(){
			let url = '/todos/' + tasks[i].ID;
			let message = {
				"ID": tasks[i].ID
			};
			ajax.delete(url, message, controller.render);
		});
		taskToAdd.appendChild(deleteButtonToAdd);

		let checkboxToAdd = document.createElement('input');
		checkboxToAdd.setAttribute('type', 'checkbox');
		if (tasks[i].status === 1) {
			checkboxToAdd.checked = true;
			taskToAdd.classList.add('done')
		}
		checkboxToAdd.addEventListener('click', function(){
			let url = '/todos/' + tasks[i].ID;
			let status = null;
			if (checkboxToAdd.checked === true) {
				status = 1;
			} else {
				status = 0;
			}
			let message = {
				"status": status
			};
			ajax.put(url, message, controller.render);
		});
		taskToAdd.appendChild(checkboxToAdd);

		taskToAdd.setAttribute('id', i);
		taskToAdd.setAttribute('draggable', 'true');
		taskToAdd.setAttribute('ondragstart', 'dragstart_handler(event);');

    listOfTasks.appendChild(taskToAdd);
  }
};

(controller.displayTasks = function() {
  ajax.get('/todos', controller.render);
})();

function dragstart_handler(ev) {
 // Add the target element's id to the data transfer object
 ev.dataTransfer.setData("text/plain", ev.target.id);
 ev.dropEffect = "move";
}
function dragover_handler(ev) {
 ev.preventDefault();
 // Set the dropEffect to move
 ev.dataTransfer.dropEffect = "move"
}
function drop_handler(ev) {
 ev.preventDefault();
 // Get the id of the target and add the moved element to the target's DOM
 var data = ev.dataTransfer.getData("text");
 ev.target.appendChild(document.getElementById(data));
}



submitTask.addEventListener('click', function(){
	if (newTask.value.length >= 3) {
		let url = '/todos';
		let message = {
			"title": newTask.value,
			"status": 0
		};
		ajax.post(url, message, controller.render);
		newTask.value = '';
	} else {
		alert("Make it at least 3 characters long!");
	}
})
