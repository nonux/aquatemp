from dataclasses import dataclass

from custom_components.aqua_temp.common.consts import API_STATUS, POWER_MODE_ON
from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntityDescription,
)
from homeassistant.components.climate import ClimateEntityDescription, HVACMode
from homeassistant.components.select import SelectEntityDescription
from homeassistant.components.sensor import SensorEntityDescription
from homeassistant.const import EntityCategory, Platform, UnitOfTemperature
from homeassistant.helpers.entity import EntityDescription


@dataclass(frozen=True, kw_only=True)
class AquaTempEntityDescription(EntityDescription):
    platform: Platform | None = None
    is_protocol_code: bool = True


@dataclass(frozen=True, kw_only=True)
class AquaTempClimateEntityDescription(
    ClimateEntityDescription, AquaTempEntityDescription
):
    platform: Platform | None = Platform.CLIMATE
    fan_modes: list[str] | None = None
    hvac_modes: list[HVACMode] | list[str] = None


@dataclass(frozen=True, kw_only=True)
class AquaTempBinarySensorEntityDescription(
    BinarySensorEntityDescription, AquaTempEntityDescription
):
    platform: Platform | None = Platform.BINARY_SENSOR
    on_value: str | bool | None = None
    attributes: list[str] | None = None


@dataclass(frozen=True, kw_only=True)
class AquaTempSensorEntityDescription(
    SensorEntityDescription, AquaTempEntityDescription
):
    platform: Platform | None = Platform.SENSOR
    state_class: str | None = None
    convert_to_float: bool = True
    attributes: list[str] | None = None


@dataclass(frozen=True, kw_only=True)
class AquaTempSelectEntityDescription(
    SelectEntityDescription, AquaTempEntityDescription
):
    platform: Platform | None = Platform.SELECT


DEFAULT_ENTITY_DESCRIPTIONS: list[AquaTempEntityDescription] = [
    AquaTempBinarySensorEntityDescription(
        key=API_STATUS,
        name="API Status",
        entity_category=EntityCategory.DIAGNOSTIC,
        is_protocol_code=False,
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        on_value=True,
        translation_key=API_STATUS,
    ),
    AquaTempSelectEntityDescription(
        key="temperature_unit",
        name="Temperature Unit",
        options=[UnitOfTemperature.CELSIUS, UnitOfTemperature.FAHRENHEIT],
        entity_category=EntityCategory.CONFIG,
        is_protocol_code=False,
        translation_key="temperature_unit",
    ),
    AquaTempBinarySensorEntityDescription(
        key="is_fault",
        name="Fault",
        on_value=POWER_MODE_ON,
        is_protocol_code=False,
        device_class=BinarySensorDeviceClass.PROBLEM,
        attributes=["fault"],
        translation_key="is_fault",
    ),
    AquaTempBinarySensorEntityDescription(
        key="device_status",
        name="Status",
        on_value="ONLINE",
        is_protocol_code=False,
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        translation_key="device_status",
    ),
    AquaTempSensorEntityDescription(
        key="last_fault_code",
        name="Last Fault Code",
        is_protocol_code=False,
        convert_to_float=False,
        entity_category=EntityCategory.DIAGNOSTIC,
        attributes=["last_fault_description", "last_fault_time"],
        translation_key="last_fault_code",
    ),
    AquaTempSensorEntityDescription(
        key="last_fault_time",
        name="Last Fault Time",
        is_protocol_code=False,
        convert_to_float=False,
        entity_category=EntityCategory.DIAGNOSTIC,
        translation_key="last_fault_time",
    ),
    AquaTempSensorEntityDescription(
        key="fault_history_count",
        name="Fault History",
        is_protocol_code=False,
        convert_to_float=False,
        entity_category=EntityCategory.DIAGNOSTIC,
        attributes=["fault_history"],
        translation_key="fault_history",
    ),
    AquaTempClimateEntityDescription(key="Mode", name=None, translation_key="mode"),
]
