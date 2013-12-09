'use strict';

$(document).ready(function () {

  runSlides();
  loadMap();

  function runSlides() {
    var $slides = $('.slides li'),
        count = $slides.length,
        i = 0,
        pause = 5000;

    var setClasses = function setClasses() {
      $slides
        .eq(i)
          .removeClass('visible-slide');
      $slides
        .eq(i)
          .addClass('hidden-slide');

      if (++i >= count) {
        i = 0;
      }

      $slides
        .eq(i)
          .removeClass('hidden-slide');
      $slides
        .eq(i)
          .addClass('visible-slide');

      setTimeout(setClasses, pause);
    };

    setTimeout(setClasses, pause);

  }

  $('#testimonial-next').on( 'click', function(event) {
    var $blockquote = $('blockquote.visible-slide'),
        $next_blockquote = $blockquote.next('.hidden-slide');

    if (!$next_blockquote.length) {
      $next_blockquote = $('blockquote.hidden-slide').first();
    }

    $blockquote.removeClass('visible-slide');
    $blockquote.addClass('hidden-slide');
    $next_blockquote.removeClass('hidden-slide');
    $next_blockquote.addClass('visible-slide');
    event.preventDefault();
  });

  function loadMap() {
    var myLatlng = new google.maps.LatLng(60.2296837,24.7602503);
        var myOptions = {
          zoom: 13,
          center: myLatlng,
          disableDefaultUI: true,
          panControl: true,
          scrollwheel: false,
          zoomControl: true,
          zoomControlOptions: {
            style: google.maps.ZoomControlStyle.DEFAULT
          },

          mapTypeControl: true,
          mapTypeControlOptions: {
            style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR
          },
          streetViewControl: true,
          mapTypeId: google.maps.MapTypeId.ROADMAP
          },
          map = new google.maps.Map(document.getElementById('map-canvas'), myOptions),
          marker = new google.maps.Marker({
            position: myLatlng,
            map: map,
            title:'Kotkakuja 3, Espoo, Finland'
          });
  }

  function ajaxCall(target_url, payload, onSuccess, onError) {
    $.ajax({
      url: target_url,
      data: payload,
      type: 'POST',
      success: function(result) {
        onSuccess(result);
      },
      error: function(result) {
        if (typeof(onError) == 'undefined') {
          console.log('onError');
        } else {
          onError(result);
        }
      }
    });
}

});