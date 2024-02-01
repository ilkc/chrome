var port = null;

var getKeys = function(obj){
   var keys = [];
   for(var key in obj){
      keys.push(key);
   }
   return keys;
}

function sendNativeMessage(url) {
  message = url;
  port.postMessage(message);
}

function onNativeMessage(message) {
}

function onDisconnected() {
  port = null;
}

function getCurrenTabUrl(callback){
  var queryInfo = {
      active: true,
      currentWindow: true
  };

  chrome.tabs.query(queryInfo, function(tabs){
      var tab = tabs[0];
      var url = tab.url;
      callback(url);
  });
}

function connect() {
  var hostName = "com.google.chrome.example.echo";
  port = chrome.runtime.connectNative(hostName);
  port.onMessage.addListener(onNativeMessage);
  port.onDisconnect.addListener(onDisconnected);
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function _main(){
  //while (1){}
  //await sleep(3000)
  getCurrenTabUrl(function(url){
      connect();
      sendNativeMessage(url);
      
    });

}


document.addEventListener('DOMContentLoaded', function () {

  _main();


});
  
