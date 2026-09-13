document.addEventListener("DOMContentLoaded", function () {
   const closeButtons = document.querySelectorAll(".custom-close");
   closeButtons.forEach(function (button) {
      button.addEventListener("click", function () {
         const message = this.closest(".custom-message");
         message.classList.add("hide-message");
         setTimeout(function () {
            message.remove();
         }, 400);
      });
   });

});