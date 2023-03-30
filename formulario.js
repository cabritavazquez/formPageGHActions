const form = document.querySelector('form');
form.addEventListener('submit', handleSubmit);

async function handleSubmit(event) {
	event.preventDefault(); // previene el comportamiento por defecto del formulario
	
	const nombre = document.getElementById('nombre').value;
	const apellidos = document.getElementById('apellidos').value;
	const direccion = document.getElementById('direccion').value;
	
	const body = {
		nombre: nombre,
		apellidos: apellidos,
		direccion: direccion
	};

	try {
		const response = await fetch('https://api.github.com/repos/cabritavazquez/formPageGHActions/dispatches', {
			method: 'POST',
			headers: {
				'Authorization': 'token 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',
				'Accept': 'application/vnd.github.everest-preview+json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(body)
		});

		if (!response.ok) {
			throw new Error('Hubo un error al enviar los datos del formulario.');
		}

		alert('Los datos del formulario se enviaron correctamente.');
	} catch (error) {
		console.error(error);
		alert('Hubo un error al enviar los datos del formulario.');
	}
}
