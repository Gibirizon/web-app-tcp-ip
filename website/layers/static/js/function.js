function display_app_layer(element) {
	fetch("/warstwa/dodaj-opis", {
		method: "POST",
		body: element.value,
	})
		.then(response => response.text())
		.then(data => {
			document.getElementById("desc").innerHTML = data
			document.getElementById("desc").style.display = "block"
			// document.getElementById("desc").classList.add("description")

			// setTimeout(function () {
			// 	content.classList.remove("animate")
			// }, 500)
		})
}

function close_app_layer() {
	// document.getElementById("desc").classList.remove("description")
	document.getElementById("desc").style.display = "none"
}
