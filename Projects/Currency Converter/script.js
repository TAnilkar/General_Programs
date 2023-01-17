function dollersToRupees() {
  let usd = document.getElementById("usdInput").value;

  let result = usd * 81.59;

  document.getElementById("result").innerText = "Result: ₹" + result.toFixed(2);
}
