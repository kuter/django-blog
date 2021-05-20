$(document).ready(function(){
    $( "tbody" ).sortable({
        items: "tr.form-row",
        stop: function () {
            var inputs = $('tr[class^="form-row-"]:not(#set-empty)')
            var nbElems = inputs.length;
            $('input[id$="-order"]').each(function(idx) {
                position = idx + 1;
                $(this).val(position);
                $(this).parent().prev().find('p').html(position);
            });}
    });
    $( "tbody" ).sortable( "serialize", { key: "sort" } );
});
