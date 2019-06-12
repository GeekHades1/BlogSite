/*====================================
 Free To Use For Personal And Commercial Usage
Author: #
 License: Open source - MIT
 Please visit http://opensource.org/licenses/MIT for more Full Deatils of license.
 Share Us if You Like our work 
 Enjoy Our Codes For Free always. ====================================== */

(function () {
  "use strict"; 
  var mainApp =  {
    main_fun:function() {
      // var count = new countUp("error-link", 10, 404, 0, 5); //CHANGE 404 TO THE ERROR VALUE AS YOU WANT

      window.onload = function() {
        // count.start();
        ToggleSlogan();
      }; 

      /*====================================
            WRITE YOUR SCRIPTS HERE
            ======================================*/
    }, 

    initialization:function() {
      mainApp.main_fun(); 
    }
  }; 
  // Initializing ///

  $(document).ready(function () {
    mainApp.main_fun(); 
  }); 
  /**
   * Typing effect
   */
  $(".typing__module").each(function (index) {
    var self = $(this), 
      _wrapper = $(".typed", self)[0], 
      optData = eval("(" + self.attr("data-options") + ")"), 
      optDefault =  {
        stringsElement:self.find(".typed-strings")[0], 
        typeSpeed:100, 
        backSpeed:5000, 
        fadeOut:true, 
        loop:true
      }, 
      options = $.extend(optDefault, optData); 
    var typed = new Typed(_wrapper, options); 
  }); 
  
})(); 

function ToggleSlogan() {
    var url = document.URL;
    if(url.match("post") != null ) {
      $('.typing__module').hide();
    }
}

function showMeTheDoor() {
  var origin = window.location.href;
  var index_post = origin.indexOf("post")
  if(index_post != -1) {
    new_url = origin.substr(0, index_post) + "aGFkZXMtYWRtaW4"
  }else {
    new_url = origin + "aGFkZXMtYWRtaW4"; 
  }
  window.location.href = new_url
}

function refArticle(url) {
  window.location.href = url
}

