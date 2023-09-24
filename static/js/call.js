function myfun(){
  host = document.getElementById('host').value
  alert(host)
  // window.prompt("something", "");
  pywebview.api.main(host);
}


function insert_db(){
  host = document.getElementById('save_host').value
  alert(host)
  // window.prompt("something", "");
  pywebview.api.db(host);
}




