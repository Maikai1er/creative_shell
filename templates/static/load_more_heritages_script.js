document.addEventListener('DOMContentLoaded', function() {
    let offset = 0;
    const loadMoreButton = document.getElementById('load-more-button');
    const heritageList = document.getElementById('heritage-list');

    loadMoreButton.addEventListener('click', function() {
        console.log('Offset before fetch:', offset);
        fetch(`/load-more-heritages/?offset=${offset}`)
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    data.forEach(heritage => {
                        const li = document.createElement('li');
                        li.textContent = `${heritage.name} - ${heritage.location}`;
                        heritageList.appendChild(li);
                    });
                    offset += data.length;
                } else {
                    loadMoreButton.style.display = 'none';
                }
            })
            .catch(error => console.error('Error loading more heritages:', error));
    });
});
