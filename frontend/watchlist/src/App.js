import "./App.css";
import aapllogo from "./image/AAPL.png";
import bajlogo from "./image/BAJFIN.png";
import bhellogo from "./image/BHEL.png";
import hdfclogo from "./image/HDFC.png";
import hindlogo from "./image/HINDPETRO.png";

function App() {
  return (
    <div className="App">
      <div my-10>
        <h3>My Watchlist</h3>
      </div>

      <div>
        <img className="photo" src={aapllogo}></img>
        <div className="companies">AAPL 172.570007</div>
        <div className="companies">Apple</div>
        <div style={{ color: "red" }}>1.049988</div>
      </div>
      <div>
        <img className="photo" src={bajlogo}></img>
        <div className="companies">BAJFIN 6714.399902</div>
        <div className="companies">Bajaj Finance</div>
        <div style={{ color: "green" }}>64.399902</div>
      </div>
      <div>
        <img className="photo" src={bhellogo}></img>
        <div className="companies">BHEL 80.949997</div>
        <div className="companies">Bharath Electronics</div>
        <div style={{ color: "red" }}>0.100006</div>
      </div>
      <div>
        <img className="photo" src={hdfclogo}></img>
        <div className="companies">HDFC 1667.800049</div>
        <div className="companies">HDFC Bank</div>
        <div style={{ color: "green" }}>20.800049</div>
      </div>
      <div>
        <img className="photo" src={hindlogo}></img>
        <div className="companies">HINDPETR 260.750000</div>
        <div className="companies">Hindustan Petroleum</div>
        <div style={{ color: "green" }}>2.75</div>
      </div>
    </div>
  );
}

export default App;
