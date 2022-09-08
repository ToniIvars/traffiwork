const inputs = document.querySelectorAll('input:required')
inputs.forEach(inp => {
  const label = inp.previousElementSibling
  label.classList.toggle('required')
})