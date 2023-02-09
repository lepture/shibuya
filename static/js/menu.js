function toggleMenu(button) {
  const id = button.getAttribute('aria-controls')
  const ctrl = document.getElementById(id)
  button.addEventListener('click', function () {
    if (button.getAttribute('aria-expanded') === 'false') {
      button.setAttribute('aria-expanded', 'true')
      ctrl.classList.add('_expanded')
      document.body.setAttribute('data-expanded-' + id, 'true')
    } else {
      button.setAttribute('aria-expanded', 'false')
      ctrl.classList.remove('_expanded')
      document.body.removeAttribute('data-expanded-' + id)
    }
  })
}

const menuButtons = document.querySelectorAll('.js-menu')
for (let i = 0; i < menuButtons.length; i++) {
  toggleMenu(menuButtons[i])
}
