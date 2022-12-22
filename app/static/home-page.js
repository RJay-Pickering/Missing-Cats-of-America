var btn = document.querySelectorAll( '.btn-front-1' );

var btnFront
var btnYes
var btnNo

for (let i = 0; i < btn.length; i++) {
  btnFront = btn[i].querySelector( '.btn-front' ),
  btnYes = btn[i].querySelector( '.btn-back .yes' ),
  btnNo = btn[i].querySelector( '.btn-back .no' );

  btnFront.addEventListener( 'click', function( event ) {
    var mx = event.clientX - btn[i].offsetLeft,
        my = event.clientY - btn[i].offsetTop;

    var w = btn[i].offsetWidth,
        h = btn[i].offsetHeight;
    
    var directions = [
      { id: 'top', x: w/2, y: 0 },
      { id: 'right', x: w, y: h/2 },
      { id: 'bottom', x: w/2, y: h },
      { id: 'left', x: 0, y: h/2 }
    ];
    
    directions.sort( function( a, b ) {
      return distance( mx, my, a.x, a.y ) - distance( mx, my, b.x, b.y );
    } );
    
    btn[i].setAttribute( 'data-direction', directions.shift().id );
    btn[i].classList.add( 'is-open' );

  } );

  btnYes.addEventListener( 'click', function( event ) {	
    btn[i].classList.remove( 'is-open' );
  } );
  
  btnNo.addEventListener( 'click', function( event ) {
    btn[i].classList.remove( 'is-open' );
  } );
}

function distance( x1, y1, x2, y2 ) {
  var dx = x1-x2;
  var dy = y1-y2;
  return Math.sqrt( dx*dx + dy*dy );
}