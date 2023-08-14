// Get all elements with the class "mb-text"
var mbTextElements = document.querySelectorAll('.maxbutton');

// Iterate through each element and modify its classes
mbTextElements.forEach(function(element, index) {
    element.style.margin = '10px'
    if (index % 2 === 0) {
      // Even index, add classes "btn" and "btn-success"
      element.classList.add('btn', 'btn-success');
    } else {
      // Odd index, add classes "btn" and "btn-primary"
      element.classList.add('btn', 'btn-primary');
    }
  });

// Get all <p> elements
var pElements = document.querySelectorAll('p');

// Iterate through each <p> element
pElements.forEach(function (pElement) {
    // Check if the innerHTML contains the text "Note:" or if it's empty
    if (pElement.innerHTML.includes('Note:') || pElement.innerHTML.trim() === '') {
        // Remove the <p> element
        pElement.remove();
    }
});
// Select the <div> element with class "gridlove-author"
var divElement = document.querySelector('.gridlove-author');
var pe = document.querySelector('.gridlove-prev-next-nav')
pe.remove()


// Remove the entire <div> element from the DOM
divElement.remove();
window.onscroll = function () { myFunction() };

var navbar_sticky = document.getElementById("navbar_sticky");
var sticky = navbar_sticky.offsetTop;
var navbar_height = document.querySelector('.navbar').offsetHeight;

function myFunction() {
    if (window.pageYOffset >= sticky + navbar_height) {
        navbar_sticky.classList.add("sticky")
        document.body.style.paddingTop = navbar_height + 'px';
    } else {
        navbar_sticky.classList.remove("sticky");
        document.body.style.paddingTop = '0'
    }
}
