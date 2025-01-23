
import MainContentPage from "./component/MainPage/MainContentPage"
import Header from "./component/Header/Header"
import { Provider } from 'react-redux';
import { store } from './component/Store/Store';
function App() {

  return (
    <>
    <Provider store={store}>
    <Header/>
     <MainContentPage/>
     </Provider>
    </>
  )
}

export default App
