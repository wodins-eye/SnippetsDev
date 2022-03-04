/* Set the width of the side navigation to 250px and the left margin of the page content to 250px */
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  var dropdown = document.getElementsByClassName("dropbtn");
    var i;

    for (i = 0; i < dropdown.length; i++) {
      dropdown[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var dropdownContent = this.nextElementSibling;
        if (dropdownContent.style.display === "block") {
          dropdownContent.style.display = "none";
        } else {
          dropdownContent.style.display = "block";
        }
      });
    }
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}

function del_children(e) {

    let child = e.lastElementChild;
    while (child) {
        e.removeChild(child);
        child = e.lastElementChild;
    }
}


async  function updateMenu (url, model)  {
  await fetch(url, {
      headers:{
          'Accept': 'application/json',
          'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
      },
  })
  .then(response => {
      return response.json() //Convert response to JSON
  })
  .then(data => {
      const parsed_data = JSON.parse(data);

      const menu = document.getElementById(model)

      del_children(menu)

      for (let i=0; i<parsed_data.length; i++) {
        let item = document.createElement('a')
            item.setAttribute('class', 'menu-item')
            item.setAttribute('href', `/${model}/${parsed_data[i]['fields']['name']}`)

            console.log(parsed_data[i]['fields']['name'])
        item.innerText = `${parsed_data[i]['fields']['name']}`
        menu.appendChild(item)
        //
      }
      //Perform actions with the response data from the view
  })

}

