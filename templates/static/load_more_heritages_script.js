document.addEventListener('DOMContentLoaded', function() {
    let offset = 0;
    let isLoading = false;
    const heritageList = document.getElementById('heritage-list');

    function loadMoreItems() {
        if (isLoading) return;

        isLoading = true;
        fetch(`/load-more-heritages/?offset=${offset}`)
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    data.forEach(heritage => {
                        const li = document.createElement('li');
                        li.innerHTML = `${heritage.name} <br> ${heritage.location} <br> ${heritage.year_whs} - ${heritage.year_endangered} <br>`;
                        const heritageImage = document.createElement('img');
                        heritageImage.src = '/static/website-stopper.jpg';
                        li.appendChild(heritageImage);
                        heritageList.appendChild(li);
                    });
                    offset += data.length;
                } else {
                    document.getElementById('load-more-button').style.display = 'none';
                }
            })
            .catch(error => console.error('Error loading more heritages:', error))
            .finally(() => {
                isLoading = false;
            });
    }

    window.addEventListener('scroll', function() {
        const scrollPosition = window.scrollY + window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;

        if (scrollPosition >= documentHeight * 0.9) {
            loadMoreItems();
        }
    });

    loadMoreItems();
});
