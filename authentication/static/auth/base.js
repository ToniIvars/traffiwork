const inputs = document.querySelectorAll('input:required')
inputs.forEach(inp => {
  const label = inp.labels[0]
  label.classList.toggle('required')
})