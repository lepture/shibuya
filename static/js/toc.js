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

function addToggleToc () {
  const sublist = document.querySelectorAll(".globaltoc .toctree-l1 ul")
  sublist.forEach(el => {
    const list = el.parentNode
    const link = el.previousSibling
    const title = link.textContent
    const button = document.createElement("button")
    button.innerHTML = '<i class="i-icon chevron"></i>'

    const updateButton = () => {
      if (list.classList.contains("current")) {
        button.setAttribute("arial-label", "Collapse " + title)
      } else {
        button.setAttribute("arial-label", "Expand " + title)
      }
    }
    updateButton()

    const toggleCurrent = (e) => {
      e.preventDefault()
      if (list.classList.contains("current")) {
        list.classList.remove("current")
      } else {
        list.classList.add("current")
      }
      updateButton()
    }

    if (link.getAttribute("href") === "#") {
      link.addEventListener("click", toggleCurrent)
    }
    button.addEventListener("click", toggleCurrent)
    list.insertBefore(button, el)
  })
}

addToggleToc()

window.addEventListener('hashchange', () => {
  handleHash()
}, false)
