const element = document.querySelector('.js-repo-stats')


async function fetchGitHubStats (user, repo) {
  const url = `https://api.github.com/repos/${user}/${repo}`
  const resp = await fetch(url)
  const data = await resp.json()
  const stats = {stars: data.watchers, forks: data.forks}
  showStats(stats)
  sessionStorage.setItem('_sy/repo/stats', JSON.stringify(stats))
}


async function fetchGitlabStats (user, repo) {
  const url = 'https://gitlab.com/api/v4/projects/' + encodeURIComponent(user + '/' + repo)
  const resp = await fetch(url)
  const data = await resp.json()
  const stats = {stars: data.star_count, forks: data.forks_count}
  showStats(stats)
  sessionStorage.setItem('_sy/repo/stats', JSON.stringify(stats))
}


function showStats ({ stars, forks }) {
  if (stars) {
    document.querySelector('.js-repo-stars').textContent = stars
  }
  if (forks) {
    document.querySelector('.js-repo-forks').textContent = forks
  }
}


function renderStats () {
  const _stats = sessionStorage.getItem('_sy/repo/stats')
  if (_stats) {
    showStats(JSON.parse(_stats))
  } else {
    const user = element.getAttribute('data-user')
    const repo = element.getAttribute('data-repo')
    const type = element.getAttribute('data-type')
    if (type === 'github') {
      fetchGitHubStats(user, repo)
    } else if (type === 'gitlab') {
      fetchGitlabStats(user, repo)
    }
  }
}

if (element) {
  renderStats()
}
