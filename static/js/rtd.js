document.addEventListener("readthedocs-addons-data-ready", function (event) {
  document.querySelector(".searchbox input").addEventListener("focusin", () => {
    const event = new CustomEvent("readthedocs-search-show");
    document.dispatchEvent(event);
  });
});
