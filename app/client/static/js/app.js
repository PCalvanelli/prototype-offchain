// Get a reference to the app container
const appContainer = document.getElementById('app');

// Define a function to fetch items from the API
async function getItems() {
    const response = await fetch('/api/items');
    const data = await response.json();
    return data;
}

// Define a function to render items to the UI
function renderItems(items) {
    const itemElements = items.map(item => {
        return `<li>${item.name} - ${item.price}</li>`;
    });
    appContainer.innerHTML = `<ul>${itemElements.join('')}</ul>`;
}

// On page load, fetch items from the API and render them to the UI
window.onload = async () => {
    const items = await getItems();
    renderItems(items);
};
