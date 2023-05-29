$(document).ready(function() {
    $.ajax({
        url: "/get_data/",
        success: function(data) {
            $.each(data, function(index, item) {
                $('#myTable tbody').append(
                    '<tr>' +
                    '<td>' + item.column1 + '</td>' +
                    '<td>' + item.column2 + '</td>' +
                    '<td>' + item.column3 + '</td>' +
                    '</tr>'
                );
            });
        }
    });
});