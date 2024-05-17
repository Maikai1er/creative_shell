import './App.css';
import Header from "./Header";
import About from "./About";
import MenuButton from "./MenuButton";
import HeritageList from "./HeritageList";

function App() {
    return (
        <div>
            <Header />
            <main>
                <MenuButton />
                <About />
                <HeritageList />
            </main>
        </div>
    );
}

export default App;
