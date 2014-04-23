'use strict';

$(document).ready(function () {

  window.mapsCallback = function(){
    $(window).trigger('mapsLoaded');
  };

  $(window).on('hashchange', function () {
    window.scrollTo(window.scrollX, window.scrollY - 50);
  });

  $(window).on('load', function(){
    $(window).on('scroll', function(){
      if ($(window).scrollTop() >= 1000) {
        loadGoogleMaps();
        $(window).off('scroll');
      }
    });
  });

  runSlides();

  function initialize(){
    var myLatLng = new google.maps.LatLng(60.2296837,24.7602503),
      myOptions = {
        zoom: 13,
        center: myLatLng,
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
        position: myLatLng,
        map: map,
        title:'Kotkakuja 3, Espoo, Finland'
      });
  }

  function loadGoogleMaps(){
    var scriptTag = document.createElement('script');
    scriptTag.setAttribute('type','text/javascript');
    scriptTag.setAttribute('src','http://maps.google.com/maps/api/js?sensor=false&callback=mapsCallback');
    (document.getElementsByTagName('head')[0] || document.documentElement).appendChild(scriptTag);
  }

  $(window).bind('mapsLoaded', initialize);

  /**
  * runSlides() find li elements from 'slides' class.
  * Iterate though those elements with changing classes
  * to make visible or invisible blocks.
  *
  */
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

  $('.modal').on('click', '.booking', function() {
    $('.modal').modal('hide');
    location.href = '#contact';
  });

  $('.collapse').on('click', 'a', function() {
    if ($('.navbar-toggle').is(":visible")) {
      $('.navbar-toggle').click();
    }
  });

  /**
  * switchTestimonial() Take two elements as parameters 
  * and switch visible/hidden classes of those elements.
  *
  * @param <Element> element, <Element> element
  *
  */
  function switchTestimonial($blockquote, $nextBlockquote) {
    $blockquote.toggleClass('visible-slide hidden-slide');
    $nextBlockquote.toggleClass('visible-slide hidden-slide');
  }

  $('#testimonial-next').on('click', function(event) {
    var $blockquote = $('blockquote.visible-slide'),
        $nextBlockquote = $blockquote.next('.hidden-slide');

    if (!$nextBlockquote.length) {
      $nextBlockquote = $('blockquote.hidden-slide').first();
    }

    switchTestimonial($blockquote, $nextBlockquote);

    event.preventDefault();
  });

  $('#testimonial-prev').on('click', function(event) {
    var $blockquote = $('blockquote.visible-slide'),
        $nextBlockquote = $blockquote.prev('.hidden-slide');

    if (!$nextBlockquote.length) {
      $nextBlockquote = $('blockquote.hidden-slide').last();
    }

    switchTestimonial($blockquote, $nextBlockquote);

    event.preventDefault();
  });

  $('#contact-form').submit(function(event){
    var waitData = {
      status: 'WAIT',
      messageClass: 'alert-info',
      message: 'Please wait while we validate and send message.'
    };

    ajaxCall('/contact/', $(this).serialize(), function(data) {showMessage(data);}, showMessage);
    showMessage(waitData);
    event.preventDefault();
  });

  $('#info .close').on('click', function() {
    $('#info').addClass('hidden');
  });

  function showMessage(data) {
    var messageHolder = $('#info'),
        messageClass,
        message;

    if (data) {
      if (data.status === 'OK' || data.status === 'WAIT') {
        messageClass = data.messageClass;
        message = data.message;
      }
    } else {
      messageClass = 'alert-danger';
      message = 'Problem with the server. Please contact us directly by mail or phone.'
    }

    messageHolder
      .removeClass('alert-success alert-danger alert-info hidden')
      .addClass(messageClass)
      .find('p')
        .text(message);

    if (data.status === 'OK') {
      $('#contact-form').trigger("reset");
    }

    $('html, body').animate({
        scrollTop: messageHolder.offset().top
    }, 100);
  };
  
  function ajaxCall(targetUrl, payload, onSuccess, onError) {
    $.ajax({
      url: targetUrl,
      data: payload,
      type: 'POST',
      success: function(result) {
        onSuccess(result);
      },
      error: function() {
        if (typeof(onError) === 'undefined') {
          console.log('onError');
        } else {
          onError();
        }
      }
    });
  };

});
