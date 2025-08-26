let dataTable = null;
let chart = null;

async function cargarReporte() {
  let res = await fetch("/reporte");
  let data = await res.json();

  // === Totales ===
  document.getElementById("total").textContent = "$" + data.total_dia;
  document.getElementById("totalVehiculos").textContent = data.registros.length;

  // === Tabla ===
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

  // Inicializar o refrescar DataTable
  if (dataTable) {
    dataTable.destroy();
  }
  dataTable = new DataTable("#tabla-reporte");

  // === Gráfica ===
  let ctx = document.getElementById("grafica").getContext("2d");
  let labels = data.registros.map(r => r.placa);
  let valores = data.registros.map(r => r.costo || 0);

  if (chart) {
    chart.destroy();
  }
  chart = new Chart(ctx, {
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

// cargar reporte al inicio
cargarReporte();

// (Opcional) refrescar cada 5 segundos
setInterval(cargarReporte, 2000);
