document.addEventListener('DOMContentLoaded', function() {
    let offset = 0;
    let isLoading = false; // Переменная для отслеживания состояния загрузки
    const heritageList = document.getElementById('heritage-list');

    // Функция для загрузки дополнительных элементов
    function loadMoreItems() {
        if (isLoading) return; // Если уже идет загрузка, прекратить выполнение

        isLoading = true; // Устанавливаем флаг загрузки
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
                    // Если больше элементов нет, скрываем кнопку
                    document.getElementById('load-more-button').style.display = 'none';
                }
            })
            .catch(error => console.error('Error loading more heritages:', error))
            .finally(() => {
                isLoading = false; // Сбрасываем флаг загрузки после завершения запроса
            });
    }

    // Обработчик события scroll для загрузки при достижении нижней части страницы
    window.addEventListener('scroll', function() {
        const scrollPosition = window.scrollY + window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;

        if (scrollPosition >= documentHeight * 0.9) {
            loadMoreItems();
        }
    });

    // Инициализация загрузки при загрузке страницы
    loadMoreItems();
});
