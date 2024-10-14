const searchBoxStyle = `
:host > div .results .hit h2 {
  color: var(--sy-c-heading);
  margin-bottom: 0;
  border-bottom: 0;
  font-weight: 600;
}
:host > div .results .hit .hit-block .content {
  color: var(--sy-c-text);
}
:host > div .results .hit-block a.hit:hover, :host > div .results .hit-block .hit.active {
  background-color: var(--gray-5);
  border-radius: 4px;
}

:host > div div.hit-block a.hit-block-heading:hover {
  text-decoration: underline;
}

:host > div div.hit-block a.hit-block-heading i,
:host > div div.hit-block .hit-block-heading-container .close-icon {
  color: var(--sy-c-light);
  margin-bottom: 0;
  display: flex;
}
`

document.addEventListener("readthedocs-addons-data-ready", function (event) {
  document.querySelector(".searchbox input").addEventListener("focusin", () => {
    const event = new CustomEvent("readthedocs-search-show")
    document.dispatchEvent(event)
  })
  setTimeout(() => {
    const rtdSearchElement = document.querySelector("readthedocs-search")
    if (rtdSearchElement) {
      const style = document.createElement('style')
      style.textContent = searchBoxStyle
      rtdSearchElement.shadowRoot.appendChild(style)
    }
  }, 1000)
});
