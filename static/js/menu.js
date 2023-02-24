function toggleMenu(button) {
  const id = button.getAttribute('aria-controls')
  const ctrl = document.getElementById(id)
  const expanded = 'data-expanded-' + id
  button.addEventListener('click', function () {
    if (document.body.hasAttribute(expanded)) {
      document.body.removeAttribute(expanded)
      ctrl.classList.remove('_expanded')
      setButtonExpanded(id, 'false')
    } else {
      document.body.setAttribute(expanded, "true")
      ctrl.classList.add('_expanded')
      setButtonExpanded(id, 'true')
    }
  })
}

function setButtonExpanded(id, value) {
  const els = document.querySelectorAll('[aria-controls="' + id + '"]')
  for (el of els) {
    el.setAttribute('aria-expanded', value)
  }
}

const menuButtons = document.querySelectorAll('.js-menu')
for (let i = 0; i < menuButtons.length; i++) {
  toggleMenu(menuButtons[i])
}
