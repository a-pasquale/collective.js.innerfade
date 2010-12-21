jq(document).ready(function() {

    var options = {
        speed: 'slow',
        timeout: '2000',
        containerheight: 279,
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
        }//,

        // hover out
        //function() {
        //    id = jq(this).parent().attr('id').substr(5);
        //    
        //    options['first_slide'] = id;
        //    jq('#Innerfade').innerFadeUnbind();
        //   jq('#Innerfade').innerFade(options);
        //}
    );
});