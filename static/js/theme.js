const COLOR_MODES = ['auto', 'light', 'dark']
let index = COLOR_MODES.indexOf(sessionStorage['_theme'] || 'auto')

const el = document.querySelector('.js-theme')

function rotateColorMode () {
  index += 1
  if (!COLOR_MODES[index]) {
    index = 0
  }
  const mode = COLOR_MODES[index]
  setColorMode(mode)
  sessionStorage['_theme'] = mode
  updateLabel(mode)
}

function updateLabel (mode) {
  const label = el.getAttribute('data-aria-' + mode)
  el.setAttribute('aria-label', label)
}

if (el) {
  el.addEventListener('click', rotateColorMode)
  updateLabel(COLOR_MODES[index] || 'auto')
}
