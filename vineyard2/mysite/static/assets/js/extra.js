
window.onerror = function(message, url, line, column, error) {
  console.error("Error:", message, "URL:", url, "Line:", line, "Column:", column, "Error object:", error);
};



// select all elements with class "my-class"
const elements = document.querySelectorAll('.show-fields-btn');

// loop through the selected elements and add an event listener to each one
elements.forEach(element => {
  element.addEventListener('click', function(event) {
    // handle the click event here
    console.log('Clicked element:', element);
  });
});