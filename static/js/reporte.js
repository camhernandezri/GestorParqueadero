async function cargarReporte() {
  let res = await fetch("/reporte");
  let data = await res.json();

  // Total
  document.getElementById("total").textContent = "$" + data.total_dia;
  document.getElementById("totalVehiculos").textContent = data.registros.length;

  // Tabla con DataTables
  let tbody = document.querySelector("#tabla-reporte tbody");
  tbody.innerHTML = "";
  data.registros.forEach(r => {
    tbody.innerHTML += `
      <tr>
        <td>${r.placa}</td>
        <td>${r.entrada}</td>
        <td>${r.salida ?? "-"}</td>
        <td>${r.costo ?? "-"}</td>
      </tr>`;
  });
  new DataTable("#tabla-reporte");

  // Gráfica de ingresos
  let ctx = document.getElementById("grafica").getContext("2d");
  let labels = data.registros.map(r => r.placa);
  let valores = data.registros.map(r => r.costo || 0);

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [{
        label: "Ingresos por vehículo",
        data: valores,
        backgroundColor: "rgba(54, 162, 235, 0.6)"
      }]
    }
  });
}

cargarReporte();
