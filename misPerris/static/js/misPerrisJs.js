$('.modalUp').click(function(){
	$('#perrite').html("<img class='logo' src='"+$(this).children().attr("src")+"'/>");
	var nombre = $(this).children().attr("src").replace("/static/img/rescatados/","");
	$('#perriteName').html("Nombre: " + nombre.replace(".jpg",""));
	console.log(nombre);

	if(nombre === 'Oso.jpg'){
		$('#breveResena').html("Este perrito es muy bonito y super calmado, por lo que es perfecto para niños. Es muy jugueton durante todo el dia y cuenta con un largo pelaje.");
	}else if(nombre === 'Maya.jpg'){
		$('#breveResena').html("Este perrito es demasiado tierno, pero te seguira a donde vayas. Perro perfecto de compañia para adultos mayores o personas que necesitan un compañero.");
	}else if(nombre === 'Wifi.jpg'){
		$('#breveResena').html("Este perrito es un travieso y nunca parara de jugar. Solo busca recibir y dar amor mediante juegos.");
	}else if(nombre === 'Chocolate.jpg'){
		$('#breveResena').html("Este gran y elegante perro es perfecto para ser el proximo guardian de tu hogar, un temperamento perfecto para estar cerca de niños y para cuidar la casa. Perro de tamaño grande.");
	}else if(nombre === 'Pexel.jpg'){
		$('#breveResena').html("Este pequeñin es un jugueton por naturaleza, ya que puede correr todo el dia sin parar. Este chico alegrara tus salidas a los parques y a toda tu familia. Pelaje enorme.");
	}else if(nombre === 'Bigotes.jpg'){
		$('#breveResena').html("Este muchacho es demasiado timido, leal y jugador. No te dejes engañar por su tamaño, ya que no dañaria ni ha una mosca.");
	}else if(nombre === 'Luna.jpg'){
		$('#breveResena').html("Este cachorro no tiene mas de 3 meses y necesita una familia para comenzar su vida. Tiene todas sus vacunas y listo para la insercion en tu hogar.");
	}else{
		$('#breveResena').html("Animal ingresado no encontrado 404 error");
	}
})
