import React, { useState, useEffect } from "react";
import axios from "axios";
import Skeleton from "react-loading-skeleton";
import "react-loading-skeleton/dist/skeleton.css";

const API_KEY = "YOUR_OMDB_API_KEY"; // Replace with your OMDb API key

const MovieSearchApp = () => {
    const [query, setQuery] = useState("");
    const [movies, setMovies] = useState([]);
    const [loading, setLoading] = useState(false);
    const [page, setPage] = useState(1);
    const [totalResults, setTotalResults] = useState(0);
    const [debounceTimer, setDebounceTimer] = useState(null);

    // Fetch movies from OMDb API
    const fetchMovies = async (searchQuery, pageNum = 1) => {
        if (!searchQuery) return;
        setLoading(true);
        try {
            const response = await axios.get(
                `https://www.omdbapi.com/?apikey=${API_KEY}&s=${searchQuery}&page=${pageNum}`
            );
            if (response.data.Response === "True") {
                setMovies((prev) => (pageNum === 1 ? response.data.Search : [...prev, ...response.data.Search]));
                setTotalResults(parseInt(response.data.totalResults));
            } else {
                setMovies([]);
                setTotalResults(0);
            }
        } catch (error) {
            console.error(error);
        } finally {
            setLoading(false);
        }
    };

    // Debounced search handler
    const handleSearchChange = (e) => {
        const value = e.target.value;
        setQuery(value);
        setPage(1);

        if (debounceTimer) clearTimeout(debounceTimer);
        const timer = setTimeout(() => {
            fetchMovies(value, 1);
        }, 500); // 500ms debounce
        setDebounceTimer(timer);
    };

    const loadMore = () => {
        const nextPage = page + 1;
        fetchMovies(query, nextPage);
        setPage(nextPage);
    };

    return (
        <div style={{ maxWidth: "900px", margin: "20px auto", padding: "0 20px", fontFamily: "Arial" }}>
            <h1>Movie Search App</h1>
            <input
                type="text"
                placeholder="Search movies..."
                value={query}
                onChange={handleSearchChange}
                style={{ width: "100%", padding: "10px", marginBottom: "20px", fontSize: "1rem" }}
            />

            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill,minmax(150px,1fr))", gap: "15px" }}>
                {loading && Array.from({ length: 6 }).map((_, i) => <Skeleton key={i} height={225} />)}
                {!loading && movies.length === 0 && query && <p>No movies found.</p>}
                {!loading &&
                    movies.map((movie) => (
                        <div key={movie.imdbID} style={{ border: "1px solid #ccc", borderRadius: "8px", overflow: "hidden" }}>
                            <img
                                src={movie.Poster !== "N/A" ? movie.Poster : "https://via.placeholder.com/150x225?text=No+Image"}
                                alt={movie.Title}
                                style={{ width: "100%", height: "225px", objectFit: "cover" }}
                            />
                            <div style={{ padding: "10px" }}>
                                <h3 style={{ fontSize: "1rem", margin: "0 0 5px 0" }}>{movie.Title}</h3>
                                <p style={{ margin: 0 }}>{movie.Year}</p>
                            </div>
                        </div>
                    ))}
            </div>

            {movies.length < totalResults && !loading && (
                <button
                    onClick={loadMore}
                    style={{
                        marginTop: "20px",
                        padding: "10px 20px",
                        fontSize: "1rem",
                        cursor: "pointer",
                    }}
                >
                    Load More
                </button>
            )}
        </div>
    );
};

export default MovieSearchApp;