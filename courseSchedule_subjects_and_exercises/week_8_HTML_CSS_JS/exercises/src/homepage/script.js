// Wait for DOM to load
document.addEventListener("DOMContentLoaded", function () {
  const button = document.getElementById("alertButton");

  if (button) {
    button.addEventListener("click", function () {
      alert("Hello! Thanks for visiting my homepage! 😊");
    });
  }
});
