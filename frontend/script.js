fetch("http://127.0.0.1:5000/orders")
  .then(response => response.json())
  .then(data => {

    const compressed = document.getElementById("compressed");
    data.compressed_orders.forEach(order => {
      compressed.innerHTML += `
        <div class="card">${order.item} × ${order.quantity}</div>
      `;
    });

    const priority = document.getElementById("priority");
    data.priority_orders.forEach(order => {
      priority.innerHTML += `
        <div class="card">${order.item} (${order.prep_time} mins)</div>
      `;
    });

  });
