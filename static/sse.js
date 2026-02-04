const evtSource = new EventSource("/sse/run/");

evtSource.onmessage = (event) => {
  const newElement = document.createElement("li");
  parsed = JSON.parse(event.data)
  
  newElement.textContent = parsed?.value ;

  const eventContainer = document.getElementById("sse-container");
  eventContainer.appendChild(newElement);
};

evtSource.addEventListener("done", () => {
  evtSource.close();
});
