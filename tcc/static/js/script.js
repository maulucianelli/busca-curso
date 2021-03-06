var el = document.querySelector('.tabs');
//callAPI("https://limitless-shore-04114.herokuapp.com/https://api.educamaisbrasil.com.br/api/Curso/ConsultarSalarioPorteCargo?cursoUrl=administracao", function(response){showSalary(response)});

function b64convert( str ) {
    return decodeURIComponent(escape(window.atob( str )));
}
function callAPI(code, callback) {
    url = "https://limitless-shore-04114.herokuapp.com/https://api.educamaisbrasil.com.br/api/Curso/ConsultarSalarioPorteCargo?cursoUrl=" + code
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.responseType = 'json';
    xhr.onload = function(){
        if(xhr.status === 200){
            callback(xhr.response)
        }else{
            console.log("Erro ao acessar a API")
            return 0;
        }
    }
    xhr.send();
    return 1;
}

function showSalary(response){
    if(response.length>0){
        document.getElementById("salario_junior").innerText = "R$" + response[1].SALARIO_TRAINEE
        document.getElementById("salario_pleno").innerText = "R$" + response[1].SALARIO_PLENO
        document.getElementById("salario_senior").innerText = "R$" + response[1].SALARIO_SENIOR
    }
    else{
        document.getElementById("salario_pleno").innerHTML = "<h5>Informação de Salário Indisponível</h5>"
    }
}
var $rows = $('#table tr');
$('#search').keyup(function() {
    var val = $.trim($(this).val()).replace(/ +/g, ' ').toLowerCase();
    
    $rows.show().filter(function() {
        var text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
        return !~text.indexOf(val);
    }).hide();
});

function searchArticles() {
  search('searchArticles', 'articles');
}
  
function search(searchInput, searchTable) {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById(searchInput);
  filter = input.value.toUpperCase();
  table = document.getElementById(searchTable);
  tr = table.getElementsByTagName("tr");
  
  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
          txtValue = td.textContent || td.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
              tr[i].style.display = "";
          } else {
              tr[i].style.display = "none";
          }
      }
  }
}