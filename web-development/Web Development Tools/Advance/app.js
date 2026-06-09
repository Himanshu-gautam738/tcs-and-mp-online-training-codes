const { useState, useEffect } = React;

function App() {
    const [category, setCategory] = useState("All");
    const [menuItems, setMenuItems] = useState([]);
    const [cart, setCart] = useState([]);

    // Fetch menu from PHP API
    useEffect(() => {
        fetch(`backend/menu.php?category=${category}`)
            .then(res => res.json())
            .then(data => setMenuItems(data));
    }, [category]);

    const addToCart = (item) => {
        setCart(prev => [...prev, item]);
    };

    return (
        <div style={{ maxWidth: "900px", margin: "20px auto", fontFamily: "Arial" }}>
            <h1>Restaurant Menu</h1>

            {/* Category Buttons */}
            <div style={{ marginBottom: "20px" }}>
                {["All", "Breakfast", "Lunch", "Shakes"].map(cat => (
                    <button
                        key={cat}
                        onClick={() => setCategory(cat)}
                        style={{ margin: "0 5px", padding: "10px 15px", cursor: "pointer" }}
                    >
                        {cat}
                    </button>
                ))}
            </div>

            {/* Menu Items */}
            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill,minmax(150px,1fr))", gap: "15px" }}>
                {menuItems.map(item => (
                    <div key={item.id} style={{ border: "1px solid #ccc", borderRadius: "8px", overflow: "hidden" }}>
                        <img src={item.image} alt={item.name} style={{ width: "100%", height: "150px", objectFit: "cover" }} />
                        <div style={{ padding: "10px" }}>
                            <h3 style={{ margin: "0 0 5px 0" }}>{item.name}</h3>
                            <p>${item.price.toFixed(2)}</p>
                            <button onClick={() => addToCart(item)}>Add to Cart</button>
                        </div>
                    </div>
                ))}
            </div>

            {/* Cart */}
            <h2>Cart</h2>
            <ul>
                {cart.map((item, idx) => (
                    <li key={idx}>{item.name} - ${item.price.toFixed(2)}</li>
                ))}
            </ul>
        </div>
    );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);