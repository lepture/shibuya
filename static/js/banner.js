const close = document.querySelector('.banner-close')

if (close) {
  close.addEventListener('click', () => {
    const banner = document.querySelector('.banner')
    banner.parentNode.removeChild(banner)
  })
}
