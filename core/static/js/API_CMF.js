$(document).ready(function () {
    // Obtener la fecha actual y la fecha anterior
    var today = new Date();
    var yesterday = new Date(today);
    yesterday.setDate(today.getDate() - 1);

    // Formatear las fechas en YYYY-MM-DD
    var todayFormatted = formatDate(today);
    var yesterdayFormatted = formatDate(yesterday);

    // Hacer la solicitud para obtener el valor del dólar del día actual
    $.ajax({
        url: 'https://api.cmfchile.cl/api-sbifv3/recursos_api/dolar/' + todayFormatted + '?apikey=2935944b579af7458629289c6aef21d1eeba5189&formato=json',
        method: 'GET',
        success: function (response) {
            var dolar = response.Dolares[0].Valor;
            $('#valor-dolar').text(dolar);
        },
        error: function (error) {
            // Si hay un error, hacer una solicitud para obtener el valor del dólar del día anterior
            $.ajax({
                url: 'https://api.cmfchile.cl/api-sbifv3/recursos_api/dolar/' + yesterdayFormatted + '?apikey=2935944b579af7458629289c6aef21d1eeba5189&formato=json',
                method: 'GET',
                success: function (response) {
                    var dolar = response.Dolares[0].Valor;
                    $('#valor-dolar').text(dolar);
                },
                error: function (error) {
                    console.log('Error al obtener el valor del dólar');
                }
            });
        }
    });

    // Función para formatear las fechas en YYYY-MM-DD
    function formatDate(date) {
        var year = date.getFullYear();
        var month = ('0' + (date.getMonth() + 1)).slice(-2);
        var day = ('0' + date.getDate()).slice(-2);
        return year + '/' + month + '/dias/' + day;
    }
});
