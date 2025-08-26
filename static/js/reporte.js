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

}

// cargar reporte al inicio
cargarReporte();

// (Opcional) refrescar cada 5 segundos
setInterval(cargarReporte, 2000);
