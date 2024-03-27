// Fungsi untuk membuka pop-up
function openPopup(type) {
  $("#" + type + "Popup").show();
  $("#overlay").show();
}

// Fungsi untuk menutup pop-up
function closePopup() {
  $(".popup").hide();
  $("#overlay").hide();
}

// Ajax untuk login
$("#loginForm").submit(function (event) {
  event.preventDefault();
  $.ajax({
    type: "POST",
    url: "login.php",
    data: $(this).serialize(),
    success: function (response) {
      // Handle response
      console.log(response);
    },
    error: function () {
      // Handle error
      console.error("Login failed");
    },
  });
});

// Ajax untuk sign up
$("#signupForm").submit(function (event) {
  event.preventDefault();
  $.ajax({
    type: "POST",
    url: "signup.php",
    data: $(this).serialize(),
    success: function (response) {
      // Handle response
      console.log(response);
    },
    error: function () {
      // Handle error
      console.error("Sign up failed");
    },
  });
});
