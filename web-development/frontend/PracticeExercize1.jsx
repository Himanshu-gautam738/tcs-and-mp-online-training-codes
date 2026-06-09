```html id="book-app"
<!DOCTYPE html>
<html>
<head>
  <title>Book Shop Application</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/knockout/3.5.1/knockout-min.js"></script>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

<div class="container py-5">
  <h2 class="mb-4 text-center">Book Shop</h2>

  <!-- Add New Book Form -->
  <div class="mb-4 p-3 bg-white border rounded">
    <h5>Add New Book</h5>
    <div class="row g-2 align-items-end">
      <div class="col-md-4">
        <label class="form-label">Book Name</label>
        <input type="text" class="form-control" data-bind="value: newBookName">
      </div>
      <div class="col-md-3">
        <label class="form-label">Quantity</label>
        <input type="number" class="form-control" data-bind="value: newBookQty">
      </div>
      <div class="col-md-3">
        <label class="form-label">Price</label>
        <input type="number" class="form-control" data-bind="value: newBookPrice">
      </div>
      <div class="col-md-2">
        <button class="btn btn-primary w-100" data-bind="click: addBook">Add Book</button>
      </div>
    </div>
  </div>

  <!-- Book List Table -->
  <div class="mb-4 bg-white p-3 border rounded">
    <h5>Available Books</h5>
    <button class="btn btn-sm btn-secondary mb-2" data-bind="click: sortBooks">Sort by Name</button>
    <table class="table table-striped table-bordered">
      <thead>
        <tr>
          <th>Name</th>
          <th>Quantity Available</th>
          <th>Price</th>
          <th>Order</th>
        </tr>
      </thead>
      <tbody data-bind="foreach: books">
        <tr>
          <td data-bind="text: name"></td>
          <td data-bind="text: quantity"></td>
          <td data-bind="text: price"></td>
          <td>
            <input type="number" min="1" class="form-control form-control-sm mb-1" data-bind="value: orderQty">
            <button class="btn btn-success btn-sm w-100" data-bind="click: $parent.addToCart">Add to Cart</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Shopping Cart -->
  <div class="bg-white p-3 border rounded">
    <h5>Shopping Basket</h5>
    <table class="table table-striped table-bordered">
      <thead>
        <tr>
          <th>Book Name</th>
          <th>Quantity</th>
          <th>Price per Item</th>
          <th>Total</th>
        </tr>
      </thead>
      <tbody data-bind="foreach: cart">
        <tr>
          <td data-bind="text: name"></td>
          <td data-bind="text: quantity"></td>
          <td data-bind="text: price"></td>
          <td data-bind="text: price * quantity"></td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <th colspan="3">Grand Total</th>
          <th data-bind="text: grandTotal()"></th>
        </tr>
      </tfoot>
    </table>
  </div>
</div>

<script>
function Book(name, quantity, price) {
    this.name = name;
    this.quantity = ko.observable(quantity);
    this.price = price;
    this.orderQty = ko.observable(1);
}

function AppViewModel() {
    var self = this;

    self.books = ko.observableArray([
        new Book("JavaScript Basics", 10, 250),
        new Book("HTML & CSS Guide", 15, 200),
        new Book("React in Depth", 8, 350)
    ]);

    self.cart = ko.observableArray([]);

    // New book input
    self.newBookName = ko.observable("");
    self.newBookQty = ko.observable(1);
    self.newBookPrice = ko.observable(100);

    // Add new book
    self.addBook = function() {
        if(self.newBookName() && self.newBookQty() > 0 && self.newBookPrice() > 0) {
            self.books.push(new Book(self.newBookName(), parseInt(self.newBookQty()), parseFloat(self.newBookPrice())));
            self.newBookName(""); self.newBookQty(1); self.newBookPrice(100);
        } else {
            alert("Please enter valid book details!");
        }
    };

    // Sort books by name
    self.sortBooks = function() {
        self.books.sort(function(a, b){
            return a.name.localeCompare(b.name);
        });
    };

    // Add book to cart
    self.addToCart = function(book) {
        var qty = parseInt(book.orderQty());
        if(qty <= 0) { alert("Enter a valid quantity"); return; }
        if(qty > book.quantity()) { alert("Not enough stock"); return; }

        // Update cart
        var existing = self.cart().find(item => item.name === book.name);
        if(existing) {
            existing.quantity += qty;
        } else {
            self.cart.push({ name: book.name, quantity: qty, price: book.price });
        }

        // Reduce available stock
        book.quantity(book.quantity() - qty);
        book.orderQty(1);
    };

    // Grand total
    self.grandTotal = ko.computed(function() {
        return self.cart().reduce((sum, item) => sum + (item.price * item.quantity), 0);
    });
}

ko.applyBindings(new AppViewModel());
</script>

</body>
</html>
```
