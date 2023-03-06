async function fetchGitHubStats (repo) {
  const url = `https://api.github.com/repos/${repo}`
  const resp = await fetch(url)
  const data = await resp.json()
  renderStats(data.watchers, data.forks)
}


function renderStats (stars, forks) {
  localStorage.setItem('_stars', stars)
  localStorage.setItem('_forks', forks)
  localStorage.setItem('_time', Date.now())
  showStats(stars, forks)
}


function showStats (stars, forks) {
  document.querySelector('.js-repo-stars').textContent = stars
  document.querySelector('.js-repo-forks').textContent = forks
}

const element = document.querySelector('.js-repo-stats')

if (element) {
  const stars = localStorage.getItem('_stars')
  const forks = localStorage.getItem('_forks')
  if (stars || forks) {
    showStats(stars, forks)
  }
  const last = localStorage.getItem('_time')
  if (!last || Date.now() - parseInt(last, 10) > 86400000) {
    const user = element.getAttribute('data-user')
    const repo = element.getAttribute('data-repo')
    const type = element.getAttribute('data-type')
    if (type === 'github') {
      fetchGitHubStats(user + '/' + repo)
    }
  }
}
