// Ambil elemen tombol dan popup
var openPopupBtn = document.getElementById("masukBtn");
var popup = document.getElementById("popup-form");

// Ketika tombol dibuka, tampilkan popup
openPopupBtn.addEventListener("click", function () {
  popup.style.display = "block";
});

// Ketika tombol close di klik, sembunyikan popup
popup.querySelector(".close").addEventListener("click", function () {
  popup.style.display = "none";
});

// Jika pengguna mengklik di luar popup, sembunyikan juga
window.addEventListener("click", function (event) {
  if (event.target == popup) {
    popup.style.display = "none";
  }
});

fetch("products.json")
  .then(function (response) {
    return response.json();
  })

  .then(function (product) {
    let placeholder = document.querySelectorAll("#listProduct");
    let out = "";
    for (let product of products) {
      out += `
  <div class="image">
  <img src="${info.image}">
</div>
<div class="name">
<p>${info.name}</p>
</div>
<div>
<p>Rp ${info.price}</p>
</div>
<div class="quantity">
  <span class="minus">-</span>
  <span>${item.quantity}</span>
  <span class="plus">+</span>
</div>
<div class="totalPrice">Rp${info.price * item.quantity}</div>
`;
    }
  });
