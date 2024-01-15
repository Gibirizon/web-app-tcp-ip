function delete_question(element) {
	fetch("/quiz/dodaj-pytanie", {
		method: "POST",
		body: element,
	})
}
