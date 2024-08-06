document.addEventListener('DOMContentLoaded', function () {
    cargarTareas();
});

function cargarTareas() {
    fetch('/api/tareas/')
        .then(response => response.json())
        .then(data => {
            data.forEach(tarea => mostrarTarea(tarea));
        })
        .catch(error => console.error('Error al cargar las tareas:', error));
}

document.getElementById('tarea-form').addEventListener('submit', function (event) {
    event.preventDefault();
    agregarTarea();
});

function agregarTarea() {
    var descripcion = document.getElementById('description').value;

    // Enviar datos al servidor para guardar la tarea
    fetch('/api/tareas/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ description: descripcion, eliminada: false })
    })
        .then(response => response.json())
        .then(data => {
            // Recuperar y mostrar la tarea guardada
            mostrarTarea(data);
            document.getElementById('tarea-form').reset();
        })
        .catch(error => console.error('Error al guardar la tarea:', error));
}

function mostrarTarea(tarea) {
    var tablaCuerpo = document.getElementById('tabla-cuerpo');
    var nuevaFila = document.createElement('tr');
    nuevaFila.setAttribute('data-parent-id', tarea.id);

    var celdaID = document.createElement('td');
    celdaID.textContent = tarea.id;

    var celdaDescripcion = document.createElement('td');
    celdaDescripcion.textContent = tarea.description;

    var celdaEstado = document.createElement('td');
    celdaEstado.textContent = tarea.eliminada ? 'Si' : 'No';
    if (tarea.eliminada) {
        nuevaFila.appendChild(celdaID);
        nuevaFila.appendChild(celdaDescripcion);
        nuevaFila.appendChild(celdaEstado);
    } else {
        var celdaAcciones = document.createElement('td');
        var botonEliminar = document.createElement('button');
        botonEliminar.textContent = 'Eliminar';
        botonEliminar.classList.add('btn', 'btn-danger', 'me-2');
        botonEliminar.onclick = function () {
            eliminarTarea(tarea.id);
        };

        var botonSubtarea = document.createElement('button');
        botonSubtarea.textContent = 'Agregar Subtarea';
        botonSubtarea.classList.add('btn', 'btn-secondary');
        botonSubtarea.onclick = function () {
            abrirModalSubtarea(tarea.id);
        };

        celdaAcciones.appendChild(botonEliminar);
        celdaAcciones.appendChild(botonSubtarea);

        nuevaFila.appendChild(celdaID);
        nuevaFila.appendChild(celdaDescripcion);
        nuevaFila.appendChild(celdaEstado);
        nuevaFila.appendChild(celdaAcciones);
    }
    tablaCuerpo.appendChild(nuevaFila);

    // Mostrar subtareas si existen
    if (tarea.subtareas && tarea.subtareas.length > 0) {
        tarea.subtareas.forEach(subtarea => mostrarSubtarea(subtarea, nuevaFila));
    }
}

function abrirModalSubtarea(tareaId) {
    var modal = new bootstrap.Modal(document.getElementById('subtareaModal'));
    var subtareaForm = document.getElementById('subtarea-form');

    subtareaForm.onsubmit = function (event) {
        event.preventDefault();
        agregarSubtarea(tareaId);
        modal.hide();
    };

    modal.show();
}

function agregarSubtarea(tareaId) {
    var descripcionSubtarea = document.getElementById('subtarea-description').value;

    // Enviar datos al servidor para guardar la subtarea
    fetch(`/api/subtareas/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ description: descripcionSubtarea, eliminada: false, id_tarea: tareaId })
    })
        .then(response => response.json())
        .then(data => {
            // Recuperar y mostrar la subtarea guardada
            var filaTarea = document.querySelector(`tr[data-parent-id='${tareaId}']`);
            mostrarSubtarea(data, filaTarea);
            document.getElementById('subtarea-form').reset();
        })
        .catch(error => console.error('Error al guardar la subtarea:', error));
}

function mostrarSubtarea(subtarea, filaTarea) {
    var nuevaFilaSubtarea = document.createElement('tr');
    nuevaFilaSubtarea.setAttribute('data-id', subtarea.id);
    nuevaFilaSubtarea.setAttribute('data-parent-id', subtarea.id_tarea);
    nuevaFilaSubtarea.classList.add('subtarea'); // Añadir la clase subtarea

    var celdaVacia = document.createElement('td'); // Columna vacía para el desplazamiento

    // var celdaID = document.createElement('td');
    // celdaID.textContent = subtarea.id;

    var celdaDescripcion = document.createElement('td');
    celdaDescripcion.textContent = subtarea.description;

    var celdaEstado = document.createElement('td');
    celdaEstado.textContent = subtarea.eliminada ? 'Si' : 'No';

    if (subtarea.eliminada) {
        nuevaFilaSubtarea.appendChild(celdaVacia); // Añadir la columna vacía
        nuevaFilaSubtarea.appendChild(celdaDescripcion);
        nuevaFilaSubtarea.appendChild(celdaEstado);
    } else {
        var celdaAcciones = document.createElement('td');
        var botonEliminar = document.createElement('button');
        botonEliminar.textContent = 'Eliminar';
        botonEliminar.classList.add('btn', 'btn-danger', 'me-2');
        botonEliminar.onclick = function () {
            eliminarSubtarea(subtarea.id);
        };

        celdaAcciones.appendChild(botonEliminar);

        nuevaFilaSubtarea.appendChild(celdaVacia); // Añadir la columna vacía
        // nuevaFilaSubtarea.appendChild(celdaID);
        nuevaFilaSubtarea.appendChild(celdaDescripcion);
        nuevaFilaSubtarea.appendChild(celdaEstado);
        nuevaFilaSubtarea.appendChild(celdaAcciones);
    }
    // Insertar la nueva fila de subtarea justo después de la fila de la tarea
    filaTarea.insertAdjacentElement('afterend', nuevaFilaSubtarea);

}


function eliminarTarea(tareaId) {
    fetch(`/api/tareas/${tareaId}/`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ eliminada: true })
    })
        .then(response => {
            if (response.ok) {
                var filaTarea = document.querySelector(`tr[data-parent-id='${tareaId}']`);
                var celdaEstado = filaTarea.querySelector('td:nth-child(3)');
                celdaEstado.textContent = 'Si';
                var celdaAction = filaTarea.querySelector('td:nth-child(4)');
                celdaAction.textContent = '';

                // Actualizar el estado de las subtareas asociadas
                var subtareas = document.querySelectorAll(`tr.subtarea`);
                subtareas.forEach(subtarea => {
                    var subtareaId = subtarea.getAttribute('data-id');
                    var parentId = subtarea.getAttribute('data-parent-id');
                    if (String(parentId) === String(tareaId)) {
                        eliminarSubtarea(subtareaId);
                    }
                });
            } else {
                console.error('Error al actualizar el estado de la tarea');
            }
        })
        .catch(error => console.error('Error al actualizar el estado de la tarea:', error));
}



function eliminarSubtarea(subtareaId) {
    fetch(`/api/subtareas/${subtareaId}/`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ eliminada: true })
    })
        .then(response => {
            if (response.ok) {
                var filaSubtarea = document.querySelector(`tr[data-id='${subtareaId}']`);
                var celdaEstado = filaSubtarea.querySelector('td:nth-child(3)');
                celdaEstado.textContent = 'Si';
                var celdaAction = filaSubtarea.querySelector('td:nth-child(4)');
                celdaAction.textContent = '';
            } else {
                console.error('Error al actualizar el estado de la subtarea');
            }
        })
        .catch(error => console.error('Error al actualizar el estado de la subtarea:', error));
}
