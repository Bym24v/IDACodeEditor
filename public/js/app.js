var btn = document.getElementById("send-btn");

// Stop Crtl-s
$(document).bind('keydown', function(e) {
    if(e.ctrlKey && (e.which == 83)) {
      e.preventDefault();
      //alert('Ctrl+S');
      return false;
    }
  });


// btn send
btn.addEventListener("click", function(){

    // Start WebSocket
    var ws = new WebSocket("ws://127.0.0.1:8000/ws");

    ws.onopen = function(){
    ws.send(editor.getValue());
    ws.close();

    //console.log("send...");
    }

    ws.onmessage = function(data){
        //console.log("message")
    }

    ws.onclose = function(){
        //console.log("close")

        ws.close();
    }

    
})