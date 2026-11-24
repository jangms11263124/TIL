// DOM Elements
const searchInput = document.querySelector('.search-box__input')
const searchButton = document.querySelector('.search-box__button')
const searchResult = document.querySelector('.search-result')
const loadingList = document.querySelector('.search-result--loadingList')

// API Configurations
const LIMIT = 10
const API_KEY = 'YOUR_API_KEY'
const BASE_URL = 'https://ws.audioscrobbler.com/2.0/'

// Application State
let page = 1
let keyword = ''
let isLoading = false
let isEnd = false

// Sentinel element for infinite scroll
const sentinel = document.createElement('div')
sentinel.id = 'sentinel'

// Infinite Scroll Observer
const observer = new IntersectionObserver(([entry]) => {
  if (entry.isIntersecting && !isLoading && !isEnd && keyword) {
    page++
    fetchAlbums()
  }
})

// Event Listeners
searchButton.addEventListener('click', () => startNewSearch())
searchInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') startNewSearch()
})

// Reset state and start a new search
function startNewSearch() {
  const trimmed = searchInput.value.trim()
  if (!trimmed) {
    alert('검색어를 입력해주세요.')
    return
  }

  keyword = trimmed
  page = 1
  isEnd = false
  searchResult.innerHTML = ''

  observer.unobserve(sentinel)
  sentinel.remove()

  fetchAlbums()
}

// Fetch albums from Last.fm API
async function fetchAlbums() {
  if (isLoading || isEnd) return

  isLoading = true
  loadingList.style.display = 'block' // API 요청 시 로더 활성화

  const params = {
    method: 'album.search',
    api_key: API_KEY,
    album: keyword,
    page: page,
    limit: LIMIT,
    format: 'json',
  }

  try {
    const res = await axios.get(BASE_URL, { params })
    const albums = res.data?.results?.albummatches?.album
    const albumList = Array.isArray(albums) ? albums : (albums ? [albums] : [])
    const totalResults = Number(res.data?.results?.['opensearch:totalResults']) || 0

    if (albumList.length > 0) {
      appendAlbumCards(albumList)
    } else if (page === 1) {
      // First page with no results
      searchResult.innerHTML = `<p class="search-result--no-result" style="text-align: center; color: #6B7280; padding: 24px 0;">검색 결과가 없습니다.</p>`
    }

    // Check if we reached the end of search results
    if (page * LIMIT >= totalResults || albumList.length < LIMIT) {
      isEnd = true
      observer.unobserve(sentinel)
      sentinel.remove()
    } else {
      // Append sentinel to detect next scroll
      searchResult.appendChild(sentinel)
      observer.observe(sentinel)
    }
  } catch (error) {
    console.error('앨범 정보를 불러오는 데 실패했습니다:', error)
  } finally {
    isLoading = false
    loadingList.style.display = 'none' // API 응답 성공/실패 시 로더 비활성화
  }
}

// Render album card lists
function appendAlbumCards(albums) {
  const fragment = document.createDocumentFragment()

  albums.forEach((album) => {
    const card = document.createElement('div')
    card.className = 'search-result__card'

    const imgUrl = album.image?.[1]?.['#text'] || 'assets/logo.png'
    const artist = album.artist || 'Unknown Artist'
    const name = album.name || 'Unknown Album'

    card.innerHTML = `
      <img src="${imgUrl}" alt="${name}" width="64" height="64">
      <div>
        <h2>${artist}</h2>
        <p>${name}</p>
      </div>
    `

    card.addEventListener('click', () => {
      if (album.url) {
        window.open(album.url, '_blank')
      }
    })

    fragment.appendChild(card)
  })

  searchResult.appendChild(fragment)
}
