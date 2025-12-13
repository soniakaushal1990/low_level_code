<?php

require_once __DIR__ . '/VehicleType.php';



class Vehicle {
    public VehicleType $type;
    public string $licenseType;

    public function __construct($type,$licenseType){
        $this->type = $type;
        $this->licenseType = $licenseType;
    }

    public function getVehicleType(){
        $this->type;
    }

    public function getLicensePlate(){
        $this->licenseType;
    }
}

$car = new Vehicle(VehicleType::CAR,'32344');
 
print_r($car);


