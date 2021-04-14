$(function () {

    "use strict";

    //===== Prealoder

    $(window).on('load', function (event) {
        $('.preloader').delay(500).fadeOut(500);
    });



    //===== Sticky

    $(window).on('scroll', function (event) {
        var scroll = $(window).scrollTop();
        if (scroll < 20) {
            $(".navbar-area").removeClass("sticky");
        } else {
            $(".navbar-area").addClass("sticky");
        }
    });


        $(window).on('scroll', function (event) {
        var scroll = $(window).scrollTop();
        var x = document.getElementById("sticky_footer");
        if (scroll < 20) {
            x.style.visibility = "hidden";
            $(".navbar-area").removeClass("sticky");
        } else {
            x.style.visibility = "visible";
            $(".navbar-area").addClass("sticky");
        }
    });


    //===== Section Menu Active

    // var scrollLink = $('.page-scroll');
    // // Active link switching
    // $(window).scroll(function () {
    //     var scrollbarLocation = $(this).scrollTop();

    //     scrollLink.each(function () {

    //         var sectionOffset = $(this.hash).offset().top - 73;

    //         if (sectionOffset <= scrollbarLocation) {
    //             $(this).parent().addClass('active');
    //             $(this).parent().siblings().removeClass('active');
    //         }
    //     });
    // });


    //===== close navbar-collapse when a  clicked

    $(".navbar-nav a").on('click', function () {
        $(".navbar-collapse").removeClass("show");
    });

    $(".navbar-toggler").on('click', function () {
        $(this).toggleClass("active");
    });

    $(".navbar-nav a").on('click', function () {
        $(".navbar-toggler").removeClass('active');
    });




    //===== Back to top

    // Show or hide the sticky footer button
    $(window).on('scroll', function (event) {
        if ($(this).scrollTop() > 600) {
            $('.back-to-top').fadeIn(200)
        } else {
            $('.back-to-top').fadeOut(200)
        }
    });


    //Animate the scroll to yop
    $('.back-to-top').on('click', function (event) {
        event.preventDefault();

        $('html, body').animate({
            scrollTop: 0,
        }, 1500);
    });


    //===== Svg

    jQuery('img.svg').each(function () {
        var $img = jQuery(this);
        var imgID = $img.attr('id');
        var imgClass = $img.attr('class');
        var imgURL = $img.attr('src');

        jQuery.get(imgURL, function (data) {
            // Get the SVG tag, ignore the rest
            var $svg = jQuery(data).find('svg');

            // Add replaced image's ID to the new SVG
            if (typeof imgID !== 'undefined') {
                $svg = $svg.attr('id', imgID);
            }
            // Add replaced image's classes to the new SVG
            if (typeof imgClass !== 'undefined') {
                $svg = $svg.attr('class', imgClass + ' replaced-svg');
            }

            // Remove any invalid XML tags as per http://validator.w3.org
            $svg = $svg.removeAttr('xmlns:a');

            // Replace image with new SVG
            $img.replaceWith($svg);

        }, 'xml');

    });

    //
    var $thank = $('#thankyouModal');

    // Listen for modal hide and popstate events.
    function startListening() {
        $thank.on('hide.bs.modal', onModalHide);
        $(window).on('popstate', onPopState);
    }

    // Stop listening for modal hide and popstate events.
    function stopListening() {
        $thank.off('hide.bs.modal', onModalHide);
        $(window).off('popstate', onPopState);
    }

    // Modal opens.
    // Add event listeners and push state.
    function onModalShow() {
        startListening();
        window.history.pushState({}, '', 'submit-success');
    }

    // Modal hides.
    // Remove event listeners and go back.
    function onModalHide() {
        stopListening();
        window.history.back();
    }

    // Navigation occurs.
    // Remove event listeners and hide modal.
    function onPopState() {
        stopListening();
        $thank.modal('hide');
    }

    // Listen for when the modal shows.
    $thank.on('show.bs.modal', onModalShow);


    //=====  WOW active

    new WOW().init();





});


