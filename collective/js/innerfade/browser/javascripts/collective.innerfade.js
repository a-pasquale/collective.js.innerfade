jq(document).ready(function() {

    var options = {
        speed: 'slow',
        timeout: '5000',
        containerheight: 271,
        animationtype: 'fade',
        type: 'sequence'
    }

    jq('#Innerfade').innerFade(options);

    jq(".ifnav img").hover(

        // hover
        function() {
            id = jq(this).parent().attr('id').substr(5);
            
            jq('#Innerfade').innerFadeUnbind();
            jq('#Innerfade').innerFadeTo(id);
        }
    );
});