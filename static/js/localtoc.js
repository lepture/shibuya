function handleHash () {
  const selector = '.localtoc a[href="' + location.hash + '"]'
  const el = document.querySelector(selector);
  if (el) {
    const lis = document.querySelectorAll('.localtoc li')
    lis.forEach(li => {
      li.classList.remove('active')
    })
    el.parentNode.classList.add('active')
  }
}

handleHash()

window.addEventListener('hashchange', () => {
  handleHash()
}, false)
