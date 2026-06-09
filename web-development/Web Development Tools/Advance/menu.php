<?php
header('Content-Type: application/json');

$menu = [
    "All" => [
        ["id"=>1,"name"=>"Pancakes","price"=>5.99,"image"=>"images/pancakes.jpg","category"=>"Breakfast"],
        ["id"=>2,"name"=>"Burger","price"=>8.99,"image"=>"images/burger.jpg","category"=>"Lunch"],
        ["id"=>3,"name"=>"Chocolate Shake","price"=>4.5,"image"=>"images/shake.jpg","category"=>"Shakes"]
    ],
    "Breakfast" => [
        ["id"=>1,"name"=>"Pancakes","price"=>5.99,"image"=>"images/pancakes.jpg","category"=>"Breakfast"]
    ],
    "Lunch" => [
        ["id"=>2,"name"=>"Burger","price"=>8.99,"image"=>"images/burger.jpg","category"=>"Lunch"]
    ],
    "Shakes" => [
        ["id"=>3,"name"=>"Chocolate Shake","price"=>4.5,"image"=>"images/shake.jpg","category"=>"Shakes"]
    ]
];

// Get category from query param
$category = $_GET['category'] ?? 'All';

echo json_encode($menu[$category]);