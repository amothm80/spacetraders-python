# ShipFrame

The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less maneuverable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol of the frame. | 
**name** | **str** | Name of the frame. | 
**description** | **str** | Description of the frame. | 
**condition** | **float** | The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases. | 
**integrity** | **float** | The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time. | 
**module_slots** | **int** | The amount of slots that can be dedicated to modules installed in the ship. Each installed module take up a number of slots, and once there are no more slots, no new modules can be installed. | 
**mounting_points** | **int** | The amount of slots that can be dedicated to mounts installed in the ship. Each installed mount takes up a number of points, and once there are no more points remaining, no new mounts can be installed. | 
**fuel_capacity** | **int** | The maximum amount of fuel that can be stored in this ship. When refueling, the ship will be refueled to this amount. | 
**requirements** | [**ShipRequirements**](ShipRequirements.md) |  | 

## Example

```python
from openapi_client.models.ship_frame import ShipFrame

# TODO update the JSON string below
json = "{}"
# create an instance of ShipFrame from a JSON string
ship_frame_instance = ShipFrame.from_json(json)
# print the JSON string representation of the object
print(ShipFrame.to_json())

# convert the object into a dict
ship_frame_dict = ship_frame_instance.to_dict()
# create an instance of ShipFrame from a dict
ship_frame_form_dict = ship_frame.from_dict(ship_frame_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

