const factDisplayer = document.getElementById("displayer");
const factType = document.getElementById("factType");
const generateButton = document.getElementById("generateBtn");
const copyButton = document.getElementById("copyBtn");

const API_URL = "";

function displayFact(fact) {
  factDisplayer.innerText = fact;
  return;
}

function generateFact() {
  generateButton.disabled = true;
  copyButton.disabled = true;

  let type = factType.value;

  fetch(`${API_URL}/${type}`)
    .then(response => {
      
      if (!response.ok) {
        throw new Error("Something went wrong!. " + response.status);
      }

      return response.json();
    })
    .then(fact => {
      let factTitlte = fact["Title"];

      displayFact(factTitlte);

      setTimeout( () => {
        generateButton.disabled = false;
        copyButton.disabled = false;
      }, 600 )
    })
    .catch(error => {
      generateButton.disabled = false;
      copyButton.disabled = false;
      
      console.error(error);
      displayFact("Try Again!");
    })
}

generateButton.addEventListener("click", generateFact);
copyButton.addEventListener("click", () => {
  navigator.clipboard.writeText("Did you really think it would work?");
})