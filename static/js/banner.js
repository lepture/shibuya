const wrapper = document.querySelector('.announcement')
const close = document.querySelector('.announcement-close')

if (wrapper) {
  const style = document.createElement("style")
  document.head.appendChild(style)

  function resize() {
    style.textContent = `:root{--sy-s-banner-height:${wrapper.clientHeight}px}`
  }

  close.addEventListener('click', () => {
    wrapper.parentNode.removeChild(wrapper)
    document.head.removeChild(style)
  })

  resize()
  window.addEventListener("resize", resize)
}
