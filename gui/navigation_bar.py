from typing import Any, Dict, List, Tuple
from flet import (
    NavigationBar,
    NavigationDestination,
    icons,
    Rotate,
    Scale,
    Offset,
    Animation,
    RouteChangeEvent
)
from flet_core.border import Border
from flet_core.buttons import OutlinedBorder
from flet_core.navigation_bar import NavigationBarLabelBehavior
from flet_core.ref import Ref
from flet_core.types import MaterialState


class AppNavigationBar(NavigationBar):

    def __init__(self, destinations: List[NavigationDestination] | None = None, selected_index: int | None = None, bgcolor: str | None = None, label_behavior: NavigationBarLabelBehavior | None = None, elevation: None | int | float = None, shadow_color: str | None = None, indicator_color: str | None = None, indicator_shape: OutlinedBorder | None = None, surface_tint_color: str | None = None, border: Border | None = None, animation_duration: int | None = None, overlay_color: None | str | Dict[MaterialState, str] = None, on_change=None, ref: Ref | None = None, width: None | int | float = None, height: None | int | float = None, left: None | int | float = None, top: None | int | float = None, right: None | int | float = None, bottom: None | int | float = None, expand: None | bool | int = None, expand_loose: bool | None = None, col: Dict[str, int | float] | int | float | None = None, opacity: None | int | float = None, rotate: None | int | float | Rotate = None, scale: None | int | float | Scale = None, offset: None | Offset | Tuple[float | int, float | int] = None, aspect_ratio: None | int | float = None, animate_opacity: None | bool | int | Animation = None, animate_size: None | bool | int | Animation = None, animate_position: None | bool | int | Animation = None, animate_rotation: None | bool | int | Animation = None, animate_scale: None | bool | int | Animation = None, animate_offset: None | bool | int | Animation = None, on_animation_end=None, visible: bool | None = None, disabled: bool | None = None, data: Any = None, adaptive: bool | None = None):
        super().__init__(destinations, selected_index, bgcolor, label_behavior, elevation, shadow_color, indicator_color, indicator_shape, surface_tint_color, border, animation_duration, overlay_color, on_change, ref, width, height, left, top, right, bottom, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, visible, disabled, data, adaptive)
    
        self.destinations = [
            NavigationDestination(
                icon=icons.INVENTORY, label="Invoices"
            ),
            NavigationDestination(
                icon=icons.PRODUCTION_QUANTITY_LIMITS, label="Products"
            )
        ],
        self.bgcolor = "blue"
        self.selected_index = 0
        self.on_change = self.navigation_change

    def navigation_change(self, e: RouteChangeEvent):
        self.selected_index = e.control.selected_index
