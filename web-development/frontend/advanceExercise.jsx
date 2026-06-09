```jsx id="Pagination.jsx"
import React, { useState } from "react";

const Pagination = ({ items, itemsPerPage = 5, renderItem }) => {
  const [currentPage, setCurrentPage] = useState(1);

  const totalPages = Math.ceil(items.length / itemsPerPage);

  // Get current page items
  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = items.slice(indexOfFirstItem, indexOfLastItem);

  const handleNext = () => {
    if (currentPage < totalPages) setCurrentPage(currentPage + 1);
  };

  const handlePrev = () => {
    if (currentPage > 1) setCurrentPage(currentPage - 1);
  };

  return (
    <div>
      <div className="item-list">
        {currentItems.map((item, index) => renderItem(item, index))}
      </div>

      <div className="pagination-buttons mt-3 d-flex justify-content-center gap-2">
        <button className="btn btn-secondary" onClick={handlePrev} disabled={currentPage === 1}>
          Previous
        </button>
        <span className="align-self-center">Page {currentPage} of {totalPages}</span>
        <button className="btn btn-secondary" onClick={handleNext} disabled={currentPage === totalPages}>
          Next
        </button>
      </div>
    </div>
  );
};

export default Pagination;
```
