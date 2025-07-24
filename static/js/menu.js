/**
 * @param {HTMLButtonElement} button
 */
function bindButtonEvent(button) {
  const id = button.getAttribute('aria-controls')
  const content = document.getElementById(id)
  if (!content) return

  content.addEventListener('click', (e) => {
    e.stopPropagation()
  })

  button.addEventListener('click', (e) => {
    e.stopPropagation()

    const components = getExpandedComponents()
    const index = components.indexOf(id)
    if (content.getAttribute('aria-hidden') === 'false') {
      components.splice(index, 1)
      document.body.setAttribute('data-expanded', components.join(' '))
      content.setAttribute('aria-hidden', 'true')
      setButtonExpanded(id, 'false')
    } else {
      components.push(id)
      document.body.setAttribute('data-expanded', components.join(' '))
      content.setAttribute('aria-hidden', 'false')
      setButtonExpanded(id, 'true')
    }
  })
}

/**
 * @param {string} id
 * @param {string} value
 */
function setButtonExpanded(id, value) {
  const els = document.querySelectorAll('[aria-controls="' + id + '"]')
  for (let i = 0; i < els.length; i++) {
    els[i].setAttribute('aria-expanded', value)
  }
}

function getExpandedComponents() {
  const expanded = document.body.getAttribute('data-expanded') || ''
  if (!expanded.trim()) {
    return []
  }
  return expanded.split(/\s+/)
}

/** @type {NodeListOf<HTMLButtonElement>} */
const menuButtons = document.querySelectorAll('.js-menu')
for (let i = 0; i < menuButtons.length; i++) {
  bindButtonEvent(menuButtons[i])
}

document.body.addEventListener('click', () => {
  const components = getExpandedComponents()
  document.body.setAttribute('data-expanded', '')
  components.forEach((id) => {
    const content = document.getElementById(id)
    content.setAttribute('aria-hidden', 'true')
    setButtonExpanded(id, 'false')
  })
})
