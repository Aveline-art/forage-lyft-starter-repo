```mermaid
classDiagram
    Car ..> Engine
    Car ..> Battery
    Car ..> Tire
    Engine <|-- CapuletEngine
    Engine <|-- SternmanEngine
    Engine <|-- WilloughbyEngine
    Battery <|-- NubbinBattery
    Battery <|-- SpindlerBattery
    Tire <|-- CarriganTire
    Tire <|-- OctoprimeTire
    class Car{
      +Engine engine
      +Battery battery
      +Tire tire
      +needs_service() bool
    }
    class Engine{
      +needs_service() bool
    }
    class CapuletEngine~Engine~{
      +int last_service_mileage
      +int current_mileage
      +needs_service() bool
    }
    class SternmanEngine~Engine~{
      +bool is_warning_on
      +needs_service() bool
    }
    class WilloughbyEngine~Engine~{
      +int last_service_mileage
      +int current_mileage
      +needs_service() bool
    }
    class Battery{
      +datetime last_service_date
      +needs_service() bool
    }
    class NubbinBattery~Battery~{
      +datetime last_service_date
      +needs_service() bool
    }
    class SpindlerBattery~Battery~{
      +datetime last_service_date
      +needs_service() bool
    }
    class Tire{
      +sensor_values List<int>
      +needs_service() bool
    }
    class CarriganTire~Tire~{
      +sensor_values List<int>
      +needs_service() bool
    }
    class OctoprimeTire~Tire~{
      +sensor_values List<int>
      +needs_service() bool
    }
```

## Notes

- Engine and Battery classes are not implemented with a functioning `needs_service()` function (it will be an abstract method).
  - Specific engines and batteries, such as Spindler or Capulet, will be classes that inherit from their related parts class and implement its own `needs_service()` function
- The `needs_service()` function in a Car class exists to check all parts that are in the car at once, should that function be desirable
  - In order for this function to work optimally, however, the parts should be collected in some kind of array or dict. However, there are no current plans to implement this optimally.

## Requirements

The current service criteria are as follows:

- Engines
  - Capulet Engine - should be serviced once every 30,000 miles
  - Willoughby Engine - should be serviced once every 60,000 miles
  - Sternman Engine - should be serviced only when the warning indicator is on
- Batteries
  - Spindler Battery - should be serviced once every 2 years
  - Nubbin Battery - should be serviced once every 4 years

The current car models are as follows:

- Calliope
  - Capulet Engine
  - Spindler Battery
- Glissade
  - Willoughby Engine
  - Spindler Battery
- Palindrome
  - Sternman Engine
  - Spindler Battery
- Rorschach
  - Willoughby Engine
  - Nubbin Battery
- Thovex
  - Capulet Engine
  - Nubbin Battery
