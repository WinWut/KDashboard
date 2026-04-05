async function fetchData() {
  try {
    const res = await fetch("http://127.0.0.1:8000/data");
    const data = await res.json();

    console.log("DATA:", data); // debug

    // update UI
    document.getElementById("ec").innerText = data.ec + " Uq";
    document.getElementById("ph").innerText = data.ph;
    document.getElementById("humidity").innerText = data.humidity;
    document.getElementById("watertemp").innerText = data.watertemp;
    document.getElementById("airtemp").innerText = data.airtemp;
  } catch (err) {
    console.error("Fetch error:", err);
  }
}

// fetch every second
setInterval(fetchData, 2000);

