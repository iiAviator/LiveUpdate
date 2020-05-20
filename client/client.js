const socket = new WebSocket("ws://localhost:8765");

let data = 0;

socket.addEventListener("open", function (event) {
  socket.send("Client Connected");
});

socket.addEventListener("message", function (event) {
  console.log("SERVER: " + event.data);
  data = event.data;
});

Plotly.plot("data", [{ y: [data], type: "line" }]);

setInterval(() => {
  Plotly.extendTraces("data", { y: [[data]] }, [0]);
}, 200);
