<?php

require_once __DIR__ . './ParkingSpotType.php';



class ParkingSpot {

    private static int $nextId = 1;

    private readonly int $spotId;

    private ?Vehicle $vehcile = null;

    public function __construct(){
        $this->spotId = self::nextId;
        self::$nextId++;    
    }
}
