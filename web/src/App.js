import React from 'react';
import Header from './Header';
import HeritageList from './HeritageList'; // Импортируем компонент HeritageList из соответствующего файла

function App() {
  return (
    <div>
        <Header />
        <main>
            <HeritageList /> {/* Добавляем компонент HeritageList в основной компонент */}
        </main>
    </div>
  );
}

export default App;

