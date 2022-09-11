const h2s = document.querySelectorAll('h2')

h2s.forEach(h2 => {
  h2.onclick = el => {
    const icons = [...el.target.children]
    icons.forEach(icon => icon.classList.toggle('hidden'))

    const container = el.target.parentElement.children[1]
    container.classList.toggle('hidden')
  }
})