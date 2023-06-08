function insertCarbon (code, placement) {
  const script = document.createElement('script')
  script.id = "_carbonads_js"
  script.src = `//cdn.carbonads.com/carbon.js?serve=${code}&placement=${placement}`
  const sec0 = document.querySelector('.yue > section')
  const sec1 = document.querySelector('.yue > section > section')
  if (sec1) {
    sec0.insertBefore(script, sec1)
  } else {
    const paragraph = document.querySelector('.yue > section > p')
    if (paragraph) {
      sec0.insertBefore(script, paragraph.nextSibling)
    } else {
      sec0.appendChild(script)
    }
  }
}

const carbon = document.querySelector('.js-carbon')
if (carbon) {
  const code = carbon.getAttribute('data-carbon-code')
  const placement = carbon.getAttribute('data-carbon-placement')
  if (code && placement) {
    insertCarbon(code, placement)
  }
}
