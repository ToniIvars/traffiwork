const h2s = document.querySelectorAll('h2')
const sharingButtons = document.querySelectorAll('button[data-link]')

h2s.forEach(h2 => {
  h2.onclick = el => {
    const icons = [...el.target.children]
    icons.forEach(icon => icon.classList.toggle('hidden'))

    const container = el.target.parentElement.children[1]
    container.classList.toggle('hidden')
  }
})

sharingButtons.forEach(btn => btn.onclick = ev => {
  const button = ev.currentTarget
  const link = button.dataset.link
  navigator.clipboard.writeText(window.location.origin + link)

  button.children[0].classList.toggle('hidden')

  setTimeout(() => {
    button.children[0].classList.toggle('hidden')
  }, 2000);
})