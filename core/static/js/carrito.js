// Esperar a que el documento esté listo
document.addEventListener("DOMContentLoaded", function() {
    // Obtener todos los campos de cantidad
    var quantityInputs = document.querySelectorAll('input[name="cantidad"]');
  
    // Agregar el evento de cambio a cada campo de cantidad
    quantityInputs.forEach(function(input) {
      input.addEventListener("change", function() {
        // Obtener el valor de la cantidad y el ID del elemento
        var quantity = this.value;
        var itemId = this.getAttribute("data-id");
  
        // Realizar una solicitud AJAX para actualizar la cantidad en el servidor
        fetch(`/modificar-cantidad/${itemId}/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
          },
          body: JSON.stringify({ cantidad: quantity }),
        })
          .then(function(response) {
            // Si la solicitud fue exitosa, actualizar el subtotal en la interfaz
            if (response.ok) {
              return response.json();
            } else {
              throw new Error("Error en la solicitud");
            }
          })
          .then(function(data) {
            // Actualizar el subtotal en la interfaz
            var subtotalElement = this.parentNode.querySelector("span.subtotal");
            subtotalElement.textContent = "Subtotal: " + data.subtotal;
          })
          .catch(function(error) {
            console.log(error);
          });
      });
    });
  
    // Agregar el evento de clic a los botones de eliminar
    var removeButtons = document.querySelectorAll(".remove-item");
  
    removeButtons.forEach(function(button) {
      button.addEventListener("click", function() {
        // Obtener el ID del elemento a eliminar
        var itemId = this.getAttribute("data-id");
  
        // Realizar una solicitud AJAX para eliminar el elemento del carrito
        fetch(`/eliminar-item/${itemId}/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
          },
        })
          .then(function(response) {
            // Si la solicitud fue exitosa, eliminar el elemento de la interfaz
            if (response.ok) {
              var cartItem = this.parentNode;
              cartItem.remove();
            } else {
              throw new Error("Error en la solicitud");
            }
          })
          .catch(function(error) {
            console.log(error);
          });
      });
    });
  });
  