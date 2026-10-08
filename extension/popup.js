const input = document.getElementById("wordInput")
const results = document.getElementById("results")

async function searchWord(word){

results.innerHTML = "Searching..."

try{

let response = await fetch(
"https://api.dictionaryapi.dev/api/v2/entries/en/" + encodeURIComponent(word)
)

let data = await response.json()

results.innerHTML = ""

if(data.title){

results.innerHTML = "No definition found"

return

}

let entry = data[0]

let wordTitle = document.createElement("h3")
wordTitle.textContent = entry.word

results.appendChild(wordTitle)

entry.meanings.forEach(m => {

let part = document.createElement("b")
part.textContent = m.partOfSpeech

results.appendChild(part)

m.definitions.forEach(d => {

let def = document.createElement("div")
def.textContent = "- " + d.definition

results.appendChild(def)

})

})

}catch(err){

results.innerHTML = "Error fetching definition"

}

}

document.getElementById("searchBtn").onclick = () => {

let word = input.value.trim()

if(word){
searchWord(word)
}

}

input.addEventListener("keypress", e => {

if(e.key === "Enter"){

let word = input.value.trim()

if(word){
searchWord(word)
}

}

})
